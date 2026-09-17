"""Diff HubSpot's legacy (v1-v4) OpenAPI specs against date-based versioning.

HubSpot's own per-endpoint replacement documentation is not due until March
2027, but both sides of the mapping are already public.  This derives the map
mechanically: every legacy operation, its DBV counterpart, and the field-level
differences that will actually break a caller.

Output: map.json (machine-readable) and MAP.md (human-readable).
"""
import json, os, re, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

LEGACY_RE = re.compile(r"^\d+$")          # 1, 2, 3, 4
DBV_RE = re.compile(r"^\d{4}-\d{2}$")     # 2026-03, 2026-09
VERSION_SEG = re.compile(r"/(v\d+|\d{4}-\d{2})(?=/|$)")

MAX_DEPTH = 6


# --------------------------------------------------------------------------
# spec loading

def load_specs():
    """name -> {version: spec}"""
    by_api = collections.defaultdict(dict)
    for path in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        if os.path.basename(path).startswith("_"):
            continue
        try:
            spec = json.load(open(path))
        except Exception:
            continue
        meta = spec.get("_meta") or {}
        if not meta.get("api"):
            continue
        by_api[meta["api"]][meta["version"]] = spec
    return by_api


def normalize_path(p):
    """Strip the version segment wherever it sits, so the two sides line up.

    Date-based versioning does not just rename the segment, it *moves* it:
        /crm/v3/objects/contacts   ->  /crm/objects/2026-09/contacts
    so substituting `/v3/` for `/2026-09/` in place yields a 404.  Comparing the
    version-free skeleton is what actually pairs the operations.
    """
    return VERSION_SEG.sub("", p, count=1) or "/"


def version_moved(old_path, new_path):
    """True when the version segment sits at a different depth in the new path."""
    def idx(p):
        parts = [s for s in p.split("/") if s]
        for i, s in enumerate(parts):
            if re.fullmatch(r"v\d+|\d{4}-\d{2}", s):
                return i
        return -1
    return idx(old_path) != idx(new_path)


# --------------------------------------------------------------------------
# schema flattening

def resolve(spec, node, seen):
    """Follow a local $ref one hop. Returns (node, seen)."""
    hops = 0
    while isinstance(node, dict) and "$ref" in node and hops < 20:
        ref = node["$ref"]
        if not ref.startswith("#/"):
            return {}, seen
        if ref in seen:
            return {"type": "<recursive>"}, seen
        seen = seen | {ref}
        cur = spec
        for part in ref[2:].split("/"):
            if not isinstance(cur, dict) or part not in cur:
                return {}, seen
            cur = cur[part]
        node = cur
        hops += 1
    return node, seen


def flatten(spec, schema, prefix="", depth=0, seen=frozenset()):
    """Schema -> {dotted.field: descriptor}. Descriptor captures the things
    whose change actually breaks a caller: type, enum, format, required."""
    out = {}
    if depth > MAX_DEPTH or not isinstance(schema, dict):
        return out
    schema, seen = resolve(spec, schema, seen)
    if not isinstance(schema, dict):
        return out

    for key in ("allOf", "oneOf", "anyOf"):
        for sub in schema.get(key) or []:
            out.update(flatten(spec, sub, prefix, depth + 1, seen))

    t = schema.get("type")
    if t == "array":
        out.update(flatten(spec, schema.get("items") or {}, prefix + "[]", depth + 1, seen))
        return out

    props = schema.get("properties")
    if isinstance(props, dict):
        required = set(schema.get("required") or [])
        for name, sub in props.items():
            field = f"{prefix}.{name}" if prefix else name
            sub_r, sub_seen = resolve(spec, sub, seen)
            sub_r = sub_r if isinstance(sub_r, dict) else {}
            # Recurse first, then write the parent's own descriptor: a scalar
            # leaf re-describes itself under the same key and would otherwise
            # clobber the `required` flag that only the parent schema knows.
            child = flatten(spec, sub, field, depth + 1, sub_seen)
            child.pop(field, None)
            out.update(child)
            out[field] = {
                "type": sub_r.get("type"),
                "format": sub_r.get("format"),
                "enum": sorted(map(str, sub_r.get("enum"))) if isinstance(sub_r.get("enum"), list) else None,
                "required": name in required,
            }
        return out

    if prefix and not out:
        out[prefix] = {
            "type": t,
            "format": schema.get("format"),
            "enum": sorted(map(str, schema.get("enum"))) if isinstance(schema.get("enum"), list) else None,
            "required": False,
        }
    return out


def body_schema(spec, op):
    rb, _ = resolve(spec, op.get("requestBody") or {}, frozenset())
    if not isinstance(rb, dict):
        return {}
    content = rb.get("content") or {}
    for mime in ("application/json", "*/*"):
        if mime in content:
            return flatten(spec, (content[mime] or {}).get("schema") or {})
    for v in content.values():
        return flatten(spec, (v or {}).get("schema") or {})
    return {}


