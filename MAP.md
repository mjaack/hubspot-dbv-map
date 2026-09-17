# HubSpot legacy → date-based versioning: the per-endpoint map

Generated from HubSpot's own public OpenAPI catalogue (`https://api.hubspot.com/public/api/spec/v1/specs`).

- **1040** legacy operations across **98** APIs
- **44** have no date-based counterpart at all
- **95** have at least one difference that breaks a caller
- **18** sit in APIs with no date-based version published yet

| | |
|---|---|
| v1–v3 unsupported | 2027-09 |
| v4 unsupported | 2027-03-30 |
| legacy private app creation ends (new accounts) | 2026-09-28 |
| legacy private app creation ends (existing accounts) | 2026-10-26 |

## 1. No date-based counterpart

These calls cannot be version-bumped. They have to be rewritten against a different endpoint or dropped.

| API | Method | Legacy path | What it did |
|---|---|---|---|
| Appointments | PUT | `/crm/objects/v3/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Create an association between two CRM objects. |
| Appointments | DELETE | `/crm/objects/v3/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Remove an association between two CRM objects. |
| Associations Schema | GET | `/crm/v3/associations/{fromObjectType}/{toObjectType}/types` | — |
| At Debug | PUT | `/crm/v3/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Associate an object with another object |
| At Debug | DELETE | `/crm/v3/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Remove an association between two objects |
| Business Units | GET | `/business-units/v3/business-units/user/{userId}` | Retrieve brands by associated user |
| Calling Extensions | GET | `/crm/extensions/calling/v3/connection-statuses` | — |
| Calling Extensions | POST | `/crm/extensions/calling/v3/connection-statuses/batch/read` | — |
| Calling Extensions | GET | `/crm/extensions/calling/v3/connection-statuses/me` | — |
| Deal Splits | POST | `/crm/objects/v3/deals/splits/batch/read` | Read a batch of deal split objects by their associated deal object internal ID |
| Deal Splits | POST | `/crm/objects/v3/deals/splits/batch/upsert` | Create or replace deal splits for deals with the provided IDs. Deal split percentages for each deal must sum up to 1.0 (100%) and may have up to 8 decimal places |
| Events | GET | `/events/v3/events` | — |
| Events | GET | `/events/v3/events/event-types` | — |
| Meetings | PATCH | `/scheduler/v3/meetings/meeting-links/{meetingLinkSlug}` | — |
| Oauth | GET | `/oauth/v1/access-tokens/{token}` | — |
| Oauth | GET | `/oauth/v1/refresh-tokens/{token}` | — |
| Oauth | DELETE | `/oauth/v1/refresh-tokens/{token}` | — |
| Pages | GET | `/cms/pages/v3/landing-pages/cursor` | — |
| Pages | GET | `/cms/pages/v3/landing-pages/cursor/query` | — |
| Pages | GET | `/cms/pages/v3/landing-pages/folders/cursor` | — |
| Pages | GET | `/cms/pages/v3/landing-pages/folders/cursor/query` | — |
| Pages | GET | `/cms/pages/v3/site-pages/cursor` | — |
| Pages | GET | `/cms/pages/v3/site-pages/cursor/query` | — |
| Partner Clients | PUT | `/crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Associate a partner client with another object |
| Partner Clients | DELETE | `/crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Remove an association between two partner clients |
| Partner Services | PUT | `/crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Associate a partner service with another object |
| Partner Services | DELETE | `/crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}/{toObjectId}/{associationType}` | Remove an association between two partner services |
| Single-send | POST | `/marketing/v4/email/single-send` | Send an email |
| Subscriptions | GET | `/communication-preferences/v3/status/email/{emailAddress}` | — |
| Subscriptions | POST | `/communication-preferences/v3/subscribe` | — |
| Subscriptions | POST | `/communication-preferences/v3/unsubscribe` | — |
| Timeline | POST | `/integrators/timeline/v3/events/batch/create` | Create multiple events |
| Timeline | GET | `/integrators/timeline/v3/events/{eventTemplateId}/{eventId}` | Get an event instance |
| Timeline | GET | `/integrators/timeline/v3/{appId}/event-templates` | Get all event templates |
| Timeline | POST | `/integrators/timeline/v3/{appId}/event-templates` | Create an event template |
| Timeline | GET | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}` | Get an event template |
| Timeline | PUT | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}` | Update an event template |
| Timeline | DELETE | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}` | Delete an event template |
| Timeline | POST | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens` | Add tokens to an existing template |
| Timeline | PUT | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}` | Update a template token |
| Timeline | DELETE | `/integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}` | Delete a template token |
| Transcriptions | GET | `/crm/extensions/calling/v3/connection-statuses` | — |
| Transcriptions | POST | `/crm/extensions/calling/v3/connection-statuses/batch/read` | — |
| Transcriptions | GET | `/crm/extensions/calling/v3/connection-statuses/me` | — |

## 2. APIs with no date-based version yet

Nothing to migrate *to* as of the generation date. Watch these.

| API | Method | Legacy path |
|---|---|---|
| Automation V4 | GET | `/automation/v4/flows` |
| Automation V4 | POST | `/automation/v4/flows` |
| Automation V4 | POST | `/automation/v4/flows/batch/read` |
| Automation V4 | GET | `/automation/v4/flows/email-campaigns` |
| Automation V4 | GET | `/automation/v4/flows/performance/{flowId}` |
| Automation V4 | GET | `/automation/v4/flows/{flowId}` |
| Automation V4 | PUT | `/automation/v4/flows/{flowId}` |
| Automation V4 | DELETE | `/automation/v4/flows/{flowId}` |
| Automation V4 | POST | `/automation/v4/workflow-id-mappings/batch/read` |
| Forms | GET | `/marketing/v3/forms` |
| Forms | POST | `/marketing/v3/forms` |
| Forms | GET | `/marketing/v3/forms/{formId}` |
| Forms | PUT | `/marketing/v3/forms/{formId}` |
| Forms | DELETE | `/marketing/v3/forms/{formId}` |
| Forms | PATCH | `/marketing/v3/forms/{formId}` |
| Subscription Lifecycle | POST | `/payments-subscriptions/v1/subscriptions/crm/{objectId}/cancel` |
| Subscription Lifecycle | POST | `/payments-subscriptions/v1/subscriptions/crm/{objectId}/pause` |
| Subscription Lifecycle | POST | `/payments-subscriptions/v1/subscriptions/crm/{objectId}/unpause` |

## 3. Breaking differences

Same operation exists, but something a caller depends on changed.

### Appointments

**GET `/crm/objects/v3/{objectType}/{objectId}/associations/{toObjectType}`** → `/crm/objects/2026-09/{objectType}/{objectId}/associations/{toObjectType}` (2026-09)

- **removed** — param `query:includeFA` no longer exists
- **removed** — response field `results[].id` no longer exists
- **removed** — response field `results[].type` no longer exists

### Associations

**POST `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive`** → `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/archive` (2026-09)

- **type_changed** — type object -> array
- **removed** — request field `inputs[].type` no longer exists
- **added** — new required request field `inputs[].to[].id`

**POST `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create`** → `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/create` (2026-09)

- **removed** — request field `inputs[].type` no longer exists
- **added** — new required request field `inputs[].types[].associationCategory`
- **added** — new required request field `inputs[].types[].associationTypeId`
- **added** — new required request field `inputs[].types`
- **removed** — response field `results[].from` no longer exists
- **removed** — response field `results[].to` no longer exists
- **removed** — response field `results[].type` no longer exists

**POST `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read`** → `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/read` (2026-09)

- **removed** — response field `results[].to[].id` no longer exists
- **removed** — response field `results[].to[].type` no longer exists

### At Debug

**GET `/crm/v3/objects/{objectType}/{objectId}/associations/{toObjectType}`** → `/crm/objects/2026-03/{objectType}/{objectId}/associations/{toObjectType}` (2026-03)

- **removed** — param `query:includeFA` no longer exists
- **removed** — response field `results[].id` no longer exists
- **removed** — response field `results[].type` no longer exists

### Files

**POST `/files/v3/files/import-from-url/async`** → `/files/2026-09/files/import-from-url/async` (2026-09)

- **now_required** — request field `duplicateValidationScope` is now required
- **now_required** — request field `duplicateValidationStrategy` is now required
- **now_required** — request field `overwrite` is now required

**PATCH `/files/v3/files/{fileId}`** → `/files/2026-09/files/{fileId}` (2026-09)

- **now_required** — request field `clearExpires` is now required

**POST `/files/v3/folders/update/async`** → `/files/2026-03/folders/update/async` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**GET `/files/v3/folders/update/async/tasks/{taskId}/status`** → `/files/2026-03/folders/update/async/tasks/{taskId}/status` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

### Lists

**POST `/crm/v3/lists/search`** → `/crm/lists/2026-09/search` (2026-09)

- **now_required** — request field `listIds` is now required
- **now_required** — request field `processingTypes` is now required

### Manage Event Definitions

**POST `/events/v3/send/batch`** → `/events/2026-03/send/batch` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

### Oauth

**POST `/oauth/v1/token`** → `/oauth/2026-09/token` (2026-09)

- **removed** — param `query:client_secret` no longer exists
- **removed** — param `query:refresh_token` no longer exists

### Partner Clients

**GET `/crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}`** → `/crm/objects/2026-09/partner_clients/{partnerClientId}/associations/{toObjectType}` (2026-09)

- **removed** — param `query:includeFA` no longer exists
- **removed** — response field `results[].id` no longer exists
- **removed** — response field `results[].type` no longer exists

### Partner Services

**GET `/crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}`** → `/crm/objects/2026-09/partner_services/{partnerServiceId}/associations/{toObjectType}` (2026-09)

- **removed** — param `query:includeFA` no longer exists
- **removed** — response field `results[].id` no longer exists
- **removed** — response field `results[].type` no longer exists

### Properties

**POST `/crm/v3/properties/{objectType}`** → `/crm/properties/2026-09/{objectType}` (2026-09)

- **now_required** — request field `options[].displayOrder` is now required

**POST `/crm/v3/properties/{objectType}/batch/create`** → `/crm/properties/2026-09/{objectType}/batch/create` (2026-09)

- **now_required** — request field `inputs[].options[].displayOrder` is now required

**PATCH `/crm/v3/properties/{objectType}/{propertyName}`** → `/crm/properties/2026-09/{objectType}/{propertyName}` (2026-09)

- **now_required** — request field `options[].displayOrder` is now required

### Schemas

**POST `/crm-object-schemas/v3/schemas`** → `/crm-object-schemas/2026-09/schemas` (2026-09)

- **now_required** — request field `allowsSensitiveProperties` is now required
- **now_required** — request field `searchableProperties` is now required
- **now_required** — request field `secondaryDisplayProperties` is now required
- **now_required** — request field `shouldCreateSameObjectAssociation` is now required

**PATCH `/crm-object-schemas/v3/schemas/{objectType}`** → `/crm-object-schemas/2026-09/schemas/{objectType}` (2026-09)

- **now_required** — request field `clearDescription` is now required

### Subscriptions

**GET `/communication-preferences/v3/definitions`** → `/communication-preferences/2026-09/definitions` (2026-09)

- **removed** — response field `subscriptionDefinitions[].businessUnitId` no longer exists
- **removed** — response field `subscriptionDefinitions[].communicationMethod` no longer exists
- **removed** — response field `subscriptionDefinitions[].createdAt` no longer exists
- **removed** — response field `subscriptionDefinitions[].description` no longer exists
- **removed** — response field `subscriptionDefinitions[].id` no longer exists
- **removed** — response field `subscriptionDefinitions[].isActive` no longer exists
- **removed** — response field `subscriptionDefinitions[].isDefault` no longer exists
- **removed** — response field `subscriptionDefinitions[].isInternal` no longer exists
- **removed** — response field `subscriptionDefinitions[].name` no longer exists
- **removed** — response field `subscriptionDefinitions[].purpose` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].createdAt` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].description` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].languageCode` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].name` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].subscriptionId` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations[].updatedAt` no longer exists
- **removed** — response field `subscriptionDefinitions[].subscriptionTranslations` no longer exists
- **removed** — response field `subscriptionDefinitions[].updatedAt` no longer exists
- **removed** — response field `subscriptionDefinitions` no longer exists

### Timeline

**POST `/integrators/timeline/v3/events`** → `/integrators/timeline/2026-09/events` (2026-09)

- **removed** — request field `customObjectTypeId` no longer exists
- **removed** — request field `eventTemplateId` no longer exists
- **removed** — request field `tokens` no longer exists
- **added** — new required request field `eventTypeName`
- **added** — new required request field `properties`
- **removed** — response field `createdAt` no longer exists
- **removed** — response field `customObjectTypeId` no longer exists
- **removed** — response field `eventTemplateId` no longer exists
- **removed** — response field `objectType` no longer exists
- **removed** — response field `tokens` no longer exists

### Transactional Single Send

**POST `/marketing/v3/transactional/single-email/send`** → `/marketing/transactional/2026-09/single-email/send` (2026-09)

- **now_required** — request field `contactProperties` is now required
- **now_required** — request field `customProperties` is now required

### Url Redirects

**POST `/cms/url-redirects/v3/url-mappings`** → `/cms/url-redirects/2026-09/url-mappings` (2026-09)

- **now_required** — request field `created` is now required
- **now_required** — request field `updated` is now required

**PATCH `/cms/v3/url-redirects/{urlRedirectId}`** → `/cms/url-redirects/2026-09/{urlRedirectId}` (2026-09)

- **now_required** — request field `created` is now required
- **now_required** — request field `updated` is now required

### Webhooks

**GET `/webhooks/v3/{appId}/settings`** → `/webhooks/2026-03/{appId}/settings` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**PUT `/webhooks/v3/{appId}/settings`** → `/webhooks/2026-03/{appId}/settings` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**DELETE `/webhooks/v3/{appId}/settings`** → `/webhooks/2026-03/{appId}/settings` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**GET `/webhooks/v3/{appId}/subscriptions`** → `/webhooks/2026-03/{appId}/subscriptions` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**POST `/webhooks/v3/{appId}/subscriptions`** → `/webhooks/2026-03/{appId}/subscriptions` (2026-03)

- **now_required** — request field `active` is now required
- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**POST `/webhooks/v3/{appId}/subscriptions/batch/update`** → `/webhooks/2026-03/{appId}/subscriptions/batch/update` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**GET `/webhooks/v3/{appId}/subscriptions/{subscriptionId}`** → `/webhooks/2026-03/{appId}/subscriptions/{subscriptionId}` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**DELETE `/webhooks/v3/{appId}/subscriptions/{subscriptionId}`** → `/webhooks/2026-03/{appId}/subscriptions/{subscriptionId}` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

**PATCH `/webhooks/v3/{appId}/subscriptions/{subscriptionId}`** → `/webhooks/2026-03/{appId}/subscriptions/{subscriptionId}` (2026-03)

- **dropped_after_version** — present in 2026-03 but gone from the latest version (2026-09): pin 2026-03 or rewrite before it lapses too

## 4. Everything else

Operations that map cleanly. The path shape still changes — the version segment moves — so this is not a no-op, but nothing a caller reads or sends is affected.

