"""Download HubSpot's public OpenAPI catalogue and every spec it points at.

HubSpot announced (2026-09-15) that v1-v3 APIs go unsupported in Sept 2027 and
v4 in March 2027, and said per-endpoint replacement docs will not land until
March 2027.  The specs themselves are public today, so the mapping can be
derived six months before HubSpot publishes it.
"""
import json, os, time, urllib.request, urllib.error

CATALOG = "https://api.hubspot.com/public/api/spec/v1/specs"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hubspot-dbv-map/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.load(r)
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def slug(*parts):
    return "_".join(str(p) for p in parts).replace("/", "-").replace(" ", "-").lower()


def main():
    os.makedirs(DATA, exist_ok=True)
    catalog = get(CATALOG)
    json.dump(catalog, open(os.path.join(DATA, "_catalog.json"), "w"), indent=1)
    apis = catalog["results"]
    todo = []
    for api in apis:
        for v in api.get("versions", []):
            if v.get("openApi"):
                todo.append((api["name"], api.get("group"), v["version"], v.get("stage"), v["openApi"]))
    print(f"{len(apis)} APIs, {len(todo)} specs")
    ok = fail = cached = 0
    for name, group, version, stage, url in todo:
        path = os.path.join(DATA, slug(name, version) + ".json")
        if os.path.exists(path) and os.path.getsize(path) > 50:
            cached += 1
            continue
        try:
            spec = get(url)
        except Exception as e:
            print("FAIL", name, version, e)
            fail += 1
            continue
        spec["_meta"] = {"api": name, "group": group, "version": version, "stage": stage, "url": url}
        json.dump(spec, open(path, "w"))
        ok += 1
        if ok % 25 == 0:
            print("  fetched", ok)
    print(f"fetched {ok}, cached {cached}, failed {fail}")


if __name__ == "__main__":
    main()