def response_schema(spec, op):
    for code, resp in (op.get("responses") or {}).items():
        if not str(code).startswith("2"):
            continue
        resp, _ = resolve(spec, resp, frozenset())
        content = (resp or {}).get("content") or {}
        for v in content.values():
            return flatten(spec, (v or {}).get("schema") or {})
    return {}


def params(spec, op, path_item):
    out = {}
    for p in list(path_item.get("parameters") or []) + list(op.get("parameters") or []):
        p, _ = resolve(spec, p, frozenset())
        if not isinstance(p, dict) or not p.get("name"):
            continue
        sch, _ = resolve(spec, p.get("schema") or {}, frozenset())
        sch = sch if isinstance(sch, dict) else {}
        out[f"{p.get('in')}:{p['name']}"] = {
            "type": sch.get("type"),
            "enum": sorted(map(str, sch["enum"])) if isinstance(sch.get("enum"), list) else None,
            "required": bool(p.get("required")),
        }
    return out


def scopes(op):
    """Acceptable OAuth scopes for an operation.

    OpenAPI `security` is a list of ALTERNATIVES - any one entry satisfies the
    call - so this is the set of scopes that are *accepted*, not required.  The
    legacy specs mostly declare nothing at all while the date-based specs
    enumerate every acceptable scope, so a naive set-difference reports ~80
    "newly required scopes" per operation, all of them false.  Only the
    subtractive direction is meaningful.
    """
    got = set()
    for entry in op.get("security") or []:
        for vals in entry.values():
            got.update(vals or [])
    return sorted(got)


# --------------------------------------------------------------------------
# diffing

def diff_fields(old, new, kind, response=False):
    """Field-level differences, each tagged breaking or not.

    Direction matters.  A newly-required *request* field breaks the caller; a
    newly-required *response* field does not - the server is promising more,
    not demanding more.  Only removals and type changes break a reader.
    """
    changes = []
    for name, o in old.items():
        n = new.get(name)
        if n is None:
            changes.append({"kind": kind, "field": name, "change": "removed", "breaking": True,
                            "detail": f"{kind} `{name}` no longer exists"})
            continue
        if o.get("type") != n.get("type") and (o.get("type") or n.get("type")):
            changes.append({"kind": kind, "field": name, "change": "type_changed", "breaking": True,
                            "detail": f"type {o.get('type')} -> {n.get('type')}"})
        if o.get("format") != n.get("format") and (o.get("format") or n.get("format")):
            changes.append({"kind": kind, "field": name, "change": "format_changed", "breaking": True,
                            "detail": f"format {o.get('format')} -> {n.get('format')}"})
        if o.get("enum") and n.get("enum") and o["enum"] != n["enum"]:
            dropped = sorted(set(o["enum"]) - set(n["enum"]))
            added = sorted(set(n["enum"]) - set(o["enum"]))
            changes.append({"kind": kind, "field": name, "change": "enum_changed",
                            "breaking": bool(dropped),
                            "detail": (f"values removed: {', '.join(dropped)}; " if dropped else "")
                                      + (f"values added: {', '.join(added)}" if added else "")})
        if n.get("required") and not o.get("required"):
            changes.append({"kind": kind, "field": name, "change": "now_required", "breaking": not response,
                            "detail": f"{kind} `{name}` is now required"})
    for name, n in new.items():
        if name in old:
            continue
        changes.append({"kind": kind, "field": name, "change": "added",
                        "breaking": bool(n.get("required")) and not response,
                        "detail": f"new {'required ' if n.get('required') else ''}{kind} `{name}`"})
    return changes


def dbv_versions(versions):
    """Non-beta date-based versions, newest first."""
    return sorted((v for v in versions if DBV_RE.match(v)), reverse=True)


def operations(spec):
    ops = {}
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, op in item.items():
            if method.lower() not in ("get", "post", "put", "patch", "delete"):
                continue
            ops[(method.lower(), normalize_path(path))] = (path, op, item)
    return ops


