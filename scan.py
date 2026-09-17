"""Scan a codebase for HubSpot calls that stop being supported in 2027.

    python3 scan.py /path/to/repo

Reads map.json (built by build_map.py from HubSpot's own OpenAPI specs) and
reports, per legacy call found, where it maps to and what will break.
"""
import argparse, json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))

SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", "__pycache__",
             ".next", ".venv", "venv", "target", ".idea", ".gradle", "coverage"}
SCAN_EXT = {".js", ".jsx", ".ts", ".tsx", ".py", ".rb", ".php", ".java", ".kt",
            ".go", ".cs", ".sh", ".json", ".yml", ".yaml", ".md", ".txt", ".env",
            ".tf", ".ex", ".exs", ".rs", ".scala", ".pl", ".ps1"}
MAX_BYTES = 2_000_000

# A HubSpot path with a numbered version segment, with or without the host.
PATH_RE = re.compile(r"(?:https?://api\.hubapi\.com)?(/[A-Za-z0-9_\-./{}$:]*?/v[1-4](?:/[A-Za-z0-9_\-./{}$:%]*)?)")
HAPIKEY_RE = re.compile(r"\bhapikey\b", re.I)
PRIVATE_TOKEN_RE = re.compile(r"\bpat-[a-z0-9]{2,6}-[0-9a-f\-]{8,}", re.I)
SDK_RE = re.compile(r"""['"](@hubspot/api-client|hubspot-api-client|@hubspot/cli)['"]|"""
                    r"""\bfrom\s+hubspot\b|\brequire\(['"]hubspot""")

VAR_SEG = re.compile(r"^(\{[^}]*\}|\$\{[^}]*\}|:[A-Za-z_]\w*|\d+|[A-Za-z_]\w*Id|%s|\?)$")


def skeleton(path):
    """Collapse a concrete path to the shape used as a map key.

    /crm/v3/objects/contacts/12345  ->  /crm/objects/contacts/*
    Keeps literal segments, replaces anything that looks like an id or a
    template placeholder with *, and drops the version segment.
    """
    parts = [p for p in path.split("?")[0].split("/") if p]
    out = []
    for p in parts:
        if re.fullmatch(r"v[1-4]", p):
            continue
        out.append("*" if VAR_SEG.match(p) else p)
    return "/" + "/".join(out)


def load_index():
    """Index map operations into a segment trie.

    A call site writes concrete values where the spec writes placeholders -
    `/crm/v3/associations/contacts/deals/batch/create` against
    `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create` - so a
    plain dict lookup misses. `*` nodes in the trie match any single segment,
    and literal nodes win when both could match.
    """
    m = json.load(open(os.path.join(HERE, "map.json")))
    root = {}
    for o in m["operations"]:
        node = root
        for seg in [s for s in skeleton(o["legacy_path"]).split("/") if s]:
            node = node.setdefault(seg, {})
        node.setdefault("$", []).append(o)
    return m, root


def lookup(trie, path_skeleton):
    """All operations whose path template matches this concrete skeleton."""
    segs = [s for s in path_skeleton.split("/") if s]

    def walk(node, i):
        if i == len(segs):
            return list(node.get("$", []))
        out = []
        for key in (segs[i], "*"):
            child = node.get(key)
            if child is not None:
                out += walk(child, i + 1)
        return out

    return walk(trie, 0)


def iter_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext and ext not in SCAN_EXT:
                continue
            full = os.path.join(dirpath, name)
            try:
                if os.path.getsize(full) > MAX_BYTES:
                    continue
            except OSError:
                continue
            yield full


METHOD_RE = re.compile(
    r"""\bmethod\s*[:=]\s*['"](?P<m1>get|post|put|patch|delete)['"]"""
    r"""|\b(?:requests|axios|http|client|session|fetch)\s*\.\s*(?P<m2>get|post|put|patch|delete)\b"""
    r"""|\.(?P<m3>get|post|put|patch|delete)\s*\("""
    r"""|-X\s*(?P<m4>GET|POST|PUT|PATCH|DELETE)\b""", re.I)


def detect_method(line):
    match = METHOD_RE.search(line)
    if not match:
        return None
    return next(v for v in match.groupdict().values() if v).upper()


