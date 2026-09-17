"""Render map.json into MAP.md (the browsable per-endpoint table)."""
import json, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return (s or "").replace("|", "\\|")


def main():
    m = json.load(open(os.path.join(HERE, "map.json")))
    ops = m["operations"]
    dep = m["deprecation"]
    out = []
    w = out.append

    breaking = [o for o in ops if o["breaking"]]
    removed = [o for o in ops if o["status"] == "REMOVED"]
    nodbv = [o for o in ops if o["status"] == "NO_DBV_VERSION"]

    w("# HubSpot legacy → date-based versioning: the per-endpoint map\n")
    w(f"Generated from HubSpot's own public OpenAPI catalogue "
      f"(`{m['generated_from']}`).\n")
    w(f"- **{m['summary']['operations']}** legacy operations across "
      f"**{m['summary']['apis']}** APIs")
    w(f"- **{len(removed)}** have no date-based counterpart at all")
    w(f"- **{len(breaking)}** have at least one difference that breaks a caller")
    w(f"- **{len(nodbv)}** sit in APIs with no date-based version published yet\n")
    w("| | |")
    w("|---|---|")
    w(f"| v1–v3 unsupported | {dep['v1_v3_enforcement']} |")
    w(f"| v4 unsupported | {dep['v4_enforcement']} |")
    w(f"| legacy private app creation ends (new accounts) | "
      f"{dep['legacy_private_app_creation_ends_new_accounts']} |")
    w(f"| legacy private app creation ends (existing accounts) | "
      f"{dep['legacy_private_app_creation_ends_existing_accounts']} |")
    w("")

    w("## 1. No date-based counterpart\n")
    w("These calls cannot be version-bumped. They have to be rewritten against a "
      "different endpoint or dropped.\n")
    w("| API | Method | Legacy path | What it did |")
    w("|---|---|---|---|")
    for o in sorted(removed, key=lambda x: (x["api"], x["legacy_path"])):
        w(f"| {esc(o['api'])} | {o['method']} | `{o['legacy_path']}` | {esc(o.get('summary') or '—')} |")
    w("")

    if nodbv:
        w("## 2. APIs with no date-based version yet\n")
        w("Nothing to migrate *to* as of the generation date. Watch these.\n")
        w("| API | Method | Legacy path |")
        w("|---|---|---|")
        for o in sorted(nodbv, key=lambda x: (x["api"], x["legacy_path"])):
            w(f"| {esc(o['api'])} | {o['method']} | `{o['legacy_path']}` |")
        w("")

    w("## 3. Breaking differences\n")
    w("Same operation exists, but something a caller depends on changed.\n")
    by_api = collections.defaultdict(list)
    for o in breaking:
        if o["status"] in ("REMOVED", "NO_DBV_VERSION"):
            continue
        by_api[o["api"]].append(o)
    for api in sorted(by_api):
        w(f"### {api}\n")
        for o in sorted(by_api[api], key=lambda x: x["legacy_path"]):
            w(f"**{o['method']} `{o['legacy_path']}`** → `{o['target_path']}` "
              f"({o['target_version']})\n")
            for c in o["changes"]:
                if c["breaking"]:
                    w(f"- **{c['change']}** — {c['detail']}")
            w("")

    w("## 4. Everything else\n")
    w("Operations that map cleanly. The path shape still changes — the version "
      "segment moves — so this is not a no-op, but nothing a caller reads or "
      "sends is affected.\n")
    w("| API | Method | Legacy | Date-based | Status |")
    w("|---|---|---|---|---|")
    for o in sorted(ops, key=lambda x: (x["api"], x["legacy_path"])):
        if o["breaking"] or o["status"] in ("REMOVED", "NO_DBV_VERSION"):
            continue
        w(f"| {esc(o['api'])} | {o['method']} | `{o['legacy_path']}` | "
          f"`{o['target_path']}` | {o['status']} |")
    w("")

    open(os.path.join(HERE, "MAP.md"), "w").write("\n".join(out))
    print(f"MAP.md: {len(out)} lines, {len(removed)} removed, {len(breaking)} breaking")


if __name__ == "__main__":
    main()
