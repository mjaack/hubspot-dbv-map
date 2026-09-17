# HubSpot legacy → date-based versioning map

On **15 September 2026** HubSpot announced that `/v1/`, `/v2/` and `/v3/` API
paths, legacy public apps and legacy private apps all go unsupported, with
enforcement in **September 2027**. `/v4/` goes first, on **30 March 2027**.
Replacement is date-based versioning — `2026-03`, `2026-09` — and HubSpot's own
guidance is to jump straight to it: *"Do not use v3 or v4 as an intermediate
step."*

From the same announcement: **complete per-endpoint replacement documentation
arrives in March 2027.** Twelve months after the clock starts, six months before
it stops.

Both sides of that mapping are already public, though, in HubSpot's own OpenAPI
specs. This repo derives the map today by diffing them.

| | |
|---|---|
| v1–v3 unsupported | **September 2027** |
| v4 unsupported | **30 March 2027** |
| legacy private app creation ends, new accounts | **28 September 2026** |
| legacy private app creation ends, existing accounts | **26 October 2026** |

Source: [HubSpot developer changelog](https://developers.hubspot.com/changelog/legacy-apis-and-legacy-apps-whats-going-unsupported-and-when)

## What's in here

**[`MAP.md`](MAP.md)** — every legacy operation, where it lands in date-based
versioning, and what changed. **[`map.json`](map.json)** — the same thing for
machines.

Across **1,040 legacy operations in 98 APIs**:

- **44** have **no date-based counterpart at all.** They can't be version-bumped;
  they have to be rewritten or dropped. That includes all of Timeline events,
  the `communication-preferences` subscribe/unsubscribe endpoints, OAuth token
  introspection, and `marketing/v4/email/single-send`.
- **95** have a difference that breaks a caller — a request or response field
  removed, a parameter gone, a field newly required, a type changed.
- **18** sit in APIs that have no date-based version published yet, so there is
  nothing to migrate *to* as of the generation date.
- The rest map cleanly, but **the path shape still changes**: the version
  segment moves position, `/crm/v3/objects/contacts` →
  `/crm/objects/2026-09/contacts`. A find-and-replace of `v3` for `2026-09` is
  not the documented form.

Some specifics, as a flavour of what the diff turns up:

- `POST /crm/v3/associations/{from}/{to}/batch/create` — the request field
  `inputs[].type` is gone, replaced by a required `inputs[].types`. Silent
  400s if you miss it.
- `POST /crm/v3/lists/search` — `listIds` and `processingTypes` are now
  required.
- `GET /crm/v3/objects/{type}/{id}/associations/{toType}` — the `includeFA`
  parameter is gone and the response items no longer carry `id` or `type`.
- Webhooks `v3` app settings and subscriptions exist in `2026-03` but **not** in
  `2026-09`.

## Scan your own code

```bash
git clone https://github.com/mjaack/hubspot-dbv-map
cd hubspot-dbv-map
python3 scan.py /path/to/your/repo
```

No dependencies, Python 3.8+, nothing leaves your machine. It reports every
legacy call site, where it maps to, what breaks, and flags `hapikey` auth and
legacy private-app (`pat-…`) tokens. `--json` for machine output.

```
── NO REPLACEMENT — must be rewritten  (2)
   src/sync/timeline.ts:41  POST /integrators/timeline/v3/{appId}/event-templates

── BREAKING — the shape of the call or its response changed  (1)
   src/crm/assoc.ts:88  POST /crm/v3/associations/contacts/deals/batch/create
      → /crm/associations/2026-09/contacts/deals/batch/create  (2026-09)
      ! request field `inputs[].type` no longer exists
      ! new required request field `inputs[].types`
```

## How the map is derived

1. `fetch_specs.py` pulls HubSpot's public catalogue
   (`https://api.hubspot.com/public/api/spec/v1/specs`, 122 APIs) and every
   OpenAPI document it points at — 334 specs, unauthenticated.
2. `build_map.py` pairs legacy operations with date-based ones on the
   *version-free path skeleton*, falling back to `operationId`, then diffs
   parameters, request bodies, responses and accepted scopes field by field
   with `$ref`s resolved.
3. `render.py` writes `MAP.md`.

Re-run any of them; the inputs are public and the output is deterministic.

## What this map does *not* claim

Accuracy is the whole product, so here is what was checked and what was thrown
out:

- **The moved version segment is not (yet) a hard break.** Checked live on
  2026-09-17: `/crm/2026-09/objects/contacts` and `/crm/objects/2026-09/contacts`
  both route — 401 without credentials, where a bogus path gives 404. Only the
  second is documented. The map flags the shape change but does not call it
  breaking.
- **"328 endpoints now require new OAuth scopes" was wrong and is not in here.**
  OpenAPI `security` is a list of *alternatives*; the legacy specs mostly
  declare none while the date-based specs enumerate every acceptable scope.
  Differencing those sets produces ~80 false "newly required scopes" per
  operation. Only scopes that stopped being accepted are reported.
- **A newly required *response* field is not a breaking change.** The server
  promising more is not the same as the server demanding more. Direction is
  tracked separately.
- Everything here is derived from HubSpot's published specs. Where a spec is
  wrong or stale, this is too. It is not a substitute for HubSpot's own
  documentation when that lands in March 2027 — it is what there is until then.

## Staying current

HubSpot ships new date-based versions on a rolling basis and the March 2027 docs
will move things again. **DBV Watch** re-runs this diff weekly against your
endpoint inventory and emails you when something you actually call changes,
loses its counterpart, or gains a breaking field difference —
[$29/month](https://buy.stripe.com/bJe8wPahac6AeayerNdby08). The map and the
scanner in this repo stay free either way.

## Licence

MIT for the code. The map is derived from HubSpot's public specifications; it is
not affiliated with or endorsed by HubSpot.