def scan(root):
    m, idx = load_index()
    findings = []
    other = []
    for full in iter_files(root):
        try:
            text = open(full, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        rel = os.path.relpath(full, root)
        for lineno, line in enumerate(text.splitlines(), 1):
            for match in PATH_RE.finditer(line):
                raw = match.group(1)
                ops = lookup(idx, skeleton(raw))
                if not ops:
                    continue
                method = detect_method(line)
                if method:
                    exact = [o for o in ops if o["method"] == method]
                    ops = exact or ops
                # Without a detectable verb, report the worst case rather than
                # quietly picking a clean one and calling the file migrated.
                op = max(ops, key=lambda o: (o["status"] == "REMOVED", o["breaking"]))
                findings.append({"file": rel, "line": lineno, "path": raw,
                                 "op": op, "method_detected": bool(method),
                                 "source": line.strip()[:160]})
            if HAPIKEY_RE.search(line):
                other.append({"file": rel, "line": lineno, "kind": "hapikey",
                              "detail": "API-key (hapikey) auth - removed by HubSpot, "
                                        "must be an OAuth or private-app token"})
            if PRIVATE_TOKEN_RE.search(line):
                other.append({"file": rel, "line": lineno, "kind": "legacy_private_app_token",
                              "detail": "legacy private app token (pat-...). Legacy private apps "
                                        "go unsupported in Sept 2027; creation stops 2026-09-28 "
                                        "for new accounts, 2026-10-26 for existing ones"})
            if SDK_RE.search(line):
                other.append({"file": rel, "line": lineno, "kind": "sdk",
                              "detail": "HubSpot SDK import - the SDK pins legacy paths "
                                        "internally; an SDK upgrade is part of the migration"})
    return m, findings, other


def report(m, findings, other, root, as_json=False):
    if as_json:
        print(json.dumps({"root": root, "findings": [
            {k: v for k, v in f.items() if k != "op"} | {
                "api": f["op"]["api"], "method": f["op"]["method"],
                "status": f["op"]["status"], "breaking": f["op"]["breaking"],
                "target_path": f["op"]["target_path"],
                "target_version": f["op"].get("target_version"),
                "changes": f["op"]["changes"]}
            for f in findings], "other": other}, indent=1))
        return

    dep = m["deprecation"]
    print(f"\nHubSpot legacy API scan — {root}")
    print(f"v1–v3 unsupported {dep['v1_v3_enforcement']} · v4 unsupported {dep['v4_enforcement']}\n")

    if not findings and not other:
        print("No legacy HubSpot API calls found.\n")
        return

    buckets = collections.OrderedDict([("REMOVED", []), ("BREAKING", []), ("MOVED", []),
                                       ("NO_DBV_VERSION", []), ("CHANGED", []), ("IDENTICAL", [])])
    for f in findings:
        buckets.setdefault(f["op"]["status"], []).append(f)

    labels = {
        "REMOVED": "NO REPLACEMENT — must be rewritten",
        "NO_DBV_VERSION": "NO DATE-BASED VERSION PUBLISHED YET",
        "BREAKING": "BREAKING — the shape of the call or its response changed",
        "MOVED": "MOVED — matched by operation id, path differs",
        "CHANGED": "changes, none of them breaking",
        "IDENTICAL": "clean version bump",
    }
    for status, items in buckets.items():
        if not items:
            continue
        print(f"── {labels[status]}  ({len(items)})")
        for f in items:
            op = f["op"]
            verb = op["method"] if f.get("method_detected") else f"{op['method']}?"
            print(f"   {f['file']}:{f['line']}  {verb} {f['path']}")
            if op["target_path"]:
                print(f"      → {op['target_path']}  ({op['target_version']})")
            for c in op["changes"]:
                if c["breaking"]:
                    print(f"      ! {c['detail']}")
        print()

    if other:
        print(f"── auth and SDK  ({len(other)})")
        seen = set()
        for o in other:
            key = (o["kind"], o["file"])
            if key in seen:
                continue
            seen.add(key)
            print(f"   {o['file']}:{o['line']}  {o['detail']}")
        print()

    hard = len(buckets["REMOVED"]) + len(buckets["BREAKING"]) + len(buckets["NO_DBV_VERSION"])
    print(f"{len(findings)} legacy call sites, {hard} needing more than a version bump.\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    m, findings, other = scan(root)
    report(m, findings, other, root, as_json=args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