| API | Method | Legacy | Date-based | Status |
|---|---|---|---|---|
| Account Info | GET | `/account-info/v3/api-usage/daily/private-apps` | `/account-info/2026-09/api-usage/daily/private-apps` | IDENTICAL |
| Account Info | GET | `/account-info/v3/details` | `/account-info/2026-09/details` | CHANGED |
| Actions V4 | POST | `/automation/v4/actions/callbacks/complete` | `/automation/actions/callbacks/2026-09/complete` | CHANGED |
| Actions V4 | POST | `/automation/v4/actions/callbacks/{callbackId}/complete` | `/automation/actions/callbacks/2026-09/{callbackId}/complete` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}` | `/automation/actions/2026-09/{appId}` | CHANGED |
| Actions V4 | POST | `/automation/v4/actions/{appId}` | `/automation/actions/2026-09/{appId}` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}` | `/automation/actions/2026-09/{appId}/{definitionId}` | CHANGED |
| Actions V4 | DELETE | `/automation/v4/actions/{appId}/{definitionId}` | `/automation/actions/2026-09/{appId}/{definitionId}` | CHANGED |
| Actions V4 | PATCH | `/automation/v4/actions/{appId}/{definitionId}` | `/automation/actions/2026-09/{appId}/{definitionId}` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/functions` | `/automation/actions/2026-09/{appId}/{definitionId}/functions` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}` | CHANGED |
| Actions V4 | PUT | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}` | CHANGED |
| Actions V4 | DELETE | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}` | CHANGED |
| Actions V4 | PUT | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}` | CHANGED |
| Actions V4 | DELETE | `/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}` | `/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/requires-object` | `/automation/actions/2026-09/{appId}/{definitionId}/requires-object` | CHANGED |
| Actions V4 | POST | `/automation/v4/actions/{appId}/{definitionId}/requires-object` | `/automation/actions/2026-09/{appId}/{definitionId}/requires-object` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/revisions` | `/automation/actions/2026-09/{appId}/{definitionId}/revisions` | CHANGED |
| Actions V4 | GET | `/automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}` | `/automation/actions/2026-09/{appId}/{definitionId}/revisions/{revisionId}` | CHANGED |
| App Uninstalls | DELETE | `/appinstalls/v3/external-install` | `/appinstalls/2026-09/external-install` | IDENTICAL |
| Appointments | GET | `/crm/objects/v3/{objectType}` | `/crm/objects/2026-09/{objectType}` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}` | `/crm/objects/2026-09/{objectType}` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/batch/archive` | `/crm/objects/2026-09/{objectType}/batch/archive` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/batch/create` | `/crm/objects/2026-09/{objectType}/batch/create` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/batch/read` | `/crm/objects/2026-09/{objectType}/batch/read` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/batch/update` | `/crm/objects/2026-09/{objectType}/batch/update` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/batch/upsert` | `/crm/objects/2026-09/{objectType}/batch/upsert` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/gdpr-delete` | `/crm/objects/2026-09/{objectType}/gdpr-delete` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/merge` | `/crm/objects/2026-09/{objectType}/merge` | IDENTICAL |
| Appointments | POST | `/crm/objects/v3/{objectType}/search` | `/crm/objects/2026-09/{objectType}/search` | IDENTICAL |
| Appointments | GET | `/crm/objects/v3/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | IDENTICAL |
| Appointments | DELETE | `/crm/objects/v3/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | IDENTICAL |
| Appointments | PATCH | `/crm/objects/v3/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | IDENTICAL |
| Associations | POST | `/crm/v4/associations/usage/high-usage-report/{userId}` | `/crm/associations/2026-09/usage/high-usage-report/{userId}` | CHANGED |
| Associations | POST | `/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/archive` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/archive` | CHANGED |
| Associations | POST | `/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/associate/default` | CHANGED |
| Associations | POST | `/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/create` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/create` | CHANGED |
| Associations | POST | `/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/labels/archive` | CHANGED |
| Associations | POST | `/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/read` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/batch/read` | CHANGED |
| Associations | PUT | `/crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}` | `/crm/objects/2026-09/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}` | CHANGED |
| Associations | GET | `/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}` | `/crm/objects/2026-09/{objectType}/{objectId}/associations/{toObjectType}` | CHANGED |
| Associations | PUT | `/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}` | `/crm/objects/2026-09/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}` | CHANGED |
| Associations | DELETE | `/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}` | `/crm/objects/2026-09/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}` | CHANGED |
| Associations Schema | GET | `/crm/associations/v4/definitions/configurations/all` | `/crm/associations/2026-09/definitions/configurations/all` | IDENTICAL |
| Associations Schema | GET | `/crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}` | `/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}` | IDENTICAL |
| Associations Schema | POST | `/crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create` | `/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create` | IDENTICAL |
| Associations Schema | POST | `/crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge` | `/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge` | CHANGED |
| Associations Schema | POST | `/crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update` | `/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update` | IDENTICAL |
| Associations Schema | GET | `/crm/associations/v4/{fromObjectType}/{toObjectType}/labels` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels` | IDENTICAL |
| Associations Schema | PUT | `/crm/associations/v4/{fromObjectType}/{toObjectType}/labels` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels` | IDENTICAL |
| Associations Schema | POST | `/crm/associations/v4/{fromObjectType}/{toObjectType}/labels` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels` | IDENTICAL |
| Associations Schema | DELETE | `/crm/associations/v4/{fromObjectType}/{toObjectType}/labels/{associationTypeId}` | `/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels/{associationTypeId}` | IDENTICAL |
| At Debug | GET | `/crm/v3/objects/{objectType}` | `/crm/objects/2026-03/{objectType}` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}` | `/crm/objects/2026-03/{objectType}` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/batch/archive` | `/crm/objects/2026-03/{objectType}/batch/archive` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/batch/create` | `/crm/objects/2026-03/{objectType}/batch/create` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/batch/read` | `/crm/objects/2026-03/{objectType}/batch/read` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/batch/update` | `/crm/objects/2026-03/{objectType}/batch/update` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/batch/upsert` | `/crm/objects/2026-03/{objectType}/batch/upsert` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/gdpr-delete` | `/crm/objects/2026-03/{objectType}/gdpr-delete` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/merge` | `/crm/objects/2026-03/{objectType}/merge` | CHANGED |
| At Debug | POST | `/crm/v3/objects/{objectType}/search` | `/crm/objects/2026-03/{objectType}/search` | CHANGED |
| At Debug | GET | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-03/{objectType}/{objectId}` | CHANGED |
| At Debug | DELETE | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-03/{objectType}/{objectId}` | CHANGED |
| At Debug | PATCH | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-03/{objectType}/{objectId}` | CHANGED |
| Audit Logs | GET | `/account-info/v3/activity/audit-logs` | `/account-info/2026-09/activity/audit-logs` | IDENTICAL |
| Audit Logs | GET | `/account-info/v3/activity/login` | `/account-info/2026-09/activity/login` | IDENTICAL |
| Audit Logs | GET | `/account-info/v3/activity/security` | `/account-info/2026-09/activity/security` | IDENTICAL |
| Authors | GET | `/cms/v3/blogs/authors` | `/cms/blogs/2026-09/authors` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors` | `/cms/blogs/2026-09/authors` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/batch/archive` | `/cms/blogs/2026-09/authors/batch/archive` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/batch/create` | `/cms/blogs/2026-09/authors/batch/create` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/batch/read` | `/cms/blogs/2026-09/authors/batch/read` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/batch/update` | `/cms/blogs/2026-09/authors/batch/update` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/multi-language/attach-to-lang-group` | `/cms/blogs/2026-09/authors/multi-language/attach-to-lang-group` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/multi-language/create-language-variation` | `/cms/blogs/2026-09/authors/multi-language/create-language-variation` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/multi-language/detach-from-lang-group` | `/cms/blogs/2026-09/authors/multi-language/detach-from-lang-group` | CHANGED |
| Authors | PUT | `/cms/v3/blogs/authors/multi-language/set-new-lang-primary` | `/cms/blogs/2026-09/authors/multi-language/set-new-lang-primary` | CHANGED |
| Authors | POST | `/cms/v3/blogs/authors/multi-language/update-languages` | `/cms/blogs/2026-09/authors/multi-language/update-languages` | CHANGED |
| Authors | GET | `/cms/v3/blogs/authors/{objectId}` | `/cms/blogs/2026-09/authors/{objectId}` | CHANGED |
| Authors | DELETE | `/cms/v3/blogs/authors/{objectId}` | `/cms/blogs/2026-09/authors/{objectId}` | CHANGED |
| Authors | PATCH | `/cms/v3/blogs/authors/{objectId}` | `/cms/blogs/2026-09/authors/{objectId}` | CHANGED |
| Blog Settings | GET | `/cms/v3/blog-settings/settings` | `/cms/blog-settings/2026-09/settings` | CHANGED |
| Blog Settings | POST | `/cms/v3/blog-settings/settings/multi-language/attach-to-lang-group` | `/cms/blog-settings/2026-09/settings/multi-language/attach-to-lang-group` | CHANGED |
| Blog Settings | POST | `/cms/v3/blog-settings/settings/multi-language/create-language-variation` | `/cms/blog-settings/2026-09/settings/multi-language/create-language-variation` | CHANGED |
| Blog Settings | POST | `/cms/v3/blog-settings/settings/multi-language/detach-from-lang-group` | `/cms/blog-settings/2026-09/settings/multi-language/detach-from-lang-group` | CHANGED |
| Blog Settings | PUT | `/cms/v3/blog-settings/settings/multi-language/set-new-lang-primary` | `/cms/blog-settings/2026-09/settings/multi-language/set-new-lang-primary` | CHANGED |
| Blog Settings | POST | `/cms/v3/blog-settings/settings/multi-language/update-languages` | `/cms/blog-settings/2026-09/settings/multi-language/update-languages` | CHANGED |
| Blog Settings | GET | `/cms/v3/blog-settings/settings/{blogId}` | `/cms/blog-settings/2026-09/settings/{blogId}` | CHANGED |
| Blog Settings | GET | `/cms/v3/blog-settings/settings/{blogId}/revisions` | `/cms/blog-settings/2026-09/settings/{blogId}/revisions` | CHANGED |
| Blog Settings | GET | `/cms/v3/blog-settings/settings/{blogId}/revisions/{revisionId}` | `/cms/blog-settings/2026-09/settings/{blogId}/revisions/{revisionId}` | CHANGED |
| Calling Extensions | POST | `/crm/v3/extensions/calling/inbound-call` | `/crm/extensions/calling/2026-09/inbound-call` | CHANGED |
| Calling Extensions | POST | `/crm/v3/extensions/calling/recordings/ready` | `/crm/extensions/calling/2026-09/recordings/ready` | CHANGED |
| Calling Extensions | GET | `/crm/v3/extensions/calling/{appId}/settings` | `/crm/extensions/calling/2026-09/{appId}/settings` | CHANGED |
| Calling Extensions | POST | `/crm/v3/extensions/calling/{appId}/settings` | `/crm/extensions/calling/2026-09/{appId}/settings` | CHANGED |
| Calling Extensions | DELETE | `/crm/v3/extensions/calling/{appId}/settings` | `/crm/extensions/calling/2026-09/{appId}/settings` | CHANGED |
| Calling Extensions | PATCH | `/crm/v3/extensions/calling/{appId}/settings` | `/crm/extensions/calling/2026-09/{appId}/settings` | CHANGED |
| Calling Extensions | GET | `/crm/v3/extensions/calling/{appId}/settings/channel-connection` | `/crm/extensions/calling/2026-09/{appId}/settings/channel-connection` | CHANGED |
| Calling Extensions | POST | `/crm/v3/extensions/calling/{appId}/settings/channel-connection` | `/crm/extensions/calling/2026-09/{appId}/settings/channel-connection` | CHANGED |
| Calling Extensions | DELETE | `/crm/v3/extensions/calling/{appId}/settings/channel-connection` | `/crm/extensions/calling/2026-09/{appId}/settings/channel-connection` | CHANGED |
| Calling Extensions | PATCH | `/crm/v3/extensions/calling/{appId}/settings/channel-connection` | `/crm/extensions/calling/2026-09/{appId}/settings/channel-connection` | CHANGED |
| Calling Extensions | GET | `/crm/v3/extensions/calling/{appId}/settings/recording` | `/crm/extensions/calling/2026-09/{appId}/settings/recording` | CHANGED |
| Calling Extensions | POST | `/crm/v3/extensions/calling/{appId}/settings/recording` | `/crm/extensions/calling/2026-09/{appId}/settings/recording` | CHANGED |
| Calling Extensions | PATCH | `/crm/v3/extensions/calling/{appId}/settings/recording` | `/crm/extensions/calling/2026-09/{appId}/settings/recording` | CHANGED |
| Calls | GET | `/crm/v3/objects/calls` | `/crm/objects/2026-09/calls` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls` | `/crm/objects/2026-09/calls` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/batch/archive` | `/crm/objects/2026-09/calls/batch/archive` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/batch/create` | `/crm/objects/2026-09/calls/batch/create` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/batch/read` | `/crm/objects/2026-09/calls/batch/read` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/batch/update` | `/crm/objects/2026-09/calls/batch/update` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/batch/upsert` | `/crm/objects/2026-09/calls/batch/upsert` | CHANGED |
| Calls | POST | `/crm/v3/objects/calls/search` | `/crm/objects/2026-09/calls/search` | CHANGED |
| Calls | GET | `/crm/v3/objects/calls/{callId}` | `/crm/objects/2026-09/calls/{callId}` | CHANGED |
| Calls | DELETE | `/crm/v3/objects/calls/{callId}` | `/crm/objects/2026-09/calls/{callId}` | CHANGED |
| Calls | PATCH | `/crm/v3/objects/calls/{callId}` | `/crm/objects/2026-09/calls/{callId}` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns` | `/marketing/campaigns/2026-09` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns` | `/marketing/campaigns/2026-09` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/batch/archive` | `/marketing/campaigns/2026-09/batch/archive` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/batch/create` | `/marketing/campaigns/2026-09/batch/create` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/batch/read` | `/marketing/campaigns/2026-09/batch/read` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/batch/update` | `/marketing/campaigns/2026-09/batch/update` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}` | `/marketing/campaigns/2026-09/{campaignGuid}` | CHANGED |
| Campaigns Public Api | DELETE | `/marketing/v3/campaigns/{campaignGuid}` | `/marketing/campaigns/2026-09/{campaignGuid}` | CHANGED |
| Campaigns Public Api | PATCH | `/marketing/v3/campaigns/{campaignGuid}` | `/marketing/campaigns/2026-09/{campaignGuid}` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}` | `/marketing/campaigns/2026-09/{campaignGuid}/assets/{assetType}` | CHANGED |
| Campaigns Public Api | PUT | `/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}` | `/marketing/campaigns/2026-09/{campaignGuid}/assets/{assetType}/{assetId}` | CHANGED |
| Campaigns Public Api | DELETE | `/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}` | `/marketing/campaigns/2026-09/{campaignGuid}/assets/{assetType}/{assetId}` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/{campaignGuid}/budget` | `/marketing/campaigns/2026-09/{campaignGuid}/budget` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/budget/totals` | `/marketing/campaigns/2026-09/{campaignGuid}/budget/totals` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}` | `/marketing/campaigns/2026-09/{campaignGuid}/budget/{budgetId}` | CHANGED |
| Campaigns Public Api | PUT | `/marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}` | `/marketing/campaigns/2026-09/{campaignGuid}/budget/{budgetId}` | CHANGED |
| Campaigns Public Api | DELETE | `/marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}` | `/marketing/campaigns/2026-09/{campaignGuid}/budget/{budgetId}` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}` | `/marketing/campaigns/2026-09/{campaignGuid}/reports/contacts/{contactType}` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/reports/metrics` | `/marketing/campaigns/2026-09/{campaignGuid}/reports/metrics` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/reports/revenue` | `/marketing/campaigns/2026-09/{campaignGuid}/reports/revenue` | CHANGED |
| Campaigns Public Api | POST | `/marketing/v3/campaigns/{campaignGuid}/spend` | `/marketing/campaigns/2026-09/{campaignGuid}/spend` | CHANGED |
| Campaigns Public Api | GET | `/marketing/v3/campaigns/{campaignGuid}/spend/{spendId}` | `/marketing/campaigns/2026-09/{campaignGuid}/spend/{spendId}` | CHANGED |
| Campaigns Public Api | PUT | `/marketing/v3/campaigns/{campaignGuid}/spend/{spendId}` | `/marketing/campaigns/2026-09/{campaignGuid}/spend/{spendId}` | CHANGED |
| Campaigns Public Api | DELETE | `/marketing/v3/campaigns/{campaignGuid}/spend/{spendId}` | `/marketing/campaigns/2026-09/{campaignGuid}/spend/{spendId}` | CHANGED |
| Carts | GET | `/crm/v3/objects/carts` | `/crm/objects/2026-09/carts` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts` | `/crm/objects/2026-09/carts` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/batch/archive` | `/crm/objects/2026-09/carts/batch/archive` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/batch/create` | `/crm/objects/2026-09/carts/batch/create` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/batch/read` | `/crm/objects/2026-09/carts/batch/read` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/batch/update` | `/crm/objects/2026-09/carts/batch/update` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/batch/upsert` | `/crm/objects/2026-09/carts/batch/upsert` | CHANGED |
| Carts | POST | `/crm/v3/objects/carts/search` | `/crm/objects/2026-09/carts/search` | CHANGED |
| Carts | GET | `/crm/v3/objects/carts/{cartId}` | `/crm/objects/2026-09/carts/{cartId}` | CHANGED |
| Carts | DELETE | `/crm/v3/objects/carts/{cartId}` | `/crm/objects/2026-09/carts/{cartId}` | CHANGED |
| Carts | PATCH | `/crm/v3/objects/carts/{cartId}` | `/crm/objects/2026-09/carts/{cartId}` | CHANGED |
| Cms Content Audit | GET | `/cms/audit-logs/v3` | `/cms/audit-logs/2026-09` | IDENTICAL |
| Commerce Payments | GET | `/crm/v3/objects/commerce_payments` | `/crm/objects/2026-09/commerce_payments` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments` | `/crm/objects/2026-09/commerce_payments` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/batch/archive` | `/crm/objects/2026-09/commerce_payments/batch/archive` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/batch/create` | `/crm/objects/2026-09/commerce_payments/batch/create` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/batch/read` | `/crm/objects/2026-09/commerce_payments/batch/read` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/batch/update` | `/crm/objects/2026-09/commerce_payments/batch/update` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/batch/upsert` | `/crm/objects/2026-09/commerce_payments/batch/upsert` | CHANGED |
| Commerce Payments | POST | `/crm/v3/objects/commerce_payments/search` | `/crm/objects/2026-09/commerce_payments/search` | CHANGED |
| Commerce Payments | GET | `/crm/v3/objects/commerce_payments/{commercePaymentId}` | `/crm/objects/2026-09/commerce_payments/{commercePaymentId}` | CHANGED |
| Commerce Payments | DELETE | `/crm/v3/objects/commerce_payments/{commercePaymentId}` | `/crm/objects/2026-09/commerce_payments/{commercePaymentId}` | CHANGED |
| Commerce Payments | PATCH | `/crm/v3/objects/commerce_payments/{commercePaymentId}` | `/crm/objects/2026-09/commerce_payments/{commercePaymentId}` | CHANGED |
| Commerce Subscriptions | GET | `/crm/v3/objects/subscriptions` | `/crm/objects/2026-09/subscriptions` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions` | `/crm/objects/2026-09/subscriptions` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/batch/archive` | `/crm/objects/2026-09/subscriptions/batch/archive` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/batch/create` | `/crm/objects/2026-09/subscriptions/batch/create` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/batch/read` | `/crm/objects/2026-09/subscriptions/batch/read` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/batch/update` | `/crm/objects/2026-09/subscriptions/batch/update` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/batch/upsert` | `/crm/objects/2026-09/subscriptions/batch/upsert` | CHANGED |
| Commerce Subscriptions | POST | `/crm/v3/objects/subscriptions/search` | `/crm/objects/2026-09/subscriptions/search` | CHANGED |
| Commerce Subscriptions | GET | `/crm/v3/objects/subscriptions/{subscriptionId}` | `/crm/objects/2026-09/subscriptions/{subscriptionId}` | CHANGED |
| Commerce Subscriptions | DELETE | `/crm/v3/objects/subscriptions/{subscriptionId}` | `/crm/objects/2026-09/subscriptions/{subscriptionId}` | CHANGED |
| Commerce Subscriptions | PATCH | `/crm/v3/objects/subscriptions/{subscriptionId}` | `/crm/objects/2026-09/subscriptions/{subscriptionId}` | CHANGED |
| Communications | GET | `/crm/v3/objects/communications` | `/crm/objects/2026-09/communications` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications` | `/crm/objects/2026-09/communications` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/batch/archive` | `/crm/objects/2026-09/communications/batch/archive` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/batch/create` | `/crm/objects/2026-09/communications/batch/create` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/batch/read` | `/crm/objects/2026-09/communications/batch/read` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/batch/update` | `/crm/objects/2026-09/communications/batch/update` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/batch/upsert` | `/crm/objects/2026-09/communications/batch/upsert` | CHANGED |
| Communications | POST | `/crm/v3/objects/communications/search` | `/crm/objects/2026-09/communications/search` | CHANGED |
| Communications | GET | `/crm/v3/objects/communications/{communicationId}` | `/crm/objects/2026-09/communications/{communicationId}` | CHANGED |
| Communications | DELETE | `/crm/v3/objects/communications/{communicationId}` | `/crm/objects/2026-09/communications/{communicationId}` | CHANGED |
| Communications | PATCH | `/crm/v3/objects/communications/{communicationId}` | `/crm/objects/2026-09/communications/{communicationId}` | CHANGED |
| Companies | GET | `/crm/v3/objects/companies` | `/crm/objects/2026-09/companies` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies` | `/crm/objects/2026-09/companies` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/batch/archive` | `/crm/objects/2026-09/companies/batch/archive` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/batch/create` | `/crm/objects/2026-09/companies/batch/create` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/batch/read` | `/crm/objects/2026-09/companies/batch/read` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/batch/update` | `/crm/objects/2026-09/companies/batch/update` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/batch/upsert` | `/crm/objects/2026-09/companies/batch/upsert` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/merge` | `/crm/objects/2026-09/companies/merge` | CHANGED |
| Companies | POST | `/crm/v3/objects/companies/search` | `/crm/objects/2026-09/companies/search` | CHANGED |
| Companies | GET | `/crm/v3/objects/companies/{companyId}` | `/crm/objects/2026-09/companies/{companyId}` | CHANGED |
| Companies | DELETE | `/crm/v3/objects/companies/{companyId}` | `/crm/objects/2026-09/companies/{companyId}` | CHANGED |
| Companies | PATCH | `/crm/v3/objects/companies/{companyId}` | `/crm/objects/2026-09/companies/{companyId}` | CHANGED |
| Contacts | GET | `/crm/v3/objects/contacts` | `/crm/objects/2026-09/contacts` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts` | `/crm/objects/2026-09/contacts` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/batch/archive` | `/crm/objects/2026-09/contacts/batch/archive` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/batch/create` | `/crm/objects/2026-09/contacts/batch/create` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/batch/read` | `/crm/objects/2026-09/contacts/batch/read` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/batch/update` | `/crm/objects/2026-09/contacts/batch/update` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/batch/upsert` | `/crm/objects/2026-09/contacts/batch/upsert` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/gdpr-delete` | `/crm/objects/2026-09/contacts/gdpr-delete` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/merge` | `/crm/objects/2026-09/contacts/merge` | CHANGED |
| Contacts | POST | `/crm/v3/objects/contacts/search` | `/crm/objects/2026-09/contacts/search` | CHANGED |
| Contacts | GET | `/crm/v3/objects/contacts/{contactId}` | `/crm/objects/2026-09/contacts/{contactId}` | CHANGED |
| Contacts | DELETE | `/crm/v3/objects/contacts/{contactId}` | `/crm/objects/2026-09/contacts/{contactId}` | CHANGED |
| Contacts | PATCH | `/crm/v3/objects/contacts/{contactId}` | `/crm/objects/2026-09/contacts/{contactId}` | CHANGED |
| Contracts | GET | `/crm/v3/objects/contracts` | `/crm/objects/2026-09/contracts` | CHANGED |
| Contracts | POST | `/crm/v3/objects/contracts/batch/read` | `/crm/objects/2026-09/contracts/batch/read` | CHANGED |
| Contracts | GET | `/crm/v3/objects/contracts/{contractId}` | `/crm/objects/2026-09/contracts/{contractId}` | CHANGED |
| Conversations | PUT | `/conversations/conversations/v3/threads/{threadId}/assignee` | `/conversations/conversations/2026-09/threads/{threadId}/assignee` | IDENTICAL |
| Conversations | DELETE | `/conversations/conversations/v3/threads/{threadId}/assignee` | `/conversations/conversations/2026-09/threads/{threadId}/assignee` | IDENTICAL |
| Conversations | POST | `/conversations/v3/conversations/actors/batch/read` | `/conversations/conversations/2026-09/actors/batch/read` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/actors/{actorId}` | `/conversations/conversations/2026-09/actors/{actorId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/channel-accounts` | `/conversations/conversations/2026-09/channel-accounts` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/channel-accounts/{channelAccountId}` | `/conversations/conversations/2026-09/channel-accounts/{channelAccountId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/channels` | `/conversations/conversations/2026-09/channels` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/channels/{channelId}` | `/conversations/conversations/2026-09/channels/{channelId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/inboxes` | `/conversations/conversations/2026-09/inboxes` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/inboxes/{inboxId}` | `/conversations/conversations/2026-09/inboxes/{inboxId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/threads` | `/conversations/conversations/2026-09/threads` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/threads/{threadId}` | `/conversations/conversations/2026-09/threads/{threadId}` | CHANGED |
| Conversations | DELETE | `/conversations/v3/conversations/threads/{threadId}` | `/conversations/conversations/2026-09/threads/{threadId}` | CHANGED |
| Conversations | PATCH | `/conversations/v3/conversations/threads/{threadId}` | `/conversations/conversations/2026-09/threads/{threadId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/threads/{threadId}/messages` | `/conversations/conversations/2026-09/threads/{threadId}/messages` | CHANGED |
| Conversations | POST | `/conversations/v3/conversations/threads/{threadId}/messages` | `/conversations/conversations/2026-09/threads/{threadId}/messages` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/threads/{threadId}/messages/{messageId}` | `/conversations/conversations/2026-09/threads/{threadId}/messages/{messageId}` | CHANGED |
| Conversations | GET | `/conversations/v3/conversations/threads/{threadId}/messages/{messageId}/original-content` | `/conversations/conversations/2026-09/threads/{threadId}/messages/{messageId}/original-content` | CHANGED |
| Courses | GET | `/crm/v3/objects/0-410` | `/crm/objects/2026-09/0-410` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410` | `/crm/objects/2026-09/0-410` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/batch/archive` | `/crm/objects/2026-09/0-410/batch/archive` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/batch/create` | `/crm/objects/2026-09/0-410/batch/create` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/batch/read` | `/crm/objects/2026-09/0-410/batch/read` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/batch/update` | `/crm/objects/2026-09/0-410/batch/update` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/batch/upsert` | `/crm/objects/2026-09/0-410/batch/upsert` | CHANGED |
| Courses | POST | `/crm/v3/objects/0-410/search` | `/crm/objects/2026-09/0-410/search` | CHANGED |
| Courses | GET | `/crm/v3/objects/0-410/{courseId}` | `/crm/objects/2026-09/0-410/{courseId}` | CHANGED |
| Courses | DELETE | `/crm/v3/objects/0-410/{courseId}` | `/crm/objects/2026-09/0-410/{courseId}` | CHANGED |
| Courses | PATCH | `/crm/v3/objects/0-410/{courseId}` | `/crm/objects/2026-09/0-410/{courseId}` | CHANGED |
| Crm Owners | GET | `/crm/v3/owners` | `/crm/owners/2026-09` | CHANGED |
| Crm Owners | GET | `/crm/v3/owners/{ownerId}` | `/crm/owners/2026-09/{ownerId}` | CHANGED |
| Custom Channels | GET | `/conversations/custom-channels/v3` | `/conversations/custom-channels/2026-09` | IDENTICAL |
| Custom Channels | POST | `/conversations/custom-channels/v3` | `/conversations/custom-channels/2026-09` | IDENTICAL |
| Custom Channels | GET | `/conversations/v3/custom-channels/{channelId}` | `/conversations/custom-channels/2026-09/{channelId}` | CHANGED |
| Custom Channels | DELETE | `/conversations/v3/custom-channels/{channelId}` | `/conversations/custom-channels/2026-09/{channelId}` | CHANGED |
| Custom Channels | PATCH | `/conversations/v3/custom-channels/{channelId}` | `/conversations/custom-channels/2026-09/{channelId}` | CHANGED |
| Custom Channels | PATCH | `/conversations/v3/custom-channels/{channelId}/channel-account-staging-tokens/{accountToken}` | `/conversations/custom-channels/2026-09/{channelId}/channel-account-staging-tokens/{accountToken}` | CHANGED |
| Custom Channels | GET | `/conversations/v3/custom-channels/{channelId}/channel-accounts` | `/conversations/custom-channels/2026-09/{channelId}/channel-accounts` | CHANGED |
| Custom Channels | POST | `/conversations/v3/custom-channels/{channelId}/channel-accounts` | `/conversations/custom-channels/2026-09/{channelId}/channel-accounts` | CHANGED |
| Custom Channels | GET | `/conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}` | `/conversations/custom-channels/2026-09/{channelId}/channel-accounts/{channelAccountId}` | CHANGED |
| Custom Channels | PATCH | `/conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}` | `/conversations/custom-channels/2026-09/{channelId}/channel-accounts/{channelAccountId}` | CHANGED |
| Custom Channels | POST | `/conversations/v3/custom-channels/{channelId}/messages` | `/conversations/custom-channels/2026-09/{channelId}/messages` | CHANGED |
| Custom Channels | GET | `/conversations/v3/custom-channels/{channelId}/messages/{messageId}` | `/conversations/custom-channels/2026-09/{channelId}/messages/{messageId}` | CHANGED |
| Custom Channels | PATCH | `/conversations/v3/custom-channels/{channelId}/messages/{messageId}` | `/conversations/custom-channels/2026-09/{channelId}/messages/{messageId}` | CHANGED |
| Custom Objects | GET | `/crm/v3/objects/{objectType}` | `/crm/objects/2026-09/{objectType}` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}` | `/crm/objects/2026-09/{objectType}` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/batch/archive` | `/crm/objects/2026-09/{objectType}/batch/archive` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/batch/create` | `/crm/objects/2026-09/{objectType}/batch/create` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/batch/read` | `/crm/objects/2026-09/{objectType}/batch/read` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/batch/update` | `/crm/objects/2026-09/{objectType}/batch/update` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/batch/upsert` | `/crm/objects/2026-09/{objectType}/batch/upsert` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/merge` | `/crm/objects/2026-09/{objectType}/merge` | CHANGED |
| Custom Objects | POST | `/crm/v3/objects/{objectType}/search` | `/crm/objects/2026-09/{objectType}/search` | CHANGED |
| Custom Objects | GET | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | CHANGED |
| Custom Objects | DELETE | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | CHANGED |
| Custom Objects | PATCH | `/crm/v3/objects/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | CHANGED |
| Deals | GET | `/crm/v3/objects/0-3` | `/crm/objects/2026-09/0-3` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3` | `/crm/objects/2026-09/0-3` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/batch/archive` | `/crm/objects/2026-09/0-3/batch/archive` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/batch/create` | `/crm/objects/2026-09/0-3/batch/create` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/batch/read` | `/crm/objects/2026-09/0-3/batch/read` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/batch/update` | `/crm/objects/2026-09/0-3/batch/update` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/batch/upsert` | `/crm/objects/2026-09/0-3/batch/upsert` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/merge` | `/crm/objects/2026-09/0-3/merge` | CHANGED |
| Deals | POST | `/crm/v3/objects/0-3/search` | `/crm/objects/2026-09/0-3/search` | CHANGED |
| Deals | GET | `/crm/v3/objects/0-3/{dealId}` | `/crm/objects/2026-09/0-3/{dealId}` | CHANGED |
| Deals | DELETE | `/crm/v3/objects/0-3/{dealId}` | `/crm/objects/2026-09/0-3/{dealId}` | CHANGED |
| Deals | PATCH | `/crm/v3/objects/0-3/{dealId}` | `/crm/objects/2026-09/0-3/{dealId}` | CHANGED |
| Discounts | GET | `/crm/v3/objects/discounts` | `/crm/objects/2026-09/discounts` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts` | `/crm/objects/2026-09/discounts` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/batch/archive` | `/crm/objects/2026-09/discounts/batch/archive` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/batch/create` | `/crm/objects/2026-09/discounts/batch/create` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/batch/read` | `/crm/objects/2026-09/discounts/batch/read` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/batch/update` | `/crm/objects/2026-09/discounts/batch/update` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/batch/upsert` | `/crm/objects/2026-09/discounts/batch/upsert` | CHANGED |
| Discounts | POST | `/crm/v3/objects/discounts/search` | `/crm/objects/2026-09/discounts/search` | CHANGED |
| Discounts | GET | `/crm/v3/objects/discounts/{discountId}` | `/crm/objects/2026-09/discounts/{discountId}` | CHANGED |
| Discounts | DELETE | `/crm/v3/objects/discounts/{discountId}` | `/crm/objects/2026-09/discounts/{discountId}` | CHANGED |
| Discounts | PATCH | `/crm/v3/objects/discounts/{discountId}` | `/crm/objects/2026-09/discounts/{discountId}` | CHANGED |
| Domains | GET | `/cms/v3/domains` | `/cms/domains/2026-09` | CHANGED |
| Domains | GET | `/cms/v3/domains/{domainId}` | `/cms/domains/2026-09/{domainId}` | CHANGED |
| Emails | GET | `/crm/v3/objects/emails` | `/crm/objects/2026-09/emails` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails` | `/crm/objects/2026-09/emails` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/batch/archive` | `/crm/objects/2026-09/emails/batch/archive` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/batch/create` | `/crm/objects/2026-09/emails/batch/create` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/batch/read` | `/crm/objects/2026-09/emails/batch/read` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/batch/update` | `/crm/objects/2026-09/emails/batch/update` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/batch/upsert` | `/crm/objects/2026-09/emails/batch/upsert` | CHANGED |
| Emails | POST | `/crm/v3/objects/emails/search` | `/crm/objects/2026-09/emails/search` | CHANGED |
| Emails | GET | `/crm/v3/objects/emails/{emailId}` | `/crm/objects/2026-09/emails/{emailId}` | CHANGED |
| Emails | DELETE | `/crm/v3/objects/emails/{emailId}` | `/crm/objects/2026-09/emails/{emailId}` | CHANGED |
| Emails | PATCH | `/crm/v3/objects/emails/{emailId}` | `/crm/objects/2026-09/emails/{emailId}` | CHANGED |
| Exports | POST | `/crm/v3/exports/export/async` | `/crm/exports/2026-09/export/async` | CHANGED |
| Exports | GET | `/crm/v3/exports/export/async/tasks/{taskId}/status` | `/crm/exports/2026-09/export/async/tasks/{taskId}/status` | CHANGED |
| Exports | GET | `/crm/v3/exports/export/{exportId}` | `/crm/exports/2026-09/export/{exportId}` | CHANGED |
| Feedback Submissions | GET | `/crm/v3/objects/feedback_submissions` | `/crm/objects/2026-09/feedback_submissions` | CHANGED |
| Feedback Submissions | POST | `/crm/v3/objects/feedback_submissions/batch/read` | `/crm/objects/2026-09/feedback_submissions/batch/read` | CHANGED |
| Feedback Submissions | POST | `/crm/v3/objects/feedback_submissions/search` | `/crm/objects/2026-09/feedback_submissions/search` | CHANGED |
| Feedback Submissions | GET | `/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}` | `/crm/objects/2026-09/feedback_submissions/{feedbackSubmissionId}` | CHANGED |
| Fees | GET | `/crm/v3/objects/fees` | `/crm/objects/2026-09/fees` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees` | `/crm/objects/2026-09/fees` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/batch/archive` | `/crm/objects/2026-09/fees/batch/archive` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/batch/create` | `/crm/objects/2026-09/fees/batch/create` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/batch/read` | `/crm/objects/2026-09/fees/batch/read` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/batch/update` | `/crm/objects/2026-09/fees/batch/update` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/batch/upsert` | `/crm/objects/2026-09/fees/batch/upsert` | CHANGED |
| Fees | POST | `/crm/v3/objects/fees/search` | `/crm/objects/2026-09/fees/search` | CHANGED |
| Fees | GET | `/crm/v3/objects/fees/{feeId}` | `/crm/objects/2026-09/fees/{feeId}` | CHANGED |
| Fees | DELETE | `/crm/v3/objects/fees/{feeId}` | `/crm/objects/2026-09/fees/{feeId}` | CHANGED |
| Fees | PATCH | `/crm/v3/objects/fees/{feeId}` | `/crm/objects/2026-09/fees/{feeId}` | CHANGED |
| Files | POST | `/files/v3/files` | `/files/2026-09/files` | IDENTICAL |
| Files | GET | `/files/v3/files/import-from-url/async/tasks/{taskId}/status` | `/files/2026-09/files/import-from-url/async/tasks/{taskId}/status` | IDENTICAL |
| Files | GET | `/files/v3/files/search` | `/files/2026-09/files/search` | IDENTICAL |
| Files | GET | `/files/v3/files/stat/{path}` | `/files/2026-09/files/stat/{path}` | IDENTICAL |
| Files | GET | `/files/v3/files/{fileId}` | `/files/2026-09/files/{fileId}` | IDENTICAL |
| Files | PUT | `/files/v3/files/{fileId}` | `/files/2026-09/files/{fileId}` | IDENTICAL |
| Files | DELETE | `/files/v3/files/{fileId}` | `/files/2026-09/files/{fileId}` | IDENTICAL |
| Files | GET | `/files/v3/files/{fileId}/download` | `/files/2026-09/files/{fileId}/download` | IDENTICAL |
| Files | DELETE | `/files/v3/files/{fileId}/gdpr-delete` | `/files/2026-09/files/{fileId}/gdpr-delete` | IDENTICAL |
| Files | GET | `/files/v3/files/{fileId}/signed-url` | `/files/2026-09/files/{fileId}/signed-url` | IDENTICAL |
| Files | POST | `/files/v3/folders` | `/files/2026-09/folders` | IDENTICAL |
| Files | GET | `/files/v3/folders/search` | `/files/2026-09/folders/search` | IDENTICAL |
| Files | GET | `/files/v3/folders/{folderId}` | `/files/2026-09/folders/{folderId}` | IDENTICAL |
| Files | DELETE | `/files/v3/folders/{folderId}` | `/files/2026-09/folders/{folderId}` | IDENTICAL |
| Files | PATCH | `/files/v3/folders/{folderId}` | `/files/2026-09/folders/{folderId}` | IDENTICAL |
| Files | GET | `/files/v3/folders/{folderPath}` | `/files/2026-09/folders/{folderPath}` | IDENTICAL |
| Files | DELETE | `/files/v3/folders/{folderPath}` | `/files/2026-09/folders/{folderPath}` | IDENTICAL |
| Forecast Types | GET | `/forecast-settings/v3/forecast-types` | `/forecast-settings/2026-09/forecast-types` | IDENTICAL |
| Forecast Types | GET | `/forecast-settings/v3/forecast-types/{forecastTypeId}` | `/forecast-settings/2026-09/forecast-types/{forecastTypeId}` | IDENTICAL |
| Forecasts | GET | `/crm/objects/v3/{objectType}` | `/crm/objects/2026-09/{objectType}` | IDENTICAL |
| Forecasts | GET | `/crm/objects/v3/{objectType}/{objectId}` | `/crm/objects/2026-09/{objectType}/{objectId}` | IDENTICAL |
| Goal Targets | GET | `/crm/v3/objects/goal_targets` | `/crm/objects/2026-09/goal_targets` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets` | `/crm/objects/2026-09/goal_targets` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/batch/archive` | `/crm/objects/2026-09/goal_targets/batch/archive` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/batch/create` | `/crm/objects/2026-09/goal_targets/batch/create` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/batch/read` | `/crm/objects/2026-09/goal_targets/batch/read` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/batch/update` | `/crm/objects/2026-09/goal_targets/batch/update` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/batch/upsert` | `/crm/objects/2026-09/goal_targets/batch/upsert` | CHANGED |
| Goal Targets | POST | `/crm/v3/objects/goal_targets/search` | `/crm/objects/2026-09/goal_targets/search` | CHANGED |
| Goal Targets | GET | `/crm/v3/objects/goal_targets/{goalTargetId}` | `/crm/objects/2026-09/goal_targets/{goalTargetId}` | CHANGED |
| Goal Targets | DELETE | `/crm/v3/objects/goal_targets/{goalTargetId}` | `/crm/objects/2026-09/goal_targets/{goalTargetId}` | CHANGED |
| Goal Targets | PATCH | `/crm/v3/objects/goal_targets/{goalTargetId}` | `/crm/objects/2026-09/goal_targets/{goalTargetId}` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables` | `/cms/hubdb/2026-09/tables` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables` | `/cms/hubdb/2026-09/tables` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/draft` | `/cms/hubdb/2026-09/tables/draft` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}` | `/cms/hubdb/2026-09/tables/{tableIdOrName}` | CHANGED |
| Hubdb | DELETE | `/cms/v3/hubdb/tables/{tableIdOrName}` | `/cms/hubdb/2026-09/tables/{tableIdOrName}` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft` | CHANGED |
| Hubdb | PATCH | `/cms/v3/hubdb/tables/{tableIdOrName}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/draft/clone` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft/clone` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/draft/export` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft/export` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/draft/import` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft/import` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/draft/publish` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft/publish` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/draft/reset` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/draft/reset` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/export` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/export` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/rows` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/batch/read` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/batch/read` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/clone` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/clone` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/create` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/create` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/purge` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/purge` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/read` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/read` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/replace` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/update` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/update` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}` | CHANGED |
| Hubdb | GET | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}/draft` | CHANGED |
| Hubdb | PUT | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}/draft` | CHANGED |
| Hubdb | DELETE | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}/draft` | CHANGED |
| Hubdb | PATCH | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}/draft` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft/clone` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/rows/{rowId}/draft/clone` | CHANGED |
| Hubdb | POST | `/cms/v3/hubdb/tables/{tableIdOrName}/unpublish` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/unpublish` | CHANGED |
| Hubdb | DELETE | `/cms/v3/hubdb/tables/{tableIdOrName}/versions/{versionId}` | `/cms/hubdb/2026-09/tables/{tableIdOrName}/versions/{versionId}` | CHANGED |
| Imports | GET | `/crm/v3/imports` | `/crm/imports/2026-09` | CHANGED |
| Imports | POST | `/crm/v3/imports` | `/crm/imports/2026-09` | CHANGED |
| Imports | GET | `/crm/v3/imports/{importId}` | `/crm/imports/2026-09/{importId}` | CHANGED |
| Imports | POST | `/crm/v3/imports/{importId}/cancel` | `/crm/imports/2026-09/{importId}/cancel` | CHANGED |
| Imports | GET | `/crm/v3/imports/{importId}/errors` | `/crm/imports/2026-09/{importId}/errors` | CHANGED |
| Invoices | GET | `/crm/v3/objects/invoices` | `/crm/objects/2026-09/invoices` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices` | `/crm/objects/2026-09/invoices` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/batch/archive` | `/crm/objects/2026-09/invoices/batch/archive` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/batch/create` | `/crm/objects/2026-09/invoices/batch/create` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/batch/read` | `/crm/objects/2026-09/invoices/batch/read` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/batch/update` | `/crm/objects/2026-09/invoices/batch/update` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/batch/upsert` | `/crm/objects/2026-09/invoices/batch/upsert` | CHANGED |
| Invoices | POST | `/crm/v3/objects/invoices/search` | `/crm/objects/2026-09/invoices/search` | CHANGED |
| Invoices | GET | `/crm/v3/objects/invoices/{invoiceId}` | `/crm/objects/2026-09/invoices/{invoiceId}` | CHANGED |
| Invoices | DELETE | `/crm/v3/objects/invoices/{invoiceId}` | `/crm/objects/2026-09/invoices/{invoiceId}` | CHANGED |
| Invoices | PATCH | `/crm/v3/objects/invoices/{invoiceId}` | `/crm/objects/2026-09/invoices/{invoiceId}` | CHANGED |
| Leads | GET | `/crm/v3/objects/leads` | `/crm/objects/2026-09/leads` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads` | `/crm/objects/2026-09/leads` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/batch/archive` | `/crm/objects/2026-09/leads/batch/archive` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/batch/create` | `/crm/objects/2026-09/leads/batch/create` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/batch/read` | `/crm/objects/2026-09/leads/batch/read` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/batch/update` | `/crm/objects/2026-09/leads/batch/update` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/batch/upsert` | `/crm/objects/2026-09/leads/batch/upsert` | CHANGED |
| Leads | POST | `/crm/v3/objects/leads/search` | `/crm/objects/2026-09/leads/search` | CHANGED |
| Leads | GET | `/crm/v3/objects/leads/{leadsId}` | `/crm/objects/2026-09/leads/{leadsId}` | CHANGED |
| Leads | DELETE | `/crm/v3/objects/leads/{leadsId}` | `/crm/objects/2026-09/leads/{leadsId}` | CHANGED |
| Leads | PATCH | `/crm/v3/objects/leads/{leadsId}` | `/crm/objects/2026-09/leads/{leadsId}` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/associations/labels` | `/crm/limits/2026-09/associations/labels` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/associations/records/from` | `/crm/limits/2026-09/associations/records/from` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/associations/records/{fromObjectTypeId}/to` | `/crm/limits/2026-09/associations/records/{fromObjectTypeId}/to` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/associations/records/{fromObjectTypeId}/{toObjectTypeId}` | `/crm/limits/2026-09/associations/records/{fromObjectTypeId}/{toObjectTypeId}` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/calculated-properties` | `/crm/limits/2026-09/calculated-properties` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/custom-object-types` | `/crm/limits/2026-09/custom-object-types` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/custom-properties` | `/crm/limits/2026-09/custom-properties` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/pipelines` | `/crm/limits/2026-09/pipelines` | CHANGED |
| Limits Tracking | GET | `/crm/v3/limits/records` | `/crm/limits/2026-09/records` | CHANGED |
| Line Items | GET | `/crm/v3/objects/line_items` | `/crm/objects/2026-09/line_items` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items` | `/crm/objects/2026-09/line_items` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/batch/archive` | `/crm/objects/2026-09/line_items/batch/archive` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/batch/create` | `/crm/objects/2026-09/line_items/batch/create` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/batch/read` | `/crm/objects/2026-09/line_items/batch/read` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/batch/update` | `/crm/objects/2026-09/line_items/batch/update` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/batch/upsert` | `/crm/objects/2026-09/line_items/batch/upsert` | CHANGED |
| Line Items | POST | `/crm/v3/objects/line_items/search` | `/crm/objects/2026-09/line_items/search` | CHANGED |
| Line Items | GET | `/crm/v3/objects/line_items/{lineItemId}` | `/crm/objects/2026-09/line_items/{lineItemId}` | CHANGED |
| Line Items | DELETE | `/crm/v3/objects/line_items/{lineItemId}` | `/crm/objects/2026-09/line_items/{lineItemId}` | CHANGED |
| Line Items | PATCH | `/crm/v3/objects/line_items/{lineItemId}` | `/crm/objects/2026-09/line_items/{lineItemId}` | CHANGED |
| Listings | GET | `/crm/v3/objects/0-420` | `/crm/objects/2026-09/0-420` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420` | `/crm/objects/2026-09/0-420` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/batch/archive` | `/crm/objects/2026-09/0-420/batch/archive` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/batch/create` | `/crm/objects/2026-09/0-420/batch/create` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/batch/read` | `/crm/objects/2026-09/0-420/batch/read` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/batch/update` | `/crm/objects/2026-09/0-420/batch/update` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/batch/upsert` | `/crm/objects/2026-09/0-420/batch/upsert` | CHANGED |
| Listings | POST | `/crm/v3/objects/0-420/search` | `/crm/objects/2026-09/0-420/search` | CHANGED |
| Listings | GET | `/crm/v3/objects/0-420/{listingId}` | `/crm/objects/2026-09/0-420/{listingId}` | CHANGED |
| Listings | DELETE | `/crm/v3/objects/0-420/{listingId}` | `/crm/objects/2026-09/0-420/{listingId}` | CHANGED |
| Listings | PATCH | `/crm/v3/objects/0-420/{listingId}` | `/crm/objects/2026-09/0-420/{listingId}` | CHANGED |
| Lists | GET | `/crm/v3/lists` | `/crm/lists/2026-09` | CHANGED |
| Lists | POST | `/crm/v3/lists` | `/crm/lists/2026-09` | CHANGED |
| Lists | GET | `/crm/v3/lists/folders` | `/crm/lists/2026-09/folders` | CHANGED |
| Lists | POST | `/crm/v3/lists/folders` | `/crm/lists/2026-09/folders` | CHANGED |
| Lists | PUT | `/crm/v3/lists/folders/move-list` | `/crm/lists/2026-09/folders/move-list` | CHANGED |
| Lists | DELETE | `/crm/v3/lists/folders/{folderId}` | `/crm/lists/2026-09/folders/{folderId}` | CHANGED |
| Lists | PUT | `/crm/v3/lists/folders/{folderId}/move/{newParentFolderId}` | `/crm/lists/2026-09/folders/{folderId}/move/{newParentFolderId}` | CHANGED |
| Lists | PUT | `/crm/v3/lists/folders/{folderId}/rename` | `/crm/lists/2026-09/folders/{folderId}/rename` | CHANGED |
| Lists | GET | `/crm/v3/lists/idmapping` | `/crm/lists/2026-09/idmapping` | CHANGED |
| Lists | POST | `/crm/v3/lists/idmapping` | `/crm/lists/2026-09/idmapping` | CHANGED |
| Lists | GET | `/crm/v3/lists/object-type-id/{objectTypeId}/name/{listName}` | `/crm/lists/2026-09/object-type-id/{objectTypeId}/name/{listName}` | CHANGED |
| Lists | POST | `/crm/v3/lists/records/memberships/batch/read` | `/crm/lists/2026-09/records/memberships/batch/read` | CHANGED |
| Lists | GET | `/crm/v3/lists/records/{objectTypeId}/{recordId}/memberships` | `/crm/lists/2026-09/records/{objectTypeId}/{recordId}/memberships` | CHANGED |
| Lists | GET | `/crm/v3/lists/{listId}` | `/crm/lists/2026-09/{listId}` | CHANGED |
| Lists | DELETE | `/crm/v3/lists/{listId}` | `/crm/lists/2026-09/{listId}` | CHANGED |
| Lists | GET | `/crm/v3/lists/{listId}/memberships` | `/crm/lists/2026-09/{listId}/memberships` | CHANGED |
| Lists | DELETE | `/crm/v3/lists/{listId}/memberships` | `/crm/lists/2026-09/{listId}/memberships` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/memberships/add` | `/crm/lists/2026-09/{listId}/memberships/add` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/memberships/add-and-remove` | `/crm/lists/2026-09/{listId}/memberships/add-and-remove` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/memberships/add-from/{sourceListId}` | `/crm/lists/2026-09/{listId}/memberships/add-from/{sourceListId}` | CHANGED |
| Lists | GET | `/crm/v3/lists/{listId}/memberships/join-order` | `/crm/lists/2026-09/{listId}/memberships/join-order` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/memberships/remove` | `/crm/lists/2026-09/{listId}/memberships/remove` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/restore` | `/crm/lists/2026-09/{listId}/restore` | CHANGED |
| Lists | GET | `/crm/v3/lists/{listId}/schedule-conversion` | `/crm/lists/2026-09/{listId}/schedule-conversion` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/schedule-conversion` | `/crm/lists/2026-09/{listId}/schedule-conversion` | CHANGED |
| Lists | DELETE | `/crm/v3/lists/{listId}/schedule-conversion` | `/crm/lists/2026-09/{listId}/schedule-conversion` | CHANGED |
| Lists | GET | `/crm/v3/lists/{listId}/size-and-edits-history/between` | `/crm/lists/2026-09/{listId}/size-and-edits-history/between` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/update-list-filters` | `/crm/lists/2026-09/{listId}/update-list-filters` | CHANGED |
| Lists | PUT | `/crm/v3/lists/{listId}/update-list-name` | `/crm/lists/2026-09/{listId}/update-list-name` | CHANGED |
| Manage Event Definitions | GET | `/events/v3/event-definitions` | `/events/2026-09/event-definitions` | IDENTICAL |
| Manage Event Definitions | POST | `/events/v3/event-definitions` | `/events/2026-09/event-definitions` | IDENTICAL |
| Manage Event Definitions | GET | `/events/v3/event-definitions/{eventName}` | `/events/2026-09/event-definitions/{eventName}` | IDENTICAL |
| Manage Event Definitions | DELETE | `/events/v3/event-definitions/{eventName}` | `/events/2026-09/event-definitions/{eventName}` | IDENTICAL |
| Manage Event Definitions | PATCH | `/events/v3/event-definitions/{eventName}` | `/events/2026-09/event-definitions/{eventName}` | IDENTICAL |
| Manage Event Definitions | POST | `/events/v3/event-definitions/{eventName}/property` | `/events/2026-09/event-definitions/{eventName}/property` | IDENTICAL |
| Manage Event Definitions | DELETE | `/events/v3/event-definitions/{eventName}/property/{propertyName}` | `/events/2026-09/event-definitions/{eventName}/property/{propertyName}` | IDENTICAL |
| Manage Event Definitions | PATCH | `/events/v3/event-definitions/{eventName}/property/{propertyName}` | `/events/2026-09/event-definitions/{eventName}/property/{propertyName}` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails` | `/marketing/emails/2026-09` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails` | `/marketing/emails/2026-09` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/ab-test/create-variation` | `/marketing/emails/2026-09/ab-test/create-variation` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/clone` | `/marketing/emails/2026-09/clone` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/statistics/histogram` | `/marketing/emails/2026-09/statistics/histogram` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/statistics/list` | `/marketing/emails/2026-09/statistics/list` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/{emailId}` | `/marketing/emails/2026-09/{emailId}` | CHANGED |
| Marketing Emails | DELETE | `/marketing/v3/emails/{emailId}` | `/marketing/emails/2026-09/{emailId}` | CHANGED |
| Marketing Emails | PATCH | `/marketing/v3/emails/{emailId}` | `/marketing/emails/2026-09/{emailId}` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/{emailId}/ab-test/get-variation` | `/marketing/emails/2026-09/{emailId}/ab-test/get-variation` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/{emailId}/draft` | `/marketing/emails/2026-09/{emailId}/draft` | CHANGED |
| Marketing Emails | PATCH | `/marketing/v3/emails/{emailId}/draft` | `/marketing/emails/2026-09/{emailId}/draft` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/{emailId}/draft/reset` | `/marketing/emails/2026-09/{emailId}/draft/reset` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/{emailId}/publish` | `/marketing/emails/2026-09/{emailId}/publish` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/{emailId}/revisions` | `/marketing/emails/2026-09/{emailId}/revisions` | CHANGED |
| Marketing Emails | GET | `/marketing/v3/emails/{emailId}/revisions/{revisionId}` | `/marketing/emails/2026-09/{emailId}/revisions/{revisionId}` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore` | `/marketing/emails/2026-09/{emailId}/revisions/{revisionId}/restore` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft` | `/marketing/emails/2026-09/{emailId}/revisions/{revisionId}/restore-to-draft` | CHANGED |
| Marketing Emails | POST | `/marketing/v3/emails/{emailId}/unpublish` | `/marketing/emails/2026-09/{emailId}/unpublish` | CHANGED |
| Marketing Events | GET | `/marketing/marketing-events/v3` | `/marketing/marketing-events/2026-09` | IDENTICAL |
| Marketing Events | GET | `/marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists` | `/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists` | CHANGED |
| Marketing Events | PUT | `/marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}` | `/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists/{listId}` | CHANGED |
| Marketing Events | DELETE | `/marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}` | `/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists/{listId}` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/associations/{marketingEventId}/lists` | `/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists` | CHANGED |
| Marketing Events | PUT | `/marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}` | `/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists/{listId}` | CHANGED |
| Marketing Events | DELETE | `/marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}` | `/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists/{listId}` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create` | `/marketing/marketing-events/2026-09/attendance/{externalEventId}/{subscriberState}/create` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create` | `/marketing/marketing-events/2026-09/attendance/{externalEventId}/{subscriberState}/email-create` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/batch/archive` | `/marketing/marketing-events/2026-09/batch/archive` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/batch/update` | `/marketing/marketing-events/2026-09/batch/update` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events` | `/marketing/marketing-events/2026-09/events` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/delete` | `/marketing/marketing-events/2026-09/events/delete` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/events/search` | `/marketing/marketing-events/2026-09/events/search` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/upsert` | `/marketing/marketing-events/2026-09/events/upsert` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/events/{externalEventId}` | `/marketing/marketing-events/2026-09/events/{externalEventId}` | CHANGED |
| Marketing Events | PUT | `/marketing/v3/marketing-events/events/{externalEventId}` | `/marketing/marketing-events/2026-09/events/{externalEventId}` | CHANGED |
| Marketing Events | DELETE | `/marketing/v3/marketing-events/events/{externalEventId}` | `/marketing/marketing-events/2026-09/events/{externalEventId}` | CHANGED |
| Marketing Events | PATCH | `/marketing/v3/marketing-events/events/{externalEventId}` | `/marketing/marketing-events/2026-09/events/{externalEventId}` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/{externalEventId}/cancel` | `/marketing/marketing-events/2026-09/events/{externalEventId}/cancel` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/{externalEventId}/complete` | `/marketing/marketing-events/2026-09/events/{externalEventId}/complete` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert` | `/marketing/marketing-events/2026-09/events/{externalEventId}/{subscriberState}/email-upsert` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert` | `/marketing/marketing-events/2026-09/events/{externalEventId}/{subscriberState}/upsert` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/participations/contacts/{contactIdentifier}/breakdown` | `/marketing/marketing-events/2026-09/participations/contacts/{contactIdentifier}/breakdown` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}` | `/marketing/marketing-events/2026-09/participations/{externalAccountId}/{externalEventId}` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}/breakdown` | `/marketing/marketing-events/2026-09/participations/{externalAccountId}/{externalEventId}/breakdown` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/participations/{marketingEventId}` | `/marketing/marketing-events/2026-09/participations/{marketingEventId}` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/participations/{marketingEventId}/breakdown` | `/marketing/marketing-events/2026-09/participations/{marketingEventId}/breakdown` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/{appId}/settings` | `/marketing/marketing-events/2026-09/{appId}/settings` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/{appId}/settings` | `/marketing/marketing-events/2026-09/{appId}/settings` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/{externalEventId}/identifiers` | `/marketing/marketing-events/2026-09/{externalEventId}/identifiers` | CHANGED |
| Marketing Events | GET | `/marketing/v3/marketing-events/{objectId}` | `/marketing/marketing-events/2026-09/{objectId}` | CHANGED |
| Marketing Events | DELETE | `/marketing/v3/marketing-events/{objectId}` | `/marketing/marketing-events/2026-09/{objectId}` | CHANGED |
| Marketing Events | PATCH | `/marketing/v3/marketing-events/{objectId}` | `/marketing/marketing-events/2026-09/{objectId}` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/create` | `/marketing/marketing-events/2026-09/{objectId}/attendance/{subscriberState}/create` | CHANGED |
| Marketing Events | POST | `/marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/email-create` | `/marketing/marketing-events/2026-09/{objectId}/attendance/{subscriberState}/email-create` | CHANGED |
| Media Bridge | POST | `/media-bridge/v1/events/attention-span` | `/media-bridge/2026-09/events/attention-span` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/events/media-played` | `/media-bridge/2026-09/events/media-played` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/events/media-played-percent` | `/media-bridge/2026-09/events/media-played-percent` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/properties/{objectType}` | `/media-bridge/2026-09/{appId}/properties/{objectType}` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/properties/{objectType}` | `/media-bridge/2026-09/{appId}/properties/{objectType}` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/properties/{objectType}/batch/archive` | `/media-bridge/2026-09/{appId}/properties/{objectType}/batch/archive` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/properties/{objectType}/batch/create` | `/media-bridge/2026-09/{appId}/properties/{objectType}/batch/create` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/properties/{objectType}/batch/read` | `/media-bridge/2026-09/{appId}/properties/{objectType}/batch/read` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/properties/{objectType}/groups` | `/media-bridge/2026-09/{appId}/properties/{objectType}/groups` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/properties/{objectType}/groups` | `/media-bridge/2026-09/{appId}/properties/{objectType}/groups` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/groups/{groupName}` | IDENTICAL |
| Media Bridge | DELETE | `/media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/groups/{groupName}` | IDENTICAL |
| Media Bridge | PATCH | `/media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/groups/{groupName}` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/properties/{objectType}/{propertyName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/{propertyName}` | IDENTICAL |
| Media Bridge | DELETE | `/media-bridge/v1/{appId}/properties/{objectType}/{propertyName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/{propertyName}` | IDENTICAL |
| Media Bridge | PATCH | `/media-bridge/v1/{appId}/properties/{objectType}/{propertyName}` | `/media-bridge/2026-09/{appId}/properties/{objectType}/{propertyName}` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/schemas` | `/media-bridge/2026-09/{appId}/schemas` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/schemas/{objectType}` | `/media-bridge/2026-09/{appId}/schemas/{objectType}` | IDENTICAL |
| Media Bridge | PATCH | `/media-bridge/v1/{appId}/schemas/{objectType}` | `/media-bridge/2026-09/{appId}/schemas/{objectType}` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/schemas/{objectType}/associations` | `/media-bridge/2026-09/{appId}/schemas/{objectType}/associations` | IDENTICAL |
| Media Bridge | DELETE | `/media-bridge/v1/{appId}/schemas/{objectType}/associations/{associationId}` | `/media-bridge/2026-09/{appId}/schemas/{objectType}/associations/{associationId}` | IDENTICAL |
| Media Bridge | PUT | `/media-bridge/v1/{appId}/settings` | `/media-bridge/2026-09/{appId}/settings` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/settings/event-visibility` | `/media-bridge/2026-09/{appId}/settings/event-visibility` | IDENTICAL |
| Media Bridge | PATCH | `/media-bridge/v1/{appId}/settings/event-visibility` | `/media-bridge/2026-09/{appId}/settings/event-visibility` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/settings/object-definitions` | `/media-bridge/2026-09/{appId}/settings/object-definitions` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/settings/object-definitions/{mediaType}` | `/media-bridge/2026-09/{appId}/settings/object-definitions/{mediaType}` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/settings/oembed-domains` | `/media-bridge/2026-09/{appId}/settings/oembed-domains` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/settings/oembed-domains` | `/media-bridge/2026-09/{appId}/settings/oembed-domains` | IDENTICAL |
| Media Bridge | DELETE | `/media-bridge/v1/{appId}/settings/oembed-domains` | `/media-bridge/2026-09/{appId}/settings/oembed-domains` | IDENTICAL |
| Media Bridge | GET | `/media-bridge/v1/{appId}/settings/oembed-domains/{oEmbedDomainId}` | `/media-bridge/2026-09/{appId}/settings/oembed-domains/{oEmbedDomainId}` | IDENTICAL |
| Media Bridge | PATCH | `/media-bridge/v1/{appId}/settings/oembed-domains/{oEmbedDomainId}` | `/media-bridge/2026-09/{appId}/settings/oembed-domains/{oEmbedDomainId}` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/settings/register` | `/media-bridge/2026-09/{appId}/settings/register` | IDENTICAL |
| Media Bridge | POST | `/media-bridge/v1/{appId}/settings/video-association-definition` | `/media-bridge/2026-09/{appId}/settings/video-association-definition` | IDENTICAL |
| Meetings | POST | `/scheduler/v3/meetings/calendar` | `/scheduler/2026-09/meetings/calendar` | IDENTICAL |
| Meetings | GET | `/scheduler/v3/meetings/meeting-links` | `/scheduler/2026-09/meetings/meeting-links` | IDENTICAL |
| Meetings | POST | `/scheduler/v3/meetings/meeting-links/book` | `/scheduler/2026-09/meetings/meeting-links/book` | IDENTICAL |
| Meetings | GET | `/scheduler/v3/meetings/meeting-links/book/availability-page/{slug}` | `/scheduler/2026-09/meetings/meeting-links/book/availability-page/{slug}` | IDENTICAL |
| Meetings | GET | `/scheduler/v3/meetings/meeting-links/book/{slug}` | `/scheduler/2026-09/meetings/meeting-links/book/{slug}` | IDENTICAL |
| Multicurrency | POST | `/settings/v3/currencies/central-fx-rates/add-currency` | `/settings/currencies/2026-09/central-fx-rates/add-currency` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/central-fx-rates/information` | `/settings/currencies/2026-09/central-fx-rates/information` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/central-fx-rates/unsupported-currencies` | `/settings/currencies/2026-09/central-fx-rates/unsupported-currencies` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/codes` | `/settings/currencies/2026-09/codes` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/company-currency` | `/settings/currencies/2026-09/company-currency` | CHANGED |
| Multicurrency | PUT | `/settings/v3/currencies/company-currency` | `/settings/currencies/2026-09/company-currency` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/exchange-rates` | `/settings/currencies/2026-09/exchange-rates` | CHANGED |
| Multicurrency | POST | `/settings/v3/currencies/exchange-rates` | `/settings/currencies/2026-09/exchange-rates` | CHANGED |
| Multicurrency | POST | `/settings/v3/currencies/exchange-rates/batch/create` | `/settings/currencies/2026-09/exchange-rates/batch/create` | CHANGED |
| Multicurrency | POST | `/settings/v3/currencies/exchange-rates/batch/read` | `/settings/currencies/2026-09/exchange-rates/batch/read` | CHANGED |
| Multicurrency | POST | `/settings/v3/currencies/exchange-rates/batch/update` | `/settings/currencies/2026-09/exchange-rates/batch/update` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/exchange-rates/current` | `/settings/currencies/2026-09/exchange-rates/current` | CHANGED |
| Multicurrency | POST | `/settings/v3/currencies/exchange-rates/update-visibility` | `/settings/currencies/2026-09/exchange-rates/update-visibility` | CHANGED |
| Multicurrency | GET | `/settings/v3/currencies/exchange-rates/{exchangeRateId}` | `/settings/currencies/2026-09/exchange-rates/{exchangeRateId}` | CHANGED |
| Multicurrency | PATCH | `/settings/v3/currencies/exchange-rates/{exchangeRateId}` | `/settings/currencies/2026-09/exchange-rates/{exchangeRateId}` | CHANGED |
| Notes | GET | `/crm/v3/objects/notes` | `/crm/objects/2026-09/notes` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes` | `/crm/objects/2026-09/notes` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/batch/archive` | `/crm/objects/2026-09/notes/batch/archive` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/batch/create` | `/crm/objects/2026-09/notes/batch/create` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/batch/read` | `/crm/objects/2026-09/notes/batch/read` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/batch/update` | `/crm/objects/2026-09/notes/batch/update` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/batch/upsert` | `/crm/objects/2026-09/notes/batch/upsert` | CHANGED |
| Notes | POST | `/crm/v3/objects/notes/search` | `/crm/objects/2026-09/notes/search` | CHANGED |
| Notes | GET | `/crm/v3/objects/notes/{noteId}` | `/crm/objects/2026-09/notes/{noteId}` | CHANGED |
| Notes | DELETE | `/crm/v3/objects/notes/{noteId}` | `/crm/objects/2026-09/notes/{noteId}` | CHANGED |
| Notes | PATCH | `/crm/v3/objects/notes/{noteId}` | `/crm/objects/2026-09/notes/{noteId}` | CHANGED |
| Oauth | POST | `/oauth/v3/token` | `/oauth/2026-09/token` | IDENTICAL |
| Oauth | POST | `/oauth/v3/token/introspect` | `/oauth/2026-09/token/introspect` | IDENTICAL |
| Oauth | POST | `/oauth/v3/token/revoke` | `/oauth/2026-09/token/revoke` | IDENTICAL |
| Object Library | GET | `/crm/v3/object-library/enablement` | `/crm/object-library/2026-09/enablement` | CHANGED |
| Object Library | GET | `/crm/v3/object-library/enablement/{objectTypeId}` | `/crm/object-library/2026-09/enablement/{objectTypeId}` | CHANGED |
| Orders | GET | `/crm/v3/objects/orders` | `/crm/objects/2026-09/orders` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders` | `/crm/objects/2026-09/orders` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/batch/archive` | `/crm/objects/2026-09/orders/batch/archive` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/batch/create` | `/crm/objects/2026-09/orders/batch/create` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/batch/read` | `/crm/objects/2026-09/orders/batch/read` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/batch/update` | `/crm/objects/2026-09/orders/batch/update` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/batch/upsert` | `/crm/objects/2026-09/orders/batch/upsert` | CHANGED |
| Orders | POST | `/crm/v3/objects/orders/search` | `/crm/objects/2026-09/orders/search` | CHANGED |
| Orders | GET | `/crm/v3/objects/orders/{orderId}` | `/crm/objects/2026-09/orders/{orderId}` | CHANGED |
| Orders | DELETE | `/crm/v3/objects/orders/{orderId}` | `/crm/objects/2026-09/orders/{orderId}` | CHANGED |
| Orders | PATCH | `/crm/v3/objects/orders/{orderId}` | `/crm/objects/2026-09/orders/{orderId}` | CHANGED |
| Origins | GET | `/meta/network-origins/2026-03/ip-ranges` | `/meta/network-origins/2026-09/ip-ranges` | CHANGED |
| Origins | GET | `/meta/network-origins/2026-03/ip-ranges/simple` | `/meta/network-origins/2026-09/ip-ranges/simple` | IDENTICAL |
| Pages | GET | `/cms/v3/pages/landing-pages` | `/cms/pages/2026-09/landing-pages` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages` | `/cms/pages/2026-09/landing-pages` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/ab-test/create-variation` | `/cms/pages/2026-09/landing-pages/ab-test/create-variation` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/ab-test/end` | `/cms/pages/2026-09/landing-pages/ab-test/end` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/ab-test/rerun` | `/cms/pages/2026-09/landing-pages/ab-test/rerun` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/batch/archive` | `/cms/pages/2026-09/landing-pages/batch/archive` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/batch/create` | `/cms/pages/2026-09/landing-pages/batch/create` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/batch/read` | `/cms/pages/2026-09/landing-pages/batch/read` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/batch/update` | `/cms/pages/2026-09/landing-pages/batch/update` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/clone` | `/cms/pages/2026-09/landing-pages/clone` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/folders` | `/cms/pages/2026-09/landing-pages/folders` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders` | `/cms/pages/2026-09/landing-pages/folders` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders/batch/archive` | `/cms/pages/2026-09/landing-pages/folders/batch/archive` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders/batch/create` | `/cms/pages/2026-09/landing-pages/folders/batch/create` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders/batch/read` | `/cms/pages/2026-09/landing-pages/folders/batch/read` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders/batch/update` | `/cms/pages/2026-09/landing-pages/folders/batch/update` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/folders/{objectId}` | `/cms/pages/2026-09/landing-pages/folders/{objectId}` | CHANGED |
| Pages | DELETE | `/cms/v3/pages/landing-pages/folders/{objectId}` | `/cms/pages/2026-09/landing-pages/folders/{objectId}` | CHANGED |
| Pages | PATCH | `/cms/v3/pages/landing-pages/folders/{objectId}` | `/cms/pages/2026-09/landing-pages/folders/{objectId}` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/folders/{objectId}/revisions` | `/cms/pages/2026-09/landing-pages/folders/{objectId}/revisions` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/folders/{objectId}/revisions/{revisionId}` | `/cms/pages/2026-09/landing-pages/folders/{objectId}/revisions/{revisionId}` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/folders/{objectId}/revisions/{revisionId}/restore` | `/cms/pages/2026-09/landing-pages/folders/{objectId}/revisions/{revisionId}/restore` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/multi-language/attach-to-lang-group` | `/cms/pages/2026-09/landing-pages/multi-language/attach-to-lang-group` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/multi-language/create-language-variation` | `/cms/pages/2026-09/landing-pages/multi-language/create-language-variation` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/multi-language/detach-from-lang-group` | `/cms/pages/2026-09/landing-pages/multi-language/detach-from-lang-group` | CHANGED |
| Pages | PUT | `/cms/v3/pages/landing-pages/multi-language/set-new-lang-primary` | `/cms/pages/2026-09/landing-pages/multi-language/set-new-lang-primary` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/multi-language/update-languages` | `/cms/pages/2026-09/landing-pages/multi-language/update-languages` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/schedule` | `/cms/pages/2026-09/landing-pages/schedule` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/{objectId}` | `/cms/pages/2026-09/landing-pages/{objectId}` | CHANGED |
| Pages | DELETE | `/cms/v3/pages/landing-pages/{objectId}` | `/cms/pages/2026-09/landing-pages/{objectId}` | CHANGED |
| Pages | PATCH | `/cms/v3/pages/landing-pages/{objectId}` | `/cms/pages/2026-09/landing-pages/{objectId}` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/{objectId}/draft` | `/cms/pages/2026-09/landing-pages/{objectId}/draft` | CHANGED |
| Pages | PATCH | `/cms/v3/pages/landing-pages/{objectId}/draft` | `/cms/pages/2026-09/landing-pages/{objectId}/draft` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/{objectId}/draft/push-live` | `/cms/pages/2026-09/landing-pages/{objectId}/draft/push-live` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/{objectId}/draft/reset` | `/cms/pages/2026-09/landing-pages/{objectId}/draft/reset` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/{objectId}/revisions` | `/cms/pages/2026-09/landing-pages/{objectId}/revisions` | CHANGED |
| Pages | GET | `/cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}` | `/cms/pages/2026-09/landing-pages/{objectId}/revisions/{revisionId}` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}/restore` | `/cms/pages/2026-09/landing-pages/{objectId}/revisions/{revisionId}/restore` | CHANGED |
| Pages | POST | `/cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}/restore-to-draft` | `/cms/pages/2026-09/landing-pages/{objectId}/revisions/{revisionId}/restore-to-draft` | CHANGED |
| Pages | GET | `/cms/v3/pages/site-pages` | `/cms/pages/2026-09/site-pages` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages` | `/cms/pages/2026-09/site-pages` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/ab-test/create-variation` | `/cms/pages/2026-09/site-pages/ab-test/create-variation` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/ab-test/end` | `/cms/pages/2026-09/site-pages/ab-test/end` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/ab-test/rerun` | `/cms/pages/2026-09/site-pages/ab-test/rerun` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/batch/archive` | `/cms/pages/2026-09/site-pages/batch/archive` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/batch/create` | `/cms/pages/2026-09/site-pages/batch/create` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/batch/read` | `/cms/pages/2026-09/site-pages/batch/read` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/batch/update` | `/cms/pages/2026-09/site-pages/batch/update` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/clone` | `/cms/pages/2026-09/site-pages/clone` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/multi-language/attach-to-lang-group` | `/cms/pages/2026-09/site-pages/multi-language/attach-to-lang-group` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/multi-language/create-language-variation` | `/cms/pages/2026-09/site-pages/multi-language/create-language-variation` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/multi-language/detach-from-lang-group` | `/cms/pages/2026-09/site-pages/multi-language/detach-from-lang-group` | CHANGED |
| Pages | PUT | `/cms/v3/pages/site-pages/multi-language/set-new-lang-primary` | `/cms/pages/2026-09/site-pages/multi-language/set-new-lang-primary` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/multi-language/update-languages` | `/cms/pages/2026-09/site-pages/multi-language/update-languages` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/schedule` | `/cms/pages/2026-09/site-pages/schedule` | CHANGED |
| Pages | GET | `/cms/v3/pages/site-pages/{objectId}` | `/cms/pages/2026-09/site-pages/{objectId}` | CHANGED |
| Pages | DELETE | `/cms/v3/pages/site-pages/{objectId}` | `/cms/pages/2026-09/site-pages/{objectId}` | CHANGED |
| Pages | PATCH | `/cms/v3/pages/site-pages/{objectId}` | `/cms/pages/2026-09/site-pages/{objectId}` | CHANGED |
| Pages | GET | `/cms/v3/pages/site-pages/{objectId}/draft` | `/cms/pages/2026-09/site-pages/{objectId}/draft` | CHANGED |
| Pages | PATCH | `/cms/v3/pages/site-pages/{objectId}/draft` | `/cms/pages/2026-09/site-pages/{objectId}/draft` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/{objectId}/draft/push-live` | `/cms/pages/2026-09/site-pages/{objectId}/draft/push-live` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/{objectId}/draft/reset` | `/cms/pages/2026-09/site-pages/{objectId}/draft/reset` | CHANGED |
| Pages | GET | `/cms/v3/pages/site-pages/{objectId}/revisions` | `/cms/pages/2026-09/site-pages/{objectId}/revisions` | CHANGED |
| Pages | GET | `/cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}` | `/cms/pages/2026-09/site-pages/{objectId}/revisions/{revisionId}` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}/restore` | `/cms/pages/2026-09/site-pages/{objectId}/revisions/{revisionId}/restore` | CHANGED |
| Pages | POST | `/cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}/restore-to-draft` | `/cms/pages/2026-09/site-pages/{objectId}/revisions/{revisionId}/restore-to-draft` | CHANGED |
| Partner Clients | GET | `/crm/v3/objects/partner_clients` | `/crm/objects/2026-09/partner_clients` | CHANGED |
| Partner Clients | POST | `/crm/v3/objects/partner_clients/batch/read` | `/crm/objects/2026-09/partner_clients/batch/read` | CHANGED |
| Partner Clients | POST | `/crm/v3/objects/partner_clients/batch/update` | `/crm/objects/2026-09/partner_clients/batch/update` | CHANGED |
| Partner Clients | POST | `/crm/v3/objects/partner_clients/search` | `/crm/objects/2026-09/partner_clients/search` | CHANGED |
| Partner Clients | GET | `/crm/v3/objects/partner_clients/{partnerClientId}` | `/crm/objects/2026-09/partner_clients/{partnerClientId}` | CHANGED |
| Partner Clients | PATCH | `/crm/v3/objects/partner_clients/{partnerClientId}` | `/crm/objects/2026-09/partner_clients/{partnerClientId}` | CHANGED |
| Partner Services | GET | `/crm/v3/objects/partner_services` | `/crm/objects/2026-09/partner_services` | CHANGED |
| Partner Services | POST | `/crm/v3/objects/partner_services/batch/read` | `/crm/objects/2026-09/partner_services/batch/read` | CHANGED |
| Partner Services | POST | `/crm/v3/objects/partner_services/batch/update` | `/crm/objects/2026-09/partner_services/batch/update` | CHANGED |
| Partner Services | POST | `/crm/v3/objects/partner_services/search` | `/crm/objects/2026-09/partner_services/search` | CHANGED |
| Partner Services | GET | `/crm/v3/objects/partner_services/{partnerServiceId}` | `/crm/objects/2026-09/partner_services/{partnerServiceId}` | CHANGED |
| Partner Services | PATCH | `/crm/v3/objects/partner_services/{partnerServiceId}` | `/crm/objects/2026-09/partner_services/{partnerServiceId}` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}` | `/crm/pipelines/2026-09/{objectType}` | CHANGED |
| Pipelines | POST | `/crm/v3/pipelines/{objectType}` | `/crm/pipelines/2026-09/{objectType}` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}/{pipelineId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}` | CHANGED |
| Pipelines | PUT | `/crm/v3/pipelines/{objectType}/{pipelineId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}` | CHANGED |
| Pipelines | DELETE | `/crm/v3/pipelines/{objectType}/{pipelineId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}` | CHANGED |
| Pipelines | PATCH | `/crm/v3/pipelines/{objectType}/{pipelineId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}/{pipelineId}/audit` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/audit` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages` | CHANGED |
| Pipelines | POST | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages/{stageId}` | CHANGED |
| Pipelines | PUT | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages/{stageId}` | CHANGED |
| Pipelines | DELETE | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages/{stageId}` | CHANGED |
| Pipelines | PATCH | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages/{stageId}` | CHANGED |
| Pipelines | GET | `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}/audit` | `/crm/pipelines/2026-09/{objectType}/{pipelineId}/stages/{stageId}/audit` | CHANGED |
| Postal Mail | GET | `/crm/v3/objects/postal_mail` | `/crm/objects/2026-09/postal_mail` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail` | `/crm/objects/2026-09/postal_mail` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/batch/archive` | `/crm/objects/2026-09/postal_mail/batch/archive` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/batch/create` | `/crm/objects/2026-09/postal_mail/batch/create` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/batch/read` | `/crm/objects/2026-09/postal_mail/batch/read` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/batch/update` | `/crm/objects/2026-09/postal_mail/batch/update` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/batch/upsert` | `/crm/objects/2026-09/postal_mail/batch/upsert` | CHANGED |
| Postal Mail | POST | `/crm/v3/objects/postal_mail/search` | `/crm/objects/2026-09/postal_mail/search` | CHANGED |
| Postal Mail | GET | `/crm/v3/objects/postal_mail/{postalMailId}` | `/crm/objects/2026-09/postal_mail/{postalMailId}` | CHANGED |
| Postal Mail | DELETE | `/crm/v3/objects/postal_mail/{postalMailId}` | `/crm/objects/2026-09/postal_mail/{postalMailId}` | CHANGED |
| Postal Mail | PATCH | `/crm/v3/objects/postal_mail/{postalMailId}` | `/crm/objects/2026-09/postal_mail/{postalMailId}` | CHANGED |
| Posts | GET | `/cms/v3/blogs/posts` | `/cms/blogs/2026-09/posts` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts` | `/cms/blogs/2026-09/posts` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/batch/archive` | `/cms/blogs/2026-09/posts/batch/archive` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/batch/create` | `/cms/blogs/2026-09/posts/batch/create` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/batch/read` | `/cms/blogs/2026-09/posts/batch/read` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/batch/update` | `/cms/blogs/2026-09/posts/batch/update` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/clone` | `/cms/blogs/2026-09/posts/clone` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/multi-language/attach-to-lang-group` | `/cms/blogs/2026-09/posts/multi-language/attach-to-lang-group` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/multi-language/create-language-variation` | `/cms/blogs/2026-09/posts/multi-language/create-language-variation` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/multi-language/detach-from-lang-group` | `/cms/blogs/2026-09/posts/multi-language/detach-from-lang-group` | CHANGED |
| Posts | PUT | `/cms/v3/blogs/posts/multi-language/set-new-lang-primary` | `/cms/blogs/2026-09/posts/multi-language/set-new-lang-primary` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/multi-language/update-languages` | `/cms/blogs/2026-09/posts/multi-language/update-languages` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/schedule` | `/cms/blogs/2026-09/posts/schedule` | CHANGED |
| Posts | GET | `/cms/v3/blogs/posts/{objectId}` | `/cms/blogs/2026-09/posts/{objectId}` | CHANGED |
| Posts | DELETE | `/cms/v3/blogs/posts/{objectId}` | `/cms/blogs/2026-09/posts/{objectId}` | CHANGED |
| Posts | PATCH | `/cms/v3/blogs/posts/{objectId}` | `/cms/blogs/2026-09/posts/{objectId}` | CHANGED |
| Posts | GET | `/cms/v3/blogs/posts/{objectId}/draft` | `/cms/blogs/2026-09/posts/{objectId}/draft` | CHANGED |
| Posts | PATCH | `/cms/v3/blogs/posts/{objectId}/draft` | `/cms/blogs/2026-09/posts/{objectId}/draft` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/{objectId}/draft/push-live` | `/cms/blogs/2026-09/posts/{objectId}/draft/push-live` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/{objectId}/draft/reset` | `/cms/blogs/2026-09/posts/{objectId}/draft/reset` | CHANGED |
| Posts | GET | `/cms/v3/blogs/posts/{objectId}/revisions` | `/cms/blogs/2026-09/posts/{objectId}/revisions` | CHANGED |
| Posts | GET | `/cms/v3/blogs/posts/{objectId}/revisions/{revisionId}` | `/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore` | `/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}/restore` | CHANGED |
| Posts | POST | `/cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore-to-draft` | `/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}/restore-to-draft` | CHANGED |
| Products | GET | `/crm/v3/objects/products` | `/crm/objects/2026-09/products` | CHANGED |
| Products | POST | `/crm/v3/objects/products` | `/crm/objects/2026-09/products` | CHANGED |
| Products | POST | `/crm/v3/objects/products/batch/archive` | `/crm/objects/2026-09/products/batch/archive` | CHANGED |
| Products | POST | `/crm/v3/objects/products/batch/create` | `/crm/objects/2026-09/products/batch/create` | CHANGED |
| Products | POST | `/crm/v3/objects/products/batch/read` | `/crm/objects/2026-09/products/batch/read` | CHANGED |
| Products | POST | `/crm/v3/objects/products/batch/update` | `/crm/objects/2026-09/products/batch/update` | CHANGED |
| Products | POST | `/crm/v3/objects/products/batch/upsert` | `/crm/objects/2026-09/products/batch/upsert` | CHANGED |
| Products | POST | `/crm/v3/objects/products/search` | `/crm/objects/2026-09/products/search` | CHANGED |
| Products | GET | `/crm/v3/objects/products/{productId}` | `/crm/objects/2026-09/products/{productId}` | CHANGED |
| Products | DELETE | `/crm/v3/objects/products/{productId}` | `/crm/objects/2026-09/products/{productId}` | CHANGED |
| Products | PATCH | `/crm/v3/objects/products/{productId}` | `/crm/objects/2026-09/products/{productId}` | CHANGED |
| Projects | GET | `/crm/objects/v3/projects` | `/crm/objects/2026-09/projects` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects` | `/crm/objects/2026-09/projects` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/batch/archive` | `/crm/objects/2026-09/projects/batch/archive` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/batch/create` | `/crm/objects/2026-09/projects/batch/create` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/batch/read` | `/crm/objects/2026-09/projects/batch/read` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/batch/update` | `/crm/objects/2026-09/projects/batch/update` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/batch/upsert` | `/crm/objects/2026-09/projects/batch/upsert` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/merge` | `/crm/objects/2026-09/projects/merge` | IDENTICAL |
| Projects | POST | `/crm/objects/v3/projects/search` | `/crm/objects/2026-09/projects/search` | IDENTICAL |
| Projects | GET | `/crm/objects/v3/projects/{projectId}` | `/crm/objects/2026-09/projects/{projectId}` | IDENTICAL |
| Projects | DELETE | `/crm/objects/v3/projects/{projectId}` | `/crm/objects/2026-09/projects/{projectId}` | IDENTICAL |
| Projects | PATCH | `/crm/objects/v3/projects/{projectId}` | `/crm/objects/2026-09/projects/{projectId}` | IDENTICAL |
| Properties | GET | `/crm/v3/properties/{objectType}` | `/crm/properties/2026-09/{objectType}` | CHANGED |
| Properties | POST | `/crm/v3/properties/{objectType}/batch/archive` | `/crm/properties/2026-09/{objectType}/batch/archive` | CHANGED |
| Properties | POST | `/crm/v3/properties/{objectType}/batch/read` | `/crm/properties/2026-09/{objectType}/batch/read` | CHANGED |
| Properties | GET | `/crm/v3/properties/{objectType}/groups` | `/crm/properties/2026-09/{objectType}/groups` | CHANGED |
| Properties | POST | `/crm/v3/properties/{objectType}/groups` | `/crm/properties/2026-09/{objectType}/groups` | CHANGED |
| Properties | GET | `/crm/v3/properties/{objectType}/groups/{groupName}` | `/crm/properties/2026-09/{objectType}/groups/{groupName}` | CHANGED |
| Properties | DELETE | `/crm/v3/properties/{objectType}/groups/{groupName}` | `/crm/properties/2026-09/{objectType}/groups/{groupName}` | CHANGED |
| Properties | PATCH | `/crm/v3/properties/{objectType}/groups/{groupName}` | `/crm/properties/2026-09/{objectType}/groups/{groupName}` | CHANGED |
| Properties | GET | `/crm/v3/properties/{objectType}/{propertyName}` | `/crm/properties/2026-09/{objectType}/{propertyName}` | CHANGED |
| Properties | DELETE | `/crm/v3/properties/{objectType}/{propertyName}` | `/crm/properties/2026-09/{objectType}/{propertyName}` | CHANGED |
| Property Validations | GET | `/crm/v3/property-validations/{objectTypeId}` | `/crm/property-validations/2026-09/{objectTypeId}` | CHANGED |
| Property Validations | GET | `/crm/v3/property-validations/{objectTypeId}/{propertyName}` | `/crm/property-validations/2026-09/{objectTypeId}/{propertyName}` | CHANGED |
| Property Validations | GET | `/crm/v3/property-validations/{objectTypeId}/{propertyName}/rule-type/{ruleType}` | `/crm/property-validations/2026-09/{objectTypeId}/{propertyName}/rule-type/{ruleType}` | CHANGED |
| Property Validations | PUT | `/crm/v3/property-validations/{objectTypeId}/{propertyName}/rule-type/{ruleType}` | `/crm/property-validations/2026-09/{objectTypeId}/{propertyName}/rule-type/{ruleType}` | CHANGED |
| Public App Crm Cards | GET | `/crm/v3/extensions/cards-dev/sample-response` | `/crm/extensions/cards-dev/2026-09/sample-response` | CHANGED |
| Public App Crm Cards | GET | `/crm/v3/extensions/cards-dev/{appId}` | `/crm/extensions/cards-dev/2026-09/{appId}` | CHANGED |
| Public App Crm Cards | POST | `/crm/v3/extensions/cards-dev/{appId}` | `/crm/extensions/cards-dev/2026-09/{appId}` | CHANGED |
| Public App Crm Cards | POST | `/crm/v3/extensions/cards-dev/{appId}/views/migrate` | `/crm/extensions/cards-dev/2026-09/{appId}/views/migrate` | CHANGED |
| Public App Crm Cards | GET | `/crm/v3/extensions/cards-dev/{appId}/{cardId}` | `/crm/extensions/cards-dev/2026-09/{appId}/{cardId}` | CHANGED |
| Public App Crm Cards | DELETE | `/crm/v3/extensions/cards-dev/{appId}/{cardId}` | `/crm/extensions/cards-dev/2026-09/{appId}/{cardId}` | CHANGED |
| Public App Crm Cards | PATCH | `/crm/v3/extensions/cards-dev/{appId}/{cardId}` | `/crm/extensions/cards-dev/2026-09/{appId}/{cardId}` | CHANGED |
| Public App Feature Flags V3 | GET | `/feature-flags/v3/{appId}/flags/all` | `/feature-flags/2026-09/{appId}/flags/all` | IDENTICAL |
| Public App Feature Flags V3 | GET | `/feature-flags/v3/{appId}/flags/{flagName}` | `/feature-flags/2026-09/{appId}/flags/{flagName}` | IDENTICAL |
| Public App Feature Flags V3 | PUT | `/feature-flags/v3/{appId}/flags/{flagName}` | `/feature-flags/2026-09/{appId}/flags/{flagName}` | IDENTICAL |
| Public App Feature Flags V3 | DELETE | `/feature-flags/v3/{appId}/flags/{flagName}` | `/feature-flags/2026-09/{appId}/flags/{flagName}` | IDENTICAL |
| Public App Feature Flags V3 | GET | `/feature-flags/v3/{appId}/flags/{flagName}/portals` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals` | IDENTICAL |
| Public App Feature Flags V3 | POST | `/feature-flags/v3/{appId}/flags/{flagName}/portals/batch/delete` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals/batch/delete` | IDENTICAL |
| Public App Feature Flags V3 | POST | `/feature-flags/v3/{appId}/flags/{flagName}/portals/batch/upsert` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals/batch/upsert` | IDENTICAL |
| Public App Feature Flags V3 | GET | `/feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals/{portalId}` | IDENTICAL |
| Public App Feature Flags V3 | PUT | `/feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals/{portalId}` | IDENTICAL |
| Public App Feature Flags V3 | DELETE | `/feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}` | `/feature-flags/2026-09/{appId}/flags/{flagName}/portals/{portalId}` | IDENTICAL |
| Quotes | GET | `/crm/v3/objects/quotes` | `/crm/objects/2026-09/quotes` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes` | `/crm/objects/2026-09/quotes` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/batch/archive` | `/crm/objects/2026-09/quotes/batch/archive` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/batch/create` | `/crm/objects/2026-09/quotes/batch/create` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/batch/read` | `/crm/objects/2026-09/quotes/batch/read` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/batch/update` | `/crm/objects/2026-09/quotes/batch/update` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/batch/upsert` | `/crm/objects/2026-09/quotes/batch/upsert` | CHANGED |
| Quotes | POST | `/crm/v3/objects/quotes/search` | `/crm/objects/2026-09/quotes/search` | CHANGED |
| Quotes | GET | `/crm/v3/objects/quotes/{quoteId}` | `/crm/objects/2026-09/quotes/{quoteId}` | CHANGED |
| Quotes | DELETE | `/crm/v3/objects/quotes/{quoteId}` | `/crm/objects/2026-09/quotes/{quoteId}` | CHANGED |
| Quotes | PATCH | `/crm/v3/objects/quotes/{quoteId}` | `/crm/objects/2026-09/quotes/{quoteId}` | CHANGED |
| Schemas | GET | `/crm-object-schemas/v3/schemas` | `/crm-object-schemas/2026-09/schemas` | CHANGED |
| Schemas | POST | `/crm-object-schemas/v3/schemas/batch/read` | `/crm-object-schemas/2026-09/schemas/batch/read` | CHANGED |
| Schemas | GET | `/crm-object-schemas/v3/schemas/{objectType}` | `/crm-object-schemas/2026-09/schemas/{objectType}` | CHANGED |
| Schemas | DELETE | `/crm-object-schemas/v3/schemas/{objectType}` | `/crm-object-schemas/2026-09/schemas/{objectType}` | IDENTICAL |
| Schemas | POST | `/crm-object-schemas/v3/schemas/{objectType}/associations` | `/crm-object-schemas/2026-09/schemas/{objectType}/associations` | IDENTICAL |
| Schemas | DELETE | `/crm-object-schemas/v3/schemas/{objectType}/associations/{associationIdentifier}` | `/crm-object-schemas/2026-09/schemas/{objectType}/associations/{associationIdentifier}` | IDENTICAL |
| Send Event Completions | POST | `/events/v3/send` | `/events/2026-09/send` | IDENTICAL |
| Send Event Completions | POST | `/events/v3/send/batch` | `/events/2026-09/send/batch` | IDENTICAL |
| Sequences | GET | `/automation/v4/sequences` | `/automation/sequences/2026-09` | CHANGED |
| Sequences | POST | `/automation/v4/sequences/enrollments` | `/automation/sequences/2026-09/enrollments` | CHANGED |
| Sequences | GET | `/automation/v4/sequences/enrollments/contact/{contactId}` | `/automation/sequences/2026-09/enrollments/contact/{contactId}` | CHANGED |
| Sequences | GET | `/automation/v4/sequences/{sequenceId}` | `/automation/sequences/2026-09/{sequenceId}` | CHANGED |
| Services | GET | `/crm/v3/objects/0-162` | `/crm/objects/2026-09/0-162` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162` | `/crm/objects/2026-09/0-162` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/batch/archive` | `/crm/objects/2026-09/0-162/batch/archive` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/batch/create` | `/crm/objects/2026-09/0-162/batch/create` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/batch/read` | `/crm/objects/2026-09/0-162/batch/read` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/batch/update` | `/crm/objects/2026-09/0-162/batch/update` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/batch/upsert` | `/crm/objects/2026-09/0-162/batch/upsert` | CHANGED |
| Services | POST | `/crm/v3/objects/0-162/search` | `/crm/objects/2026-09/0-162/search` | CHANGED |
| Services | GET | `/crm/v3/objects/0-162/{serviceId}` | `/crm/objects/2026-09/0-162/{serviceId}` | CHANGED |
| Services | DELETE | `/crm/v3/objects/0-162/{serviceId}` | `/crm/objects/2026-09/0-162/{serviceId}` | CHANGED |
| Services | PATCH | `/crm/v3/objects/0-162/{serviceId}` | `/crm/objects/2026-09/0-162/{serviceId}` | CHANGED |
| Site Search | GET | `/cms/site-search/v3/search` | `/cms/site-search/2026-09/search` | IDENTICAL |
| Site Search | GET | `/cms/v3/site-search/indexed-data/{contentId}` | `/cms/site-search/2026-09/indexed-data/{contentId}` | CHANGED |
| Source Code | POST | `/cms/v3/source-code/extract/async` | `/cms/source-code/2026-09/extract/async` | CHANGED |
| Source Code | GET | `/cms/v3/source-code/extract/async/tasks/{taskId}/status` | `/cms/source-code/2026-09/extract/async/tasks/{taskId}/status` | CHANGED |
| Source Code | GET | `/cms/v3/source-code/{environment}/content/{path}` | `/cms/source-code/2026-09/{environment}/content/{path}` | CHANGED |
| Source Code | PUT | `/cms/v3/source-code/{environment}/content/{path}` | `/cms/source-code/2026-09/{environment}/content/{path}` | CHANGED |
| Source Code | POST | `/cms/v3/source-code/{environment}/content/{path}` | `/cms/source-code/2026-09/{environment}/content/{path}` | CHANGED |
| Source Code | DELETE | `/cms/v3/source-code/{environment}/content/{path}` | `/cms/source-code/2026-09/{environment}/content/{path}` | CHANGED |
| Source Code | GET | `/cms/v3/source-code/{environment}/metadata/{path}` | `/cms/source-code/2026-09/{environment}/metadata/{path}` | CHANGED |
| Source Code | POST | `/cms/v3/source-code/{environment}/validate/{path}` | `/cms/source-code/2026-09/{environment}/validate/{path}` | CHANGED |
| Subscriptions | GET | `/communication-preferences/v4/definitions` | `/communication-preferences/2026-09/definitions` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/links/generate` | `/communication-preferences/2026-09/links/generate` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/batch/read` | `/communication-preferences/2026-09/statuses/batch/read` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/batch/unsubscribe-all` | `/communication-preferences/2026-09/statuses/batch/unsubscribe-all` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/batch/unsubscribe-all/read` | `/communication-preferences/2026-09/statuses/batch/unsubscribe-all/read` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/batch/write` | `/communication-preferences/2026-09/statuses/batch/write` | IDENTICAL |
| Subscriptions | GET | `/communication-preferences/v4/statuses/{subscriberIdString}` | `/communication-preferences/2026-09/statuses/{subscriberIdString}` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/{subscriberIdString}` | `/communication-preferences/2026-09/statuses/{subscriberIdString}` | IDENTICAL |
| Subscriptions | GET | `/communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all` | `/communication-preferences/2026-09/statuses/{subscriberIdString}/unsubscribe-all` | IDENTICAL |
| Subscriptions | POST | `/communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all` | `/communication-preferences/2026-09/statuses/{subscriberIdString}/unsubscribe-all` | IDENTICAL |
| Tags | GET | `/cms/v3/blogs/tags` | `/cms/blogs/2026-09/tags` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags` | `/cms/blogs/2026-09/tags` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/batch/archive` | `/cms/blogs/2026-09/tags/batch/archive` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/batch/create` | `/cms/blogs/2026-09/tags/batch/create` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/batch/read` | `/cms/blogs/2026-09/tags/batch/read` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/batch/update` | `/cms/blogs/2026-09/tags/batch/update` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/multi-language/attach-to-lang-group` | `/cms/blogs/2026-09/tags/multi-language/attach-to-lang-group` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/multi-language/create-language-variation` | `/cms/blogs/2026-09/tags/multi-language/create-language-variation` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/multi-language/detach-from-lang-group` | `/cms/blogs/2026-09/tags/multi-language/detach-from-lang-group` | CHANGED |
| Tags | PUT | `/cms/v3/blogs/tags/multi-language/set-new-lang-primary` | `/cms/blogs/2026-09/tags/multi-language/set-new-lang-primary` | CHANGED |
| Tags | POST | `/cms/v3/blogs/tags/multi-language/update-languages` | `/cms/blogs/2026-09/tags/multi-language/update-languages` | CHANGED |
| Tags | GET | `/cms/v3/blogs/tags/{objectId}` | `/cms/blogs/2026-09/tags/{objectId}` | CHANGED |
| Tags | DELETE | `/cms/v3/blogs/tags/{objectId}` | `/cms/blogs/2026-09/tags/{objectId}` | CHANGED |
| Tags | PATCH | `/cms/v3/blogs/tags/{objectId}` | `/cms/blogs/2026-09/tags/{objectId}` | CHANGED |
| Tasks | GET | `/crm/v3/objects/tasks` | `/crm/objects/2026-09/tasks` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks` | `/crm/objects/2026-09/tasks` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/batch/archive` | `/crm/objects/2026-09/tasks/batch/archive` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/batch/create` | `/crm/objects/2026-09/tasks/batch/create` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/batch/read` | `/crm/objects/2026-09/tasks/batch/read` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/batch/update` | `/crm/objects/2026-09/tasks/batch/update` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/batch/upsert` | `/crm/objects/2026-09/tasks/batch/upsert` | CHANGED |
| Tasks | POST | `/crm/v3/objects/tasks/search` | `/crm/objects/2026-09/tasks/search` | CHANGED |
| Tasks | GET | `/crm/v3/objects/tasks/{taskId}` | `/crm/objects/2026-09/tasks/{taskId}` | CHANGED |
| Tasks | DELETE | `/crm/v3/objects/tasks/{taskId}` | `/crm/objects/2026-09/tasks/{taskId}` | CHANGED |
| Tasks | PATCH | `/crm/v3/objects/tasks/{taskId}` | `/crm/objects/2026-09/tasks/{taskId}` | CHANGED |
| Tax Rates | GET | `/tax-rates/v1/tax-rates` | `/tax-rates/2026-09/tax-rates` | IDENTICAL |
| Tax Rates | GET | `/tax-rates/v1/tax-rates/{taxRateGroupId}` | `/tax-rates/2026-09/tax-rates/{taxRateGroupId}` | IDENTICAL |
| Taxes | GET | `/crm/v3/objects/taxes` | `/crm/objects/2026-09/taxes` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes` | `/crm/objects/2026-09/taxes` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/batch/archive` | `/crm/objects/2026-09/taxes/batch/archive` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/batch/create` | `/crm/objects/2026-09/taxes/batch/create` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/batch/read` | `/crm/objects/2026-09/taxes/batch/read` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/batch/update` | `/crm/objects/2026-09/taxes/batch/update` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/batch/upsert` | `/crm/objects/2026-09/taxes/batch/upsert` | CHANGED |
| Taxes | POST | `/crm/v3/objects/taxes/search` | `/crm/objects/2026-09/taxes/search` | CHANGED |
| Taxes | GET | `/crm/v3/objects/taxes/{taxId}` | `/crm/objects/2026-09/taxes/{taxId}` | CHANGED |
| Taxes | DELETE | `/crm/v3/objects/taxes/{taxId}` | `/crm/objects/2026-09/taxes/{taxId}` | CHANGED |
| Taxes | PATCH | `/crm/v3/objects/taxes/{taxId}` | `/crm/objects/2026-09/taxes/{taxId}` | CHANGED |
| Tickets | GET | `/crm/v3/objects/tickets` | `/crm/objects/2026-09/tickets` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets` | `/crm/objects/2026-09/tickets` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/batch/archive` | `/crm/objects/2026-09/tickets/batch/archive` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/batch/create` | `/crm/objects/2026-09/tickets/batch/create` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/batch/read` | `/crm/objects/2026-09/tickets/batch/read` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/batch/update` | `/crm/objects/2026-09/tickets/batch/update` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/batch/upsert` | `/crm/objects/2026-09/tickets/batch/upsert` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/merge` | `/crm/objects/2026-09/tickets/merge` | CHANGED |
| Tickets | POST | `/crm/v3/objects/tickets/search` | `/crm/objects/2026-09/tickets/search` | CHANGED |
| Tickets | GET | `/crm/v3/objects/tickets/{ticketId}` | `/crm/objects/2026-09/tickets/{ticketId}` | CHANGED |
| Tickets | DELETE | `/crm/v3/objects/tickets/{ticketId}` | `/crm/objects/2026-09/tickets/{ticketId}` | CHANGED |
| Tickets | PATCH | `/crm/v3/objects/tickets/{ticketId}` | `/crm/objects/2026-09/tickets/{ticketId}` | CHANGED |
| Transactional Single Send | GET | `/marketing/v3/transactional/smtp-tokens` | `/marketing/transactional/2026-09/smtp-tokens` | CHANGED |
| Transactional Single Send | POST | `/marketing/v3/transactional/smtp-tokens` | `/marketing/transactional/2026-09/smtp-tokens` | CHANGED |
| Transactional Single Send | GET | `/marketing/v3/transactional/smtp-tokens/{tokenId}` | `/marketing/transactional/2026-09/smtp-tokens/{tokenId}` | CHANGED |
| Transactional Single Send | DELETE | `/marketing/v3/transactional/smtp-tokens/{tokenId}` | `/marketing/transactional/2026-09/smtp-tokens/{tokenId}` | CHANGED |
| Transactional Single Send | POST | `/marketing/v3/transactional/smtp-tokens/{tokenId}/password-reset` | `/marketing/transactional/2026-09/smtp-tokens/{tokenId}/password-reset` | CHANGED |
| Transcriptions | POST | `/crm/v3/extensions/calling/inbound-call` | `/crm/extensions/calling/2026-09/inbound-call` | CHANGED |
| Transcriptions | POST | `/crm/v3/extensions/calling/transcripts` | `/crm/extensions/calling/2026-09/transcripts` | CHANGED |
| Transcriptions | GET | `/crm/v3/extensions/calling/transcripts/{transcriptId}` | `/crm/extensions/calling/2026-09/transcripts/{transcriptId}` | CHANGED |
| Transcriptions | DELETE | `/crm/v3/extensions/calling/transcripts/{transcriptId}` | `/crm/extensions/calling/2026-09/transcripts/{transcriptId}` | CHANGED |
| Url Mappings | GET | `/url-mappings/v3/url-mappings` | `/url-mappings/2026-09/url-mappings` | IDENTICAL |
| Url Mappings | POST | `/url-mappings/v3/url-mappings` | `/url-mappings/2026-09/url-mappings` | IDENTICAL |
| Url Mappings | GET | `/url-mappings/v3/url-mappings/{id}` | `/url-mappings/2026-09/url-mappings/{id}` | IDENTICAL |
| Url Mappings | DELETE | `/url-mappings/v3/url-mappings/{id}` | `/url-mappings/2026-09/url-mappings/{id}` | IDENTICAL |
| Url Redirects | GET | `/cms/url-redirects/v3` | `/cms/url-redirects/2026-09` | CHANGED |
| Url Redirects | POST | `/cms/url-redirects/v3` | `/cms/url-redirects/2026-09` | CHANGED |
| Url Redirects | GET | `/cms/url-redirects/v3/url-mappings` | `/cms/url-redirects/2026-09/url-mappings` | CHANGED |
| Url Redirects | GET | `/cms/url-redirects/v3/url-mappings/{id}` | `/cms/url-redirects/2026-09/url-mappings/{id}` | CHANGED |
| Url Redirects | DELETE | `/cms/url-redirects/v3/url-mappings/{id}` | `/cms/url-redirects/2026-09/url-mappings/{id}` | IDENTICAL |
| Url Redirects | GET | `/cms/v3/url-redirects/{urlRedirectId}` | `/cms/url-redirects/2026-09/{urlRedirectId}` | CHANGED |
| Url Redirects | DELETE | `/cms/v3/url-redirects/{urlRedirectId}` | `/cms/url-redirects/2026-09/{urlRedirectId}` | CHANGED |
| User Provisioning | GET | `/settings/users/v3` | `/settings/users/2026-09` | IDENTICAL |
| User Provisioning | POST | `/settings/users/v3` | `/settings/users/2026-09` | IDENTICAL |
| User Provisioning | GET | `/settings/v3/users/roles` | `/settings/users/2026-09/roles` | CHANGED |
| User Provisioning | GET | `/settings/v3/users/teams` | `/settings/users/2026-09/teams` | CHANGED |
| User Provisioning | GET | `/settings/v3/users/{userId}` | `/settings/users/2026-09/{userId}` | CHANGED |
| User Provisioning | PUT | `/settings/v3/users/{userId}` | `/settings/users/2026-09/{userId}` | CHANGED |
| User Provisioning | DELETE | `/settings/v3/users/{userId}` | `/settings/users/2026-09/{userId}` | CHANGED |
| Users | GET | `/crm/v3/objects/users` | `/crm/objects/2026-09/users` | CHANGED |
| Users | POST | `/crm/v3/objects/users` | `/crm/objects/2026-09/users` | CHANGED |
| Users | POST | `/crm/v3/objects/users/batch/archive` | `/crm/objects/2026-09/users/batch/archive` | CHANGED |
| Users | POST | `/crm/v3/objects/users/batch/create` | `/crm/objects/2026-09/users/batch/create` | CHANGED |
| Users | POST | `/crm/v3/objects/users/batch/read` | `/crm/objects/2026-09/users/batch/read` | CHANGED |
| Users | POST | `/crm/v3/objects/users/batch/update` | `/crm/objects/2026-09/users/batch/update` | CHANGED |
| Users | POST | `/crm/v3/objects/users/batch/upsert` | `/crm/objects/2026-09/users/batch/upsert` | CHANGED |
| Users | POST | `/crm/v3/objects/users/search` | `/crm/objects/2026-09/users/search` | CHANGED |
| Users | GET | `/crm/v3/objects/users/{userId}` | `/crm/objects/2026-09/users/{userId}` | CHANGED |
| Users | DELETE | `/crm/v3/objects/users/{userId}` | `/crm/objects/2026-09/users/{userId}` | CHANGED |
| Users | PATCH | `/crm/v3/objects/users/{userId}` | `/crm/objects/2026-09/users/{userId}` | CHANGED |
| Video Conferencing Extension | GET | `/crm/v3/extensions/videoconferencing/settings/{appId}` | `/crm/extensions/videoconferencing/2026-09/settings/{appId}` | CHANGED |
| Video Conferencing Extension | PUT | `/crm/v3/extensions/videoconferencing/settings/{appId}` | `/crm/extensions/videoconferencing/2026-09/settings/{appId}` | CHANGED |
| Video Conferencing Extension | DELETE | `/crm/v3/extensions/videoconferencing/settings/{appId}` | `/crm/extensions/videoconferencing/2026-09/settings/{appId}` | CHANGED |
| Visitor Identification | POST | `/visitor-identification/v3/tokens/create` | `/visitor-identification/2026-09/tokens/create` | IDENTICAL |