def build():
    by_api = load_specs()
    entries = []
    api_rows = []

    for api_name in sorted(by_api):
        versions = by_api[api_name]
        dbvs = dbv_versions(versions)
        target_v = dbvs[0] if dbvs else None
        legacy_vs = sorted((v for v in versions if LEGACY_RE.match(v)), key=int)
        if not legacy_vs:
            continue
        row = {"api": api_name, "legacy": legacy_vs, "target": target_v,
               "group": (versions[legacy_vs[0]].get("_meta") or {}).get("group")}
        api_rows.append(row)
        if not target_v:
            for lv in legacy_vs:
                for (method, npath), (rawpath, op, _item) in operations(versions[lv]).items():
                    entries.append({
                        "api": api_name, "group": row["group"], "legacy_version": lv,
                        "method": method.upper(), "legacy_path": rawpath,
                        "target_version": None, "target_path": None,
                        "status": "NO_DBV_VERSION", "breaking": True, "changes": [],
                        "note": "this API has no date-based version published yet",
                    })
            continue

        # Index every date-based version, newest first: an endpoint that is gone
        # from 2026-09 but alive in 2026-03 is a different (and softer) problem
        # than one with no date-based home at all.
        by_version = []
        for dv in dbvs:
            ops = operations(versions[dv])
            opid = {}
            for k, (_p, o, _i) in ops.items():
                if o.get("operationId"):
                    opid.setdefault(o["operationId"], k)
            by_version.append((dv, versions[dv], ops, opid))

        for lv in legacy_vs:
            old_spec = versions[lv]
            for (method, npath), (rawpath, op, item) in operations(old_spec).items():
                hit = None
                for dv, spec_v, ops_v, opid_v in by_version:
                    if (method, npath) in ops_v:
                        hit = (dv, spec_v, ops_v, (method, npath), "path")
                        break
                    if op.get("operationId") and op["operationId"] in opid_v:
                        hit = (dv, spec_v, ops_v, opid_v[op["operationId"]], "operationId")
                        break

                if hit:
                    found_v, new_spec, new_ops, key, matched_by = hit
                    dropped_after = found_v if found_v != target_v else None
                else:
                    matched_by = None

                if not matched_by:
                    entries.append({
                        "api": api_name, "group": row["group"], "legacy_version": lv,
                        "method": method.upper(), "legacy_path": rawpath,
                        "target_version": target_v, "target_path": None,
                        "status": "REMOVED", "breaking": True, "changes": [],
                        "note": "no counterpart in the date-based version - this call has to be "
                                "rewritten or dropped",
                        "operation_id": op.get("operationId"),
                        "summary": op.get("summary"),
                    })
                    continue

                new_raw, new_op, new_item = new_ops[key]
                changes = []
                if version_moved(rawpath, new_raw):
                    changes.append({
                        "kind": "path", "field": rawpath, "change": "version_segment_moved",
                        # Checked live 2026-09-17: both shapes still route (401, not 404),
                        # so this is not yet a hard break - but only the new shape is
                        # documented, and an undocumented route is not a contract.
                        "breaking": False,
                        "detail": f"the version segment moves position: `{rawpath}` -> `{new_raw}`. "
                                  f"A find-and-replace of the version in place is NOT the documented "
                                  f"form (it happens to still route today; that is not a promise).",
                    })
                changes += diff_fields(params(old_spec, op, item), params(new_spec, new_op, new_item), "param")
                changes += diff_fields(body_schema(old_spec, op), body_schema(new_spec, new_op), "request field")
                changes += diff_fields(response_schema(old_spec, op), response_schema(new_spec, new_op),
                                       "response field", response=True)
                old_sc, new_sc = scopes(op), scopes(new_op)
                if old_sc and new_sc:
                    lost = sorted(set(old_sc) - set(new_sc))
                    if lost:
                        changes.append({"kind": "scope", "field": ",".join(lost), "change": "scope_no_longer_accepted",
                                        "breaking": True,
                                        "detail": "OAuth scope(s) that used to authorise this call are no longer "
                                                  f"listed as acceptable: {', '.join(lost)}"})

                if dropped_after:
                    changes.append({
                        "kind": "version", "field": rawpath, "change": "dropped_after_version",
                        "breaking": True,
                        "detail": f"present in {found_v} but gone from the latest version ({target_v}): "
                                  f"pin {found_v} or rewrite before it lapses too",
                    })

                breaking = any(c["breaking"] for c in changes)
                entries.append({
                    "api": api_name, "group": row["group"], "legacy_version": lv,
                    "method": method.upper(), "legacy_path": rawpath,
                    "target_version": found_v, "target_path": new_raw,
                    "latest_version": target_v,
                    "status": ("MOVED" if matched_by == "operationId" else
                               ("BREAKING" if breaking else ("CHANGED" if changes else "IDENTICAL"))),
                    "breaking": breaking or matched_by == "operationId",
                    "matched_by": matched_by,
                    "changes": changes,
                    "operation_id": op.get("operationId"),
                    "summary": op.get("summary"),
                })

    return entries, api_rows


def write(entries, api_rows):
    counts = collections.Counter(e["status"] for e in entries)
    out = {
        "generated_from": "https://api.hubspot.com/public/api/spec/v1/specs",
        "deprecation": {
            "announced": "2026-09-15",
            "v1_v3_enforcement": "2027-09",
            "v4_enforcement": "2027-03-30",
            "legacy_private_app_creation_ends_new_accounts": "2026-09-28",
            "legacy_private_app_creation_ends_existing_accounts": "2026-10-26",
            "source": "https://developers.hubspot.com/changelog/"
                      "legacy-apis-and-legacy-apps-whats-going-unsupported-and-when",
        },
        "summary": {"apis": len(api_rows), "operations": len(entries), "by_status": dict(counts)},
        "apis": api_rows,
        "operations": entries,
    }
    json.dump(out, open(os.path.join(HERE, "map.json"), "w"), indent=1)
    print(json.dumps(out["summary"], indent=1))
    return out


if __name__ == "__main__":
    e, a = build()
    write(e, a)
