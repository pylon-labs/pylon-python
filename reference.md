# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">list</a>(...) -> GetAccountsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of accounts for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of accounts to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">create</a>(...) -> CreateAccountResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new account with the specified name and optional metadata.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the account.
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `typing.Optional[CreateAccountRequestAccountType]` — The type of the account. Must be one of "customer", "internal", "community", or "partner". Defaults to "customer" if not specified.
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[Channel]]` — An array of channels to be linked to this account.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this account.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Deprecated. Please use Domains and PrimaryDomain instead.
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` — The domains of the account, without any leading scheme, for example stripe.com. Must specify one domain as primary.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.List[ExternalId]]` — An array of external IDs to be used on this account. If provided, the account's external IDs will be updated to the given external IDs.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — The logo URL of the account. Must be a square .png, .jpg or .jpeg.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — The ID of the owner of the account.
    
</dd>
</dl>

<dl>
<dd>

**primary_domain:** `typing.Optional[str]` — Must be in the list of domains. If there are any domains, there must be exactly one primary domain.
    
</dd>
</dl>

<dl>
<dd>

**subaccount_ids:** `typing.Optional[typing.List[str]]` — An array of account IDs to be added as subaccounts to this account. For normal accounts, these represent subaccounts. For partner accounts, these represent associated accounts.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — An array of strings to use as tags on this account. If provided, the accounts tags will be updated to the given tags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">bulk_update</a>(...) -> UpdateAccountsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates multiple accounts in a single request. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.bulk_update(
    account_ids=[
        "account_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_ids:** `typing.List[str]` — The account IDs to update. The number of accounts to update must be between 1 and 100.
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `typing.Optional[UpdateAccountsRequestAccountType]` — The type of the account. Can only be changed to "customer" or "partner".
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be updated on the accounts.
    
</dd>
</dl>

<dl>
<dd>

**is_disabled:** `typing.Optional[bool]` — Whether the accounts are disabled.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — The ID of the new owner. If empty string is passed in, the owner will be removed.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — An array of tags to be updated on the accounts.
    
</dd>
</dl>

<dl>
<dd>

**tags_apply_mode:** `typing.Optional[UpdateAccountsRequestTagsApplyMode]` — The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">merge</a>(...) -> MergeAccountsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merges one or more accounts into a surviving account. Issues, contacts, opportunities, domains, channels, external IDs, and other associated data are transferred to the surviving account. Tags and custom field values of the merged accounts are not transferred. The merged accounts are permanently deleted. This cannot be undone. Accounts are merged sequentially, each in its own transaction; if a merge fails partway through, accounts already merged are not restored.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.merge(
    merge_account_ids=[
        "merge_account_ids"
    ],
    merge_into_account_id="merge_into_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merge_account_ids:** `typing.List[str]` — The IDs of the accounts to merge into the surviving account. These accounts are permanently deleted after their data is transferred. The number of accounts to merge must be between 1 and 100.
    
</dd>
</dl>

<dl>
<dd>

**merge_into_account_id:** `str` — The ID of the account that will survive the merge and receive the merged data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">search</a>(...) -> SearchAccountsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optionally pass `search_text` for fuzzy matching. Results are intersected with any provided filter.

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `id` | `equals`, `in`, `not_in` |
 `domains` | `contains`, `does_not_contain`, `in`, `not_in` |
 `tags` | `contains`, `does_not_contain`, `in`, `not_in` |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `external_ids` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `owner_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |

For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of accounts to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Fuzzy text search. Results are intersected with any provided filter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">get</a>(...) -> GetAccountResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single account by ID or external ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the account to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">delete</a>(...) -> DeleteAccountResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an account by ID or external ID.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the account to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">update</a>(...) -> UpdateAccountResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing account by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the account to update.
    
</dd>
</dl>

<dl>
<dd>

**account_type:** `typing.Optional[UpdateAccountRequestBodyAccountType]` — The type of the account. Can only be changed to "customer" or "partner".
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[Channel]]` — An array of channels to be linked to this account. If provided, replaces the account's linked channels; channels you leave out are unlinked.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this account.
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` — Domains of the account. Replaces the account's domains. Must specify one domain as primary.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.List[ExternalId]]` — An array of external IDs to be used on this account. If provided, the account's external IDs will be updated to the given external IDs.
    
</dd>
</dl>

<dl>
<dd>

**is_disabled:** `typing.Optional[bool]` — Whether the account is disabled.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — Logo URL of the account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the account.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — The ID of the owner of the account. If empty string is passed in, the owner will be removed.
    
</dd>
</dl>

<dl>
<dd>

**primary_domain:** `typing.Optional[str]` — Must be in the list of domains. If there are any domains, there must be exactly one primary domain.
    
</dd>
</dl>

<dl>
<dd>

**subaccount_ids:** `typing.Optional[typing.List[str]]` — An array of account IDs to set as this account's subaccounts. If provided, the account's subaccounts become exactly this list; accounts you leave out are detached.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — An array of strings to use as tags on this account. If provided, the accounts tags will be updated to the given tags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/usepylon/accounts/client.py">upload_file</a>(...) -> UploadAccountFileResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads one or more files to an account by ID or external ID.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.upload_file(
    account_id="id",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account to upload files to.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The file to upload.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — The URL to fetch the file from, if the file is not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ActivityTypes
<details><summary><code>client.activity_types.<a href="src/usepylon/activity_types/client.py">list</a>() -> GetActivityTypesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom activity type definitions for the organization.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.activity_types.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ArticleFeedback
<details><summary><code>client.article_feedback.<a href="src/usepylon/article_feedback/client.py">list</a>(...) -> GetArticleFeedbackResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of knowledge base article feedback for the organization.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.article_feedback.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of feedback submissions to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**knowledge_base_id:** `typing.Optional[str]` — The ID of the knowledge base to filter by.
    
</dd>
</dl>

<dl>
<dd>

**article_id:** `typing.Optional[str]` — The ID of the article to filter by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Attachments
<details><summary><code>client.attachments.<a href="src/usepylon/attachments/client.py">create</a>(...) -> CreateAttachmentResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a file as an attachment. Send either `file` or `file_url` (`file` takes precedence if both are sent); one file per request. Executable and script files are rejected. The returned `url` is a signed link; pass it in `attachment_urls` when creating issues or messages. Files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link. This applies to direct uploads and files fetched through file_url. Downstream delivery channels may impose smaller limits.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.attachments.create(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the file.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The file to upload. Send either `file` or `file_url`; if both are sent, `file` is used and `file_url` is ignored. Files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link.
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` — The URL to fetch the file from. Ignored when `file` is also sent. Fetched files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AuditLogs
<details><summary><code>client.audit_logs.<a href="src/usepylon/audit_logs/client.py">list</a>(...) -> GetAuditLogsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of audit log entries for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.audit_logs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of audit logs to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audit_logs.<a href="src/usepylon/audit_logs/client.py">search</a>(...) -> GetAuditLogsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a filtered, paginated list of audit log entries for the organization.
Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `action` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain` |
 `action_happened_at` | `time_is_after`, `time_is_before`, `time_range` |
 `object_id` | `equals`, `in`, `not_in` |

Timestamp values use RFC3339 format. `object_id` is the ID of the object the entry is
for, matching the `object_id` field of the returned entries.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.audit_logs.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of audit logs to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CallRecordings
<details><summary><code>client.call_recordings.<a href="src/usepylon/call_recordings/client.py">create</a>(...) -> CreateCallRecordingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a call recording from your own call recorder. Set app_type to `custom_call_recorder`; the Custom Call Recorder integration must be enabled for your organization, or the request returns 400. start_time, end_time, and at least one call_recording_messages entry are required. Every speaker_email must appear in participant_emails or match primary_user_email. The recording is linked to account_id if provided, otherwise to an account matched from the participant emails. Reusing a recording_id returns the existing recording unchanged.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon, CreateCallRecordingMessageRequest
from usepylon.environment import PylonEnvironment
import datetime

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.call_recordings.create(
    app_type="custom_call_recorder",
    call_recording_messages=[
        CreateCallRecordingMessageRequest(
            message_content="message_content",
        )
    ],
    end_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    start_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_type:** `CreateCallRecordingRequestAppType` — The source of the recording. Must be `custom_call_recorder`, which requires the Custom Call Recorder integration to be enabled.
    
</dd>
</dl>

<dl>
<dd>

**call_recording_messages:** `typing.List[CreateCallRecordingMessageRequest]` — The transcript, one entry per utterance. `custom_call_recorder` takes its transcript only from this field and ignores a plain-text transcript.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `datetime.datetime` — When the call ended, in RFC3339 format (e.g. 2025-01-01T01:00:00Z).
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `datetime.datetime` — When the call started, in RFC3339 format (e.g. 2025-01-01T00:00:00Z).
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The ID of the account to link this call recording to. If provided, the participant emails are not used for account matching, and an unknown ID returns 400. If omitted, Pylon matches an account from the participant emails, ignoring your organization's own domains; the recording is created without an account if none matches.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — Custom fields to set on the call recording. Use slugs from GET /custom-fields?object_type=meeting. Each entry needs a slug and either value or values, not both.
    
</dd>
</dl>

<dl>
<dd>

**participant_emails:** `typing.Optional[str]` — Comma-separated emails of everyone on the call (e.g. "alice@customer.com,bob@yourcompany.com"). Used to match the account when account_id is omitted. Every speaker_email in call_recording_messages must be in this list or match primary_user_email.
    
</dd>
</dl>

<dl>
<dd>

**primary_user_email:** `typing.Optional[str]` — The email of the Pylon user who owns the recording. Counted as a participant, so it does not need to be repeated in participant_emails.
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `typing.Optional[str]` — Your unique ID for this recording. Pylon deduplicates on recording_id and app_type: a request that reuses a recording_id returns the existing recording unchanged. Send a unique value for every call; if you omit it, every request after the first returns the same recording.
    
</dd>
</dl>

<dl>
<dd>

**recording_url:** `typing.Optional[str]` — A link to the recording in your call recorder. Maximum 255 characters.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the call recording.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.call_recordings.<a href="src/usepylon/call_recordings/client.py">search</a>(...) -> SearchCallRecordingsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `source` | `equals`, `in`, `not_in` |
 `title` | `equals`, `string_contains` |
 `start_time` | `time_is_after`, `time_is_before`, `time_range` |

Timestamp values use RFC3339 format.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.call_recordings.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of call recordings to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.call_recordings.<a href="src/usepylon/call_recordings/client.py">get</a>(...) -> GetCallRecordingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single call recording by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.call_recordings.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the call recording to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.call_recordings.<a href="src/usepylon/call_recordings/client.py">delete</a>(...) -> DeleteCallRecordingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a call recording by its Pylon ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.call_recordings.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The Pylon ID of the call recording to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.call_recordings.<a href="src/usepylon/call_recordings/client.py">update</a>(...) -> UpdateCallRecordingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a call recording by ID. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.call_recordings.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the call recording to update.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account ID to associate with the call recording. Pass an empty string to remove the account association.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to set on the call recording. Only passed in fields will be modified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">list</a>(...) -> GetContactsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of contacts for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of contacts to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">create</a>(...) -> CreateContactResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new contact with the specified email and optional metadata.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**account_external_id:** `typing.Optional[str]` — The external ID of the account that this contact belongs to. Cannot be used together with account_id.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account that this contact belongs to.
    
</dd>
</dl>

<dl>
<dd>

**avatar_url:** `typing.Optional[str]` — The avatar URL of the contact. Must be a square .png, .jpg or .jpeg.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be applied to this contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email of the contact.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.List[ExternalId]]` — An array of external IDs to be used on this contact.
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.List[str]]` — The phone numbers of the contact. Must contain only digits 0-9, optionally preceded by + (E.164, e.g. +4365446231), and be 15 digits or less. Include the + and country code for non-US numbers; a 10-digit number without + is treated as US.
    
</dd>
</dl>

<dl>
<dd>

**portal_role:** `typing.Optional[str]` 

The portal role to assign to the contact. If not provided uses the default portal role from the portal settings.

Known values: `no_access`, `member`, `admin`. This list is not exhaustive.
    
</dd>
</dl>

<dl>
<dd>

**portal_role_id:** `typing.Optional[str]` — The ID of the custom portal role to assign to the contact. Takes precedence over portal_role if provided.
    
</dd>
</dl>

<dl>
<dd>

**primary_phone_number:** `typing.Optional[str]` — The primary phone number. Must be in the list of phone_numbers. If there are any phone_numbers and this is not specified, the first phone number will be primary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">search</a>(...) -> SearchContactsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `id` | `equals`, `in`, `not_in` |
 `email` | `equals`, `in`, `not_in`, `string_contains` |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `account_id` | `equals`, `in`, `not_in` |

For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of contacts to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Text search across contact name, primary email, secondary emails, primary phone number, and secondary phone numbers. Results are intersected with any provided filter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">get</a>(...) -> GetContactResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single contact by ID or external ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">delete</a>(...) -> DeleteContactResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a contact by ID or external ID.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the contact to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/usepylon/contacts/client.py">update</a>(...) -> UpdateContactResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a contact by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.contacts.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or external ID of the contact to update.
    
</dd>
</dl>

<dl>
<dd>

**account_external_id:** `typing.Optional[str]` — The external ID of the account to move the contact to. Cannot be used together with account_id.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account to move the contact to. If empty string is passed in, the contact will be removed from its account.
    
</dd>
</dl>

<dl>
<dd>

**avatar_url:** `typing.Optional[str]` — The avatar URL of the contact. Must be a square .png, .jpg or .jpeg.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be applied to this contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email of the contact. Replaces all of the contact's emails with this single email. Cannot be used together with the `emails` array field.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.List[UpdateContactEmail]]` 

The emails of the contact as an array. Cannot be used together with the singular `email` field.
Each entry must include an `email` string and an optional `is_primary` boolean.
If no email is marked as primary, the first email becomes the primary.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.List[ExternalId]]` — An array of external IDs to be used on this contact. If provided, the contact's external IDs will be updated to the given external IDs.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

in: body
The name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.List[str]]` — The phone numbers of the contact. Must contain only digits 0-9, optionally preceded by + (E.164, e.g. +4365446231), and be 15 digits or less. Include the + and country code for non-US numbers; a 10-digit number without + is treated as US.
    
</dd>
</dl>

<dl>
<dd>

**portal_role:** `typing.Optional[str]` 

The portal role to assign to the contact. Can be one of `no_access`, `member`, or `admin`, or a custom role slug.

Known values: `no_access`, `member`, `admin`. This list is not exhaustive.
    
</dd>
</dl>

<dl>
<dd>

**portal_role_id:** `typing.Optional[str]` — The ID of the custom portal role to assign to the contact. Takes precedence over portal_role if provided.
    
</dd>
</dl>

<dl>
<dd>

**primary_phone_number:** `typing.Optional[str]` — The primary phone number. Must be in the list of phone_numbers. If there are any phone_numbers and this is not specified, the first phone number will be primary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomFields
<details><summary><code>client.custom_fields.<a href="src/usepylon/custom_fields/client.py">list</a>(...) -> GetCustomFieldsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom field definitions for the specified object type. Use `slug` (and `select_metadata.options[].slug` for option values) in API writes and filters.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.list(
    object_type="account",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `ListCustomFieldsRequestObjectType` — The object type of the custom fields. Can be "account", "issue", "contact", "task", "project", "meeting", or "opportunity".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_fields.<a href="src/usepylon/custom_fields/client.py">create</a>(...) -> CreateCustomFieldResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new custom field definition for the specified object type.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.create(
    label="label",
    object_type="account",
    type="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `str` — The label of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `CreateCustomFieldRequestBodyObjectType` — The object type of the custom field. Can be "account", "issue", "contact", "task", "project", "meeting", or "opportunity".
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of the custom field. Can be one of `text`, `number`, `decimal`, `boolean`, `date`, `datetime`, `user`, `url`, `select`, or `multiselect`.
    
</dd>
</dl>

<dl>
<dd>

**default_value:** `typing.Optional[str]` — The default value for single-valued custom fields.
    
</dd>
</dl>

<dl>
<dd>

**default_values:** `typing.Optional[typing.List[str]]` — The default values for multi-valued custom fields.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**select_options:** `typing.Optional[typing.List[CustomFieldDefinitionSelectOption]]` — The list options of the select custom field. This is only present for select and multiselect custom fields.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_fields.<a href="src/usepylon/custom_fields/client.py">get</a>(...) -> GetCustomFieldResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single custom field definition by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_fields.<a href="src/usepylon/custom_fields/client.py">update</a>(...) -> UpdateCustomFieldResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a custom field definition. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**default_value:** `typing.Optional[str]` — The default value for single-valued custom fields.
    
</dd>
</dl>

<dl>
<dd>

**default_values:** `typing.Optional[typing.List[str]]` — The default values for multi-valued custom fields.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — The label of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**select_options:** `typing.Optional[typing.List[CustomFieldDefinitionSelectOption]]` — The complete list of options for a select or multiselect custom field. Options missing from the list are deleted and their stored values are cleared asynchronously. Prefer the dedicated select option endpoints, which can rename an option without losing stored values.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomObjects
<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">list</a>(...) -> GetCustomObjectsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns paginated custom objects of the given type.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.list(
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor for the next page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results per page. Defaults to 25, max 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">create</a>(...) -> CreateCustomObjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new custom object instance of the given type. To link the object to an account, pass the built-in Account relationship field in `custom_fields`: `{"name":"Example","custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.create(
    type="type",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the custom object.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, CustomFieldValue]]` — Custom field values to set on the object, keyed by field slug. To link the object to an account, pass the built-in Account relationship field as `custom_fields.account.value`, for example `{"custom_fields":{"account":{"value":"account_uuid"}}}`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">bulk_update</a>(...) -> UpdateCustomObjectsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies the same update to multiple custom objects of the given type in a single request. Pass between 1 and 100 IDs and the custom field values to set; only the provided fields are modified on each object. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"ids":["object_uuid"],"custom_fields":{"account":{"value":"account_uuid"}}}`. To unset a field, pass its slug with an empty value.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.bulk_update(
    type="type",
    ids=[
        "ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "opportunity").
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.List[str]` — The IDs of the custom objects to update. Must be between 1 and 100 IDs.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, CustomFieldValue]]` — Custom field values to apply to every listed custom object, keyed by field slug. To unset a field, pass its slug with an empty value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">search</a>(...) -> SearchCustomObjectsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `name` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `is_set`, `is_unset` |
 `account` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

`account` is the built-in Account relationship field present on every custom object type; its values are account IDs.
Timestamp values use RFC3339 format. For custom fields, pass the field slug as `field`.

A `{type}` of `opportunity` is an alias for the opportunities API and filters on a different set of fields:

 Field | Allowed operators |
 --- | --- |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `account_id` | `equals`, `in`, `not_in` |
 `source` | `equals`, `in`, `not_in` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.search(
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of results to fetch. Defaults to 25, max 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">get</a>(...) -> GetCustomObjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single custom object by ID, including its custom field values.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.get(
    type="type",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of the custom object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">delete</a>(...) -> DeleteCustomObjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a custom object instance.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.delete(
    type="type",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of the custom object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_objects.<a href="src/usepylon/custom_objects/client.py">update</a>(...) -> UpdateCustomObjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a custom object. Only provided fields are modified. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_objects.update(
    type="type",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The type slug of the custom object (e.g. "companies").
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of the custom object.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, CustomFieldValue]]` — Custom field values to set on the object, keyed by field slug. To update the linked account, pass the built-in Account relationship field as `custom_fields.account.value`, for example `{"custom_fields":{"account":{"value":"account_uuid"}}}`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the custom object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EmailSuppressions
<details><summary><code>client.email_suppressions.<a href="src/usepylon/email_suppressions/client.py">list</a>(...) -> GetEmailSuppressionsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the email addresses Pylon will not send to, most recently suppressed first. Pass `email` to check a single address; an empty `data` array means it is not suppressed.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.email_suppressions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — Only return the suppression for this email address, if one exists.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of suppressions to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_suppressions.<a href="src/usepylon/email_suppressions/client.py">delete</a>(...) -> DeleteEmailSuppressionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the suppression so Pylon resumes sending email to the address.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.email_suppressions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the email suppression to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FeatureRequests
<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">create</a>(...) -> CreateFeatureRequestResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new feature request. When should_auto_fetch_evidence is true, supporting evidence is automatically gathered and used to generate the description.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.create(
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the feature request.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the feature request. Ignored when should_auto_fetch_evidence is true, since the description is then generated from gathered evidence.
    
</dd>
</dl>

<dl>
<dd>

**should_auto_fetch_evidence:** `typing.Optional[bool]` — When true, asynchronously gathers supporting evidence and generates a description, mirroring the in-app experience. Defaults to false, which creates the feature request as-is.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">merge</a>(...) -> MergeFeatureRequestsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merges one or more feature requests into a surviving feature request. Evidence and linked external issues are consolidated, and merged feature requests are archived. Merge requests that share a target should be sent serially.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.merge(
    merge_feature_request_ids=[
        "merge_feature_request_ids"
    ],
    merge_into_feature_request_id="merge_into_feature_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merge_feature_request_ids:** `typing.List[str]` — The IDs of the Feature Requests to merge into the surviving Feature Request. Must contain between 1 and 100 unique IDs.
    
</dd>
</dl>

<dl>
<dd>

**merge_into_feature_request_id:** `str` — The ID of the Feature Request that will survive the merge.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">search</a>(...) -> SearchFeatureRequestsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns feature requests matching the given criteria. Supports semantic search, status filtering, and pagination.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_ids:** `typing.Optional[typing.List[str]]` — Filter by one or more account IDs. Returns only feature requests with evidence linked to any of the given accounts.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of feature requests to return. Defaults to 100, max 1000.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — A search query string for semantic and keyword matching. If omitted, all feature requests are returned (subject to other filters and limit).
    
</dd>
</dl>

<dl>
<dd>

**request_statuses:** `typing.Optional[typing.List[str]]` — Filter by one or more request statuses. Each value can be a built-in status (new, in_progress, closed, archived) or a custom status slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">get</a>(...) -> GetFeatureRequestResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single feature request by ID. Optionally includes evidence items when fetch_evidence is true.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the feature request to fetch.
    
</dd>
</dl>

<dl>
<dd>

**fetch_evidence:** `typing.Optional[bool]` — Whether to include evidence items in the response. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">delete</a>(...) -> DeleteFeatureRequestResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a feature request and its associated evidence.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the feature request to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">update</a>(...) -> UpdateFeatureRequestResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing feature request. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the feature request to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to set. Only passed-in fields will be modified.
    
</dd>
</dl>

<dl>
<dd>

**request_status:** `typing.Optional[str]` — The new request status. Can be a built-in status (new, in_progress, closed, archived) or a custom status slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">add_evidence</a>(...) -> CreateFeatureRequestEvidenceResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a manual evidence record linking a customer account to a feature request. Repeated requests create separate evidence records.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.add_evidence(
    feature_request_id="id",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feature_request_id:** `str` — The ID of the feature request.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The ID of the customer account to link to the feature request.
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — A summary explaining why this account is linked. Defaults to "Account manually linked via API."
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">link_external_issue</a>(...) -> LinkFeatureRequestExternalIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, links the external issue and creates a backlink to the feature request in the source system. To unlink it, set the operation field to "unlink". Repeating the same link request is a successful no-op.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.link_external_issue(
    feature_request_id="id",
    external_issue_id="external_issue_id",
    source="source",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feature_request_id:** `str` — The ID of the feature request to link an external issue to.
    
</dd>
</dl>

<dl>
<dd>

**external_issue_id:** `str` — The ID or human-readable key of the external issue in the source system.
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` — The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut").
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feature_requests.<a href="src/usepylon/feature_requests/client.py">set_portal_visibility</a>(...) -> SetFeatureRequestPortalVisibilityResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Toggles portal visibility for a set of accounts on a feature request. Idempotent — adding already-visible accounts or removing already-hidden accounts is a no-op. Note: visibility only takes effect when the Feature Requests tab is enabled in portal settings.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.feature_requests.set_portal_visibility(
    feature_request_id="id",
    account_ids=[
        "account_ids"
    ],
    visible=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feature_request_id:** `str` — The ID of the feature request.
    
</dd>
</dl>

<dl>
<dd>

**account_ids:** `typing.List[str]` — The account IDs to add or remove portal visibility for.
    
</dd>
</dl>

<dl>
<dd>

**visible:** `bool` — Whether the specified accounts should be able to see this feature request in the portal. True to add visibility, false to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IssueGroups
<details><summary><code>client.issue_groups.<a href="src/usepylon/issue_groups/client.py">create</a>(...) -> CreateIssueGroupResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an issue group and attaches its initial child issues atomically.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issue_groups.create(
    child_issue_ids=[
        "child_issue_ids"
    ],
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**child_issue_ids:** `typing.List[str]` — The IDs of the issues to include in the group. At least one is required.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the issue group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IssueStatuses
<details><summary><code>client.issue_statuses.<a href="src/usepylon/issue_statuses/client.py">list</a>() -> GetIssueStatusesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all issue statuses for the organization. Use `slug` as `state` in PATCH /issues and issue search filters.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issue_statuses.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues
<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">list</a>(...) -> GetIssuesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of issues created within a required time range (max 365 days). Results are sorted by created_at, newest first. To filter on updated_at or other timestamps, use POST /issues/search.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment
import datetime

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.list(
    start_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `datetime.datetime` — The start of the time range, filtering on the issue's created_at (inclusive). Use RFC3339 with Z or a URL-encoded offset (%2B). The duration between start_time and end_time must be less than or equal to 365 days.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `datetime.datetime` — The end of the time range, filtering on the issue's created_at (exclusive). Use RFC3339 with Z or a URL-encoded offset (%2B). The duration between start_time and end_time must be less than or equal to 365 days.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of issues to fetch. Defaults to 20000. Set to 0 or omit to use the default. Must be between 0 and 20000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">create</a>(...) -> CreateIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new issue and its first message. Requires either an account_id or requester information.

Requester fields identify the customer, user_id or contact_id identifies the first-message author, and destination_metadata controls delivery. These choices are independent. If destination_metadata is omitted, the first message is an internal note and no customer is contacted. See the request-field descriptions and examples for destination-specific requirements.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon, DestinationMetadata
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.create(
    body_html="<p>I cannot access my account.</p>",
    contact_id="contact_123",
    destination_metadata=DestinationMetadata(
        destination="in_app_chat",
    ),
    requester_id="contact_123",
    title="Unable to sign in",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body_html:** `str` — The HTML content of the body of the issue.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the issue.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The account that this issue belongs to. If requester_id is also provided, the requester must belong to this account. If requester_email is provided, the contact is found or created in this account.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — The user the issue should be assigned to.
    
</dd>
</dl>

<dl>
<dd>

**attachment_urls:** `typing.Optional[typing.List[str]]` — URLs of files to attach to the issue's first message.
    
</dd>
</dl>

<dl>
<dd>

**author_unverified:** `typing.Optional[bool]` — Whether the requester's identity has NOT been verified. Defaults to false (verified).
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The contact to attribute the first message to. This controls the message author, not the issue requester. Makes the message appear as a customer message rather than an internal note. Only one of user_id or contact_id can be provided. Requires destination_metadata.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — Timestamp of when the issue was created. If not specified, the current time will be used. (RFC3339)
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this issue.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Whether the issue should be visible in the customer portal. When destination is "customer_portal", this is set to true and cannot be false.
    
</dd>
</dl>

<dl>
<dd>

**destination_metadata:** `typing.Optional[DestinationMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[CreateIssueRequestPriority]` — The priority of the issue. Can be one of: urgent, high, medium, or low.
    
</dd>
</dl>

<dl>
<dd>

**requester_avatar_url:** `typing.Optional[str]` — The URL of an avatar of the requester.
    
</dd>
</dl>

<dl>
<dd>

**requester_email:** `typing.Optional[str]` — The email of the customer this issue is for. Used when requester_id is omitted. If no matching contact exists, one will be created. When account_id is provided, the contact is found or created in that account. This does not control who authored the first message.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — The customer this issue is for. Sets the "Requester" shown in the issue sidebar but does not control who authored the first message. If account_id is omitted, the requester's primary account is used when available. If requester_email is also provided, requester_id takes precedence.
    
</dd>
</dl>

<dl>
<dd>

**requester_name:** `typing.Optional[str]` — The optional full name of the requester. Used when creating a new contact via requester_email.
    
</dd>
</dl>

<dl>
<dd>

**requester_phone_number:** `typing.Optional[str]` — The phone number of a new requester. Only supported for direct WhatsApp delivery and cannot be combined with requester_id, requester_email, requester_name, or requester_avatar_url. The number is normalized to E.164 format and used to create a phone-only contact in the same transaction as the issue.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — An array of strings to use as tags on this issue. If provided, the issue tags will be updated to the given tags.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — The ID of the team this issue should be assigned to.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — The internal Pylon user to attribute the first message to. This does not assign the user as the requester. Only one of user_id or contact_id can be provided. If neither is set, the API token's user is used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">bulk_update</a>(...) -> UpdateIssuesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies the same changes to up to 100 issues. Only provided fields are modified. Issues that do not exist, or that the caller cannot update, are skipped and listed in skipped_issues instead of failing the request.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.bulk_update(
    issue_ids=[
        "issue_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_ids:** `typing.List[str]` — The IDs of the issues to update. Must contain between 1 and 100 IDs.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — The ID of the user to assign the issues to. If empty string is passed in, the issues will be unassigned.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — Custom fields to set on the issues. Only passed in fields are modified. Clearing a custom field is not supported in bulk; use PATCH /issues/{id}.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Whether the issues should be visible in the customer portal.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — The state to move the issues to. Standard values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Tags to apply to the issues, according to tags_apply_mode.
    
</dd>
</dl>

<dl>
<dd>

**tags_apply_mode:** `typing.Optional[UpdateIssuesRequestTagsApplyMode]` — The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace".
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — The ID of the team to assign the issues to. If empty string is passed in, the team will be removed. Team assignment is applied asynchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">mark_spam</a>(...) -> MarkIssuesAsSpamResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks up to 100 email issues as spam. Each issue is deleted, and the sender's email address is blocked unless it belongs to your own domains or support inboxes. If an issue's account has no issues left afterwards, the account is deleted too. Issues from other sources are skipped with reason unsupported_source. Issues that do not exist, or that the caller cannot mark as spam, are skipped and listed in skipped_issues instead of failing the request.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.mark_spam(
    issue_ids=[
        "issue_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_ids:** `typing.List[str]` — The IDs of the issues to mark as spam. Must contain between 1 and 100 IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">merge</a>(...) -> MergeIssuesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merges one or more issues into a primary issue. All issues must belong to the same account (or, without an account, the same requester). All issues are found and validated before anything changes, so a request rejected for a missing or ineligible issue merges nothing. Closing messages are sent before the merge and are not recalled: if sending one fails, or the merge fails afterwards, duplicates processed earlier may already have received it. This cannot be undone.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.merge(
    duplicate_issue_ids=[
        "duplicate_issue_ids"
    ],
    primary_issue_id="primary_issue_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**duplicate_issue_ids:** `typing.List[str]` — The IDs or numbers of the issues to merge into the primary issue. Must contain between 1 and 50 issues, all in the same account as the primary issue.
    
</dd>
</dl>

<dl>
<dd>

**primary_issue_id:** `str` — The ID or number of the issue to merge into. It keeps its ID and receives the messages of the merged issues.
    
</dd>
</dl>

<dl>
<dd>

**closing_message:** `typing.Optional[str]` — Optional plain-text message sent to the customer on each merged Slack or form issue before it is merged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">search</a>(...) -> SearchIssuesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `customer_portal_visible` | `equals`, `in`, `not_in` |
 `ticket_form_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `requester_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `follower_user_id` | `equals`, `in`, `not_in` |
 `follower_contact_id` | `equals`, `in`, `not_in` |
 `state` | `equals`, `in`, `not_in` |
 `tags` | `contains`, `does_not_contain`, `in`, `not_in` |
 `title` | `string_contains`, `string_does_not_contain` |
 `body_html` | `string_contains`, `string_does_not_contain` |
 `assignee_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `team_id` | `equals`, `in`, `not_in` |
 `issue_type` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `issue_is_issue_group` | `equals`, `in`, `not_in` |
 `resolved_at` | `time_is_after`, `time_is_before`, `time_range` |
 `latest_message_activity_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |
 `slack_channel_id` | `equals`, `in`, `not_in` |
 `workspace_email` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `reopened` | `equals`, `in`, `not_in` |

Timestamp values use RFC3339 format. Standard `state` values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported. `issue_type` values are `conversation` and `ticket`.

For tag filters, pass the tag name. For custom fields, pass the field slug as `field`. `slack_channel_id` identifies the Slack channel where the issue was created. `workspace_email` identifies the email address connected to the Pylon workspace through which the issue's email conversation is routed. `customer_portal_visible` values are `true` and `false`; issue groups are never visible in the customer portal, so they always match `false`. `reopened` values are `true` and `false`; it is a sticky flag set the first time an issue is reopened after being resolved, and it records no timestamp.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon, Filter
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.search(
    filter=Filter(
        field="state",
        operator="equals",
        value="new",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of issues to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Fuzzy text search. Results are intersected with any provided filter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">get</a>(...) -> GetIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single issue by ID or issue number.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID or number of the issue to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">delete</a>(...) -> DeleteIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an issue by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the issue to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">update</a>(...) -> UpdateIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing issue. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the issue to update.
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — The ID of the account that this issue belongs to. To remove the account, pass an empty string and also provide requester_id. The requester can be cleared with an empty string or retained if it has no account memberships. Account removal is supported only for manual, form, and email issues.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — The ID of the user who should be assigned to this issue. If empty string is passed in, the issue assignee will be removed.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this issue. Only passed in fields will be modified.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Whether the issue should be visible in the customer portal.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — The ID of the requester that this issue is on behalf of. If an empty string is passed, the requester will be removed. This field must be provided when removing the issue's account, and a retained requester must not belong to any account.
    
</dd>
</dl>

<dl>
<dd>

**requestor_id:** `typing.Optional[str]` — Deprecated: Use requester_id instead.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — The state this issue should be moved to. Standard values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — An array of strings to use as tags on this issue. If provided, the issue tags will be updated to be exactly the given tags.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — The ID of the team this issue should be assigned to. If empty string is passed in, any assigned team will be removed.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the issue.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateIssueRequestBodyType]` — The type of the issue. Set to "ticket" to upgrade a conversation to a support ticket. Cannot be downgraded from "ticket" to "conversation".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">create_ai_response</a>(...) -> CreateIssueAiResponseResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates an AI response for the specified issue using the given agent.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.create_ai_response(
    issue_id="id",
    ai_agent_id="ai_agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to create an AI response for.
    
</dd>
</dl>

<dl>
<dd>

**ai_agent_id:** `str` — The ID of the AI agent to use to create the AI response.
    
</dd>
</dl>

<dl>
<dd>

**post_as_internal_note:** `typing.Optional[bool]` — Whether to post the AI response as an internal note on the issue.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">create_draft_reply</a>(...) -> CreateIssueDraftReplyResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a private customer-reply draft without sending it. The draft is visible only to its owner and may require a normal issue refetch before appearing in the app. For unlinked or service API tokens, user_id is required. This endpoint updates only untouched drafts that it previously created; every other existing draft returns a conflict.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.create_draft_reply(
    issue_id="id",
    body_html="body_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The draft body in HTML.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — The active Pylon user who should own and see the draft. Defaults to the API-token user when it is a human Pylon user; required for unlinked or service API tokens.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">link_external_incident</a>(...) -> LinkExternalIncidentResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links an incident from one of the organization's connected incident systems (incident.io or Rootly). An issue can have several linked incidents, and linking one that is already linked has no effect. To unlink, set the operation field to "unlink".

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.link_external_incident(
    issue_id="id",
    incident_id="incident_id",
    source="incident_io",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to link the incident to.
    
</dd>
</dl>

<dl>
<dd>

**incident_id:** `str` — The incident's reference (such as INC-123 or ROOT-123) or its ID in the incident system.
    
</dd>
</dl>

<dl>
<dd>

**source:** `LinkExternalIncidentRequestBodySource` 

The incident system the incident belongs to. It must be connected to the organization.
Valid values: "incident_io", "rootly"
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "link" to link the incident (default) or "unlink" to unlink it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">link_external_issue</a>(...) -> LinkExternalIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, links external issues. To unlink issues, set the operation field to "unlink".

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.link_external_issue(
    issue_id="id",
    external_issue_id="external_issue_id",
    source="source",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to link external issues to.
    
</dd>
</dl>

<dl>
<dd>

**external_issue_id:** `str` — The ID of the external issue in the source system.
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` — The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut").
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "link" to link issues (default) or "unlink" to unlink issues.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">create_note</a>(...) -> CreateIssueNoteResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Posts an internal note on an issue thread. Not visible to the requester.

Thread selection:
* If thread_id is provided, posts to that internal thread.
* If message_id is provided, posts to the thread containing that internal note.
* Providing both thread_id and message_id returns a 400 response.
* If neither is provided, posts to the most recently created Slack-backed internal thread. If none exists, creates a Pylon-only internal thread.
* thread_name names that newly created Pylon-only thread and is otherwise ignored.

Empty thread_id, message_id, and thread_name values are treated as omitted.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.create_note(
    issue_id="id",
    body_html="body_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The body of the message in HTML.
    
</dd>
</dl>

<dl>
<dd>

**attachment_urls:** `typing.Optional[typing.List[str]]` — URLs of files to attach to this internal note.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — The ID of an internal note whose thread should receive the new note. Use the top-level `id` from GET /issues/{id}/messages. Cannot be combined with thread_id.
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — The ID of the internal thread to post the note to. Use the `id` field (not `thread_id`) from GET /issues/{id}/threads. Cannot be combined with message_id.
    
</dd>
</dl>

<dl>
<dd>

**thread_name:** `typing.Optional[str]` — Optional name for a new Pylon-only internal thread. Used only when neither thread_id nor message_id is provided and no Slack-backed internal thread exists.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Optional user ID to post the message as. If not provided, the API token user will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">reply</a>(...) -> CreateIssueReplyResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a customer-facing reply on an issue, visible to the requester.

message_id is required to identify which existing customer-visible conversation or thread to continue. Use the top-level message id returned by GET /issues/{id}/messages; do not use an external provider's message ID or the nested email_info.message_id value.

For an email conversation, email_info must contain at least one recipient across to_emails, cc_emails, and bcc_emails. The referenced message controls email threading, but its recipients are not copied automatically.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.reply(
    issue_id="id",
    body_html="body_html",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The body of the message in HTML.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The top-level Pylon message ID to reply to, from the `id` field returned by GET /issues/{id}/messages. The message must belong to the issue in the request path and must be customer-visible, not an internal note. This selects the external conversation or thread where the reply is delivered. For email, it also sets the In-Reply-To and References chain. Do not use a provider-specific message ID or email_info.message_id.
    
</dd>
</dl>

<dl>
<dd>

**attachment_urls:** `typing.Optional[typing.List[str]]` — URLs of files to attach to this reply.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — Optional contact ID to post the message as. Only one of user_id or contact_id can be provided.
    
</dd>
</dl>

<dl>
<dd>

**custom_source:** `typing.Optional[CustomSourceInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**email_info:** `typing.Optional[CreateIssueReplyEmailInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Optional user ID to post the message as. Only one of user_id or contact_id can be provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/usepylon/issues/client.py">snooze</a>(...) -> SnoozeIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Snoozes an issue until the specified date and time.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment
import datetime

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.snooze(
    issue_id="id",
    snooze_until=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to snooze.
    
</dd>
</dl>

<dl>
<dd>

**snooze_until:** `datetime.datetime` — The date and time to snooze the issue until. (RFC3339)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases
<details><summary><code>client.knowledge_bases.<a href="src/usepylon/knowledge_bases/client.py">list</a>() -> GetKnowledgeBasesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all knowledge bases for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.<a href="src/usepylon/knowledge_bases/client.py">get</a>(...) -> GetKnowledgeBaseResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single knowledge base by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MacroGroups
<details><summary><code>client.macro_groups.<a href="src/usepylon/macro_groups/client.py">list</a>() -> GetMacroGroupsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all macro groups for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macro_groups.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Macros
<details><summary><code>client.macros.<a href="src/usepylon/macros/client.py">list</a>(...) -> GetMacrosResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all macros for the organization. Optionally filter by macro group ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macros.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**macro_group_id:** `typing.Optional[str]` — Filter macros by macro group ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.macros.<a href="src/usepylon/macros/client.py">create</a>(...) -> CreateMacroResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new macro within the specified macro group.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macros.create(
    macro_group_id="macro_group_id",
    name="name",
    text_html="text_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**macro_group_id:** `str` — The ID of the macro group this macro belongs to.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the macro.
    
</dd>
</dl>

<dl>
<dd>

**text_html:** `str` — The HTML content of the macro.
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**edit_visibility:** `typing.Optional[VisibilityInput]` 
    
</dd>
</dl>

<dl>
<dd>

**text_type:** `typing.Optional[str]` — The type of text: "reply", "note", or "email". Defaults to "reply".
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[VisibilityInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.macros.<a href="src/usepylon/macros/client.py">get</a>(...) -> GetMacroResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single macro by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macros.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the macro.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.macros.<a href="src/usepylon/macros/client.py">delete</a>(...) -> DeleteMacroResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a macro by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macros.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the macro to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.macros.<a href="src/usepylon/macros/client.py">update</a>(...) -> UpdateMacroResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing macro by ID. All fields are optional; only provided fields will be updated.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.macros.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the macro to update.
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**edit_visibility:** `typing.Optional[VisibilityInput]` 
    
</dd>
</dl>

<dl>
<dd>

**macro_group_id:** `typing.Optional[str]` — The ID of the macro group this macro belongs to.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the macro.
    
</dd>
</dl>

<dl>
<dd>

**text_html:** `typing.Optional[str]` — The HTML content of the macro.
    
</dd>
</dl>

<dl>
<dd>

**text_type:** `typing.Optional[str]` — The type of text: "reply", "note", or "email".
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[VisibilityInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Me
<details><summary><code>client.me.<a href="src/usepylon/me/client.py">get</a>() -> GetMeResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the organization and user associated with the credentials used for authentication.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.me.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Milestones
<details><summary><code>client.milestones.<a href="src/usepylon/milestones/client.py">create</a>(...) -> CreateMilestoneResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new milestone within a project.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.milestones.create(
    name="name",
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name for this milestone
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project ID for this milestone
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — Account ID for this project
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[datetime.datetime]` — Due date for this milestone, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.milestones.<a href="src/usepylon/milestones/client.py">search</a>(...) -> SearchMilestonesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `project_id` | `equals`, `in`, `not_in` |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `due_date` | `time_is_after`, `time_is_before`, `time_range`, `is_set`, `is_unset` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |
 `started_at` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |
 `completed_at` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |

Timestamp values use RFC3339 format. Milestones belonging to an unlaunched project are not returned.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.milestones.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of milestones to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.milestones.<a href="src/usepylon/milestones/client.py">get</a>(...) -> GetMilestoneResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single milestone by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.milestones.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the milestone to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.milestones.<a href="src/usepylon/milestones/client.py">delete</a>(...) -> DeleteMilestoneResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a milestone by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.milestones.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the milestone to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.milestones.<a href="src/usepylon/milestones/client.py">update</a>(...) -> UpdateMilestoneResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing milestone. Only provided fields are modified.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.milestones.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the milestone to update.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — Due date for this milestone, in RFC 3339 format. Set to an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for this milestone
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/usepylon/projects/client.py">create</a>(...) -> CreateProjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new project for an account. Provide a name or project_template_id. A template supplies defaults; non-empty name and description_html values and supplied customer_portal_visible and owner_id values override them. Supplying either start_date or end_date replaces both template dates.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.projects.create(
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — Account ID for this project
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Customer portal visible for this project
    
</dd>
</dl>

<dl>
<dd>

**description_html:** `typing.Optional[str]` — Description HTML for this project
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — End date for this project, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for this project. Required unless project_template_id is provided. When both are provided, this name overrides the template's name.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — Owner ID for this project
    
</dd>
</dl>

<dl>
<dd>

**project_template_id:** `typing.Optional[str]` — Project template ID for this project. When provided, it supplies defaults; non-empty name and description_html values and supplied customer_portal_visible and owner_id values override them. Supplying either start_date or end_date replaces both template dates.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Start date for this project, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/usepylon/projects/client.py">search</a>(...) -> SearchProjectsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set` |
 `status` | `equals`, `in`, `not_in` |
 `owner_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `is_archived` | `equals` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

Timestamp values use RFC3339 format. Valid `status` values are `not_started`, `in_progress`, and `completed`. For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.projects.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of projects to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/usepylon/projects/client.py">get</a>(...) -> GetProjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single project by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.projects.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the project to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/usepylon/projects/client.py">delete</a>(...) -> DeleteProjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a project by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.projects.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the project to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/usepylon/projects/client.py">update</a>(...) -> UpdateProjectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing project. Only provided fields are modified.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.projects.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the project to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this project. Only passed in fields will be modified.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Customer portal visible for this project
    
</dd>
</dl>

<dl>
<dd>

**description_html:** `typing.Optional[str]` — Description HTML for this project
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date for this project, in RFC 3339 format. Set to an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Whether the project is archived
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for this project
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — Owner ID for this project
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date for this project, in RFC 3339 format. Set to an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Surveys
<details><summary><code>client.surveys.<a href="src/usepylon/surveys/client.py">list</a>() -> GetSurveysResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all surveys for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.surveys.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.surveys.<a href="src/usepylon/surveys/client.py">search</a>(...) -> SearchSurveysResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

Timestamp values use RFC3339 format.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.surveys.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of surveys to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.surveys.<a href="src/usepylon/surveys/client.py">get</a>(...) -> GetSurveyResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single survey by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.surveys.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">list</a>() -> GetTagsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all tags for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">create</a>(...) -> CreateTagResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new tag with the specified value and object type.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.create(
    object_type="account",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `CreateTagRequestBodyObjectType` — The object type of the associated object. Can be "account", "article", or "issue".
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The tag value.
    
</dd>
</dl>

<dl>
<dd>

**hex_color:** `typing.Optional[str]` — The hex code of the tag's color.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">search</a>(...) -> SearchTagsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns tags the caller can read, newest first, optionally narrowed to one object type and to values containing search_text.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of tags to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[SearchTagsRequestObjectType]` — Only return tags of this object type. Omit to search every type the caller can read.
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Only return tags whose value contains this text. Spaces, hyphens, and underscores match each other.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">get</a>(...) -> GetTagResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single tag by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">delete</a>(...) -> DeleteTagResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a tag by ID.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the tag to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/usepylon/tags/client.py">update</a>(...) -> UpdateTagResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing tag. Only provided fields are modified.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tags.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the tag to update.
    
</dd>
</dl>

<dl>
<dd>

**hex_color:** `typing.Optional[str]` — The hex code of the tag's color.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 

in: body
The name of the tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TaskStatuses
<details><summary><code>client.task_statuses.<a href="src/usepylon/task_statuses/client.py">list</a>() -> GetTaskStatusesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all task statuses for the organization.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.task_statuses.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks
<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">list</a>(...) -> GetTasksResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of tasks for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of tasks to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">create</a>(...) -> CreateTaskResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new task with a title and optional metadata.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.create(
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — Title for this task
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — Account ID for this task
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — Assignee ID for this task
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `typing.Optional[str]` — Body HTML for this task
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this task.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Customer portal visible for this task
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[datetime.datetime]` — Due date for this task, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**milestone_id:** `typing.Optional[str]` — Milestone ID for this task
    
</dd>
</dl>

<dl>
<dd>

**parent_task_id:** `typing.Optional[str]` — Parent task ID, to create this task as a subtask
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Project ID for this task
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">search</a>(...) -> SearchTasksResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set` |
 `project_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `status` | `equals`, `in`, `not_in` |
 `assignee_id` | `equals`, `in`, `not_in`, `is_set` |
 `milestone_id` | `equals`, `in`, `not_in`, `is_set` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `due_date` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

Timestamp values use RFC3339 format. Valid `status` values are `not_started`, `in_progress`, and `completed`. For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of tasks to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">get</a>(...) -> GetTaskResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single task by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the task to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">delete</a>(...) -> DeleteTaskResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a task by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the task to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">update</a>(...) -> UpdateTaskResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing task. Only provided fields are modified.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the task to update.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — Assignee ID for this task
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `typing.Optional[str]` — Body HTML for this task
    
</dd>
</dl>

<dl>
<dd>

**completed_at:** `typing.Optional[datetime.datetime]` — Completed at time for this task, in RFC 3339 format. The task must already have a completed status and completion date.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.List[CustomFieldValue]]` — An array of custom fields to be used on this task. Only passed in fields will be modified.
    
</dd>
</dl>

<dl>
<dd>

**customer_portal_visible:** `typing.Optional[bool]` — Customer portal visible for this task
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — Due date for this task, in RFC 3339 format. Set to an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**milestone_id:** `typing.Optional[str]` — Milestone ID for this task
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Project ID for this task
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title for this task
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">link_external_issue</a>(...) -> LinkTaskExternalIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, links the external issue. To unlink it, set the operation field to "unlink". Repeating the same link request is a successful no-op.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.link_external_issue(
    task_id="id",
    external_issue_id="external_issue_id",
    source="source",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task to link an external issue to.
    
</dd>
</dl>

<dl>
<dd>

**external_issue_id:** `str` — The ID or human-readable key of the external issue in the source system.
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` — The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut").
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/usepylon/tasks/client.py">link_issue</a>(...) -> LinkTaskIssueResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links the issue to the task by default. To unlink it, set the operation field to "unlink".

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.link_issue(
    task_id="id",
    issue_id="issue_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task to link a Pylon issue to.
    
</dd>
</dl>

<dl>
<dd>

**issue_id:** `str` — The ID of the Pylon issue.
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.teams.<a href="src/usepylon/teams/client.py">list</a>() -> GetTeamsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all teams for the organization, each with how it assigns issues and its recurring
assignment schedule if it has one.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.teams.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/usepylon/teams/client.py">create</a>(...) -> CreateTeamResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new team with a name and optional member list. Optionally sets how the team
assigns issues and creates its recurring assignment schedule in the same call.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.teams.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the team.
    
</dd>
</dl>

<dl>
<dd>

**assignment_configuration:** `typing.Optional[TeamAssignmentConfigurationInput]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TeamScheduleInput]` 
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.List[str]]` — The list of user IDs to add to the team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/usepylon/teams/client.py">get</a>(...) -> GetTeamResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single team by ID, with how it assigns issues and its recurring assignment
schedule if it has one.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.teams.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the team to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/usepylon/teams/client.py">update</a>(...) -> UpdateTeamResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing team, including how it assigns issues and its recurring assignment
schedule. Only provided fields are modified; supplying schedule.blocks replaces the whole
rotation, and omitting it leaves the rotation unchanged.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.teams.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the team to update.
    
</dd>
</dl>

<dl>
<dd>

**assignment_configuration:** `typing.Optional[TeamAssignmentConfigurationInput]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the team.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TeamScheduleInput]` 
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.List[str]]` — The list of user IDs to add to the team. If provided, the team members will be updated to be exactly the given users.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TicketForms
<details><summary><code>client.ticket_forms.<a href="src/usepylon/ticket_forms/client.py">list</a>() -> GetTicketFormsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all ticket forms for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.ticket_forms.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_forms.<a href="src/usepylon/ticket_forms/client.py">get</a>(...) -> GetTicketFormResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single ticket form by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.ticket_forms.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the ticket form to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_forms.<a href="src/usepylon/ticket_forms/client.py">submit</a>(...) -> SubmitTicketFormResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an issue from a configured ticket form. Provide either requester_id or both requester_email and requester_name. Field types are inferred from the ticket form; use value for single-value fields and values for multi-value and file-upload fields.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.ticket_forms.submit(
    ticket_form_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_form_id:** `str` — The ID of the ticket form to submit.
    
</dd>
</dl>

<dl>
<dd>

**attachment_urls:** `typing.Optional[typing.List[str]]` — HTTPS URLs to attach to the initial ticket message. URLs are copied into durable Pylon storage before the submission is persisted.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.List[SubmitTicketFormField]]` — The submitted ticket form fields. Use the slugs returned by GET /ticket-forms/{id}, excluding name and email, which are supplied through the requester fields above.
    
</dd>
</dl>

<dl>
<dd>

**requester_email:** `typing.Optional[str]` — The requester's email address. Must be provided with requester_name and cannot be combined with requester_id.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — The ID of an existing contact to use as the requester. Provide either requester_id or both requester_email and requester_name.
    
</dd>
</dl>

<dl>
<dd>

**requester_name:** `typing.Optional[str]` — The requester's full name. Must be provided with requester_email and cannot be combined with requester_id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TrainingData
<details><summary><code>client.training_data.<a href="src/usepylon/training_data/client.py">list</a>() -> ListTrainingDataResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all training data configurations for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.training_data.<a href="src/usepylon/training_data/client.py">create</a>(...) -> CreateTrainingDataResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new training data configuration for the organization.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**training_data_name:** `typing.Optional[str]` — The name of the training data container.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[CreateTrainingDataRequestBodyVisibility]` 

The visibility of the training data. Defaults to "everyone".
Valid values: "everyone", "user_only", "ai_agent_only"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.training_data.<a href="src/usepylon/training_data/client.py">upload_files</a>(...) -> TrainingDataUploadResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads one or more files to a training data configuration.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.upload_files(
    files=[
        "files"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**files:** `typing.List[str]` 

The files to upload (minimum 1, maximum 10).
Supported types: PDF, plain text, markdown, CSV, JSON, and images (JPEG, PNG, GIF, WebP).
Maximum size: 50MB per file, 100MB total.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.List[str]]` 

External IDs for idempotent operations. Must match the number of files if provided.
Used for duplicate detection and updates.
    
</dd>
</dl>

<dl>
<dd>

**file_names:** `typing.Optional[typing.List[str]]` 

Custom names for the uploaded files. Must match the number of files if provided.
If not provided, original filenames will be used.
    
</dd>
</dl>

<dl>
<dd>

**training_data_id:** `typing.Optional[str]` 

The ID of an existing training data container to upload files to.
Required if not creating new training data.
    
</dd>
</dl>

<dl>
<dd>

**training_data_name:** `typing.Optional[str]` 

The name of a new training data container.
Required when creating new training data (if training_data_id is not provided).
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[UploadFilesTrainingDataRequestVisibility]` 

Visibility of the training data. Defaults to "everyone".
Valid values: "everyone", "user_only", "ai_agent_only"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.training_data.<a href="src/usepylon/training_data/client.py">upload_content</a>(...) -> TrainingDataUploadResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads plain text content as a training data document.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.upload_content()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content:** `typing.Optional[str]` — The text content to upload.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — External ID for idempotent operations (optional).
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` — The name for the uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**training_data_id:** `typing.Optional[str]` — The ID of an existing training data container to upload to (optional).
    
</dd>
</dl>

<dl>
<dd>

**training_data_name:** `typing.Optional[str]` — The name of a new training data container (required if training_data_id not provided).
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[UploadTrainingDataFileContentRequestBodyVisibility]` — Visibility of the training data. Defaults to "everyone".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.training_data.<a href="src/usepylon/training_data/client.py">get</a>(...) -> GetTrainingDataResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single training data configuration by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the training data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserRoles
<details><summary><code>client.user_roles.<a href="src/usepylon/user_roles/client.py">list</a>() -> GetUserRolesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all user roles for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.user_roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/usepylon/users/client.py">list</a>(...) -> GetUsersResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all users for the organization.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.users.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_deactivated:** `typing.Optional[bool]` — Whether to include deactivated users. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/usepylon/users/client.py">search</a>(...) -> SearchUsersResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `email` | `equals`, `in`, `not_in` |

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.users.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of users to fetch. Defaults to 100. Must be between 1 and 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/usepylon/users/client.py">get</a>(...) -> GetUserResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single user by ID.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.users.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/usepylon/users/client.py">update</a>(...) -> GetUserResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing user. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.users.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user to update.
    
</dd>
</dl>

<dl>
<dd>

**avatar_url:** `typing.Optional[str]` — The avatar URL of the user. Must be a square .png, .jpg or .jpeg.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the user.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — The role_id of the user.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateUserRequestBodyStatus]` — The new user status for the user. Can be one of `active`, `away`, or `out_of_office`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts Highlights
<details><summary><code>client.accounts.highlights.<a href="src/usepylon/accounts/highlights/client.py">create</a>(...) -> CreateAccountHighlightResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new highlight on an account.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.highlights.create(
    account_id="account_id",
    content_html="content_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account that the highlight belongs to.
    
</dd>
</dl>

<dl>
<dd>

**content_html:** `str` — The HTML content for this highlight.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — Optional ID or external ID of a contact to associate the resulting memory with. The contact must belong to the account.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — Optional RFC3339 timestamp of when this highlight will expire.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.highlights.<a href="src/usepylon/accounts/highlights/client.py">delete</a>(...) -> DeleteAccountHighlightResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an account highlight by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.highlights.delete(
    account_id="account_id",
    highlight_id="highlight_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account that the highlight belongs to.
    
</dd>
</dl>

<dl>
<dd>

**highlight_id:** `str` — The ID of the highlight to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.highlights.<a href="src/usepylon/accounts/highlights/client.py">update</a>(...) -> UpdateAccountHighlightResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing account highlight. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.highlights.update(
    account_id="account_id",
    highlight_id="highlight_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account that the highlight belongs to.
    
</dd>
</dl>

<dl>
<dd>

**highlight_id:** `str` — The ID of the highlight to update.
    
</dd>
</dl>

<dl>
<dd>

**content_html:** `typing.Optional[str]` — The updated HTML content for this highlight.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` — The updated expires at timestamp (RFC3339). Omit it to keep the current expiry, or set it to an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts Relationships
<details><summary><code>client.accounts.relationships.<a href="src/usepylon/accounts/relationships/client.py">create</a>(...) -> CreateAccountRelationshipResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a parent or partner relationship for the account in the URL.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.relationships.create(
    account_id="account_id",
    related_object_id="related_object_id",
    relationship_type="relationship_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the child or client account.
    
</dd>
</dl>

<dl>
<dd>

**related_object_id:** `str` — The ID of the related parent or partner account.
    
</dd>
</dl>

<dl>
<dd>

**relationship_type:** `str` — The relationship type. Must be "parent_account" or "partner_account".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.relationships.<a href="src/usepylon/accounts/relationships/client.py">list</a>(...) -> GetAccountRelationshipsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the parent-child and partner-client relationships where the account is the child or client.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.relationships.list(
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the child or client account whose relationships should be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.relationships.<a href="src/usepylon/accounts/relationships/client.py">delete</a>(...) -> DeleteAccountRelationshipResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an account relationship by ID.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.relationships.delete(
    account_id="account_id",
    relationship_id="relationship_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the child or client account.
    
</dd>
</dl>

<dl>
<dd>

**relationship_id:** `str` — The ID of the account relationship to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts Activities
<details><summary><code>client.accounts.activities.<a href="src/usepylon/accounts/activities/client.py">list</a>(...) -> GetActivitiesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns custom activities for the specified account, ordered from newest to oldest.
The {id} parameter accepts either:
Internal account ID (UUID format)
External ID (any string format)

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.activities.list(
    account_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account to fetch activities for.
    
</dd>
</dl>

<dl>
<dd>

**activity_type:** `typing.Optional[str]` — The custom activity type slug to filter by.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — The start time (RFC3339) of the activity time range.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end time (RFC3339) of the activity time range.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of activities to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.activities.<a href="src/usepylon/accounts/activities/client.py">create</a>(...) -> CreateActivityResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The {id} parameter accepts either:
Internal account ID (UUID format)
External ID (any string format)

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.activities.create(
    account_id="id",
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account to create the activity for.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `str` — The slug of the activity to create.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `typing.Optional[str]` — Optional HTML content to display in the activity.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — Optional contact ID of the actor of the activity.
    
</dd>
</dl>

<dl>
<dd>

**happened_at:** `typing.Optional[datetime.datetime]` — Timestamp (RFC3339) of when the activity happened. Defaults to the current time if empty.
    
</dd>
</dl>

<dl>
<dd>

**link:** `typing.Optional[str]` — Optional link to add to the activity.
    
</dd>
</dl>

<dl>
<dd>

**link_text:** `typing.Optional[str]` — Optional link text to display on the activity. Defaults to "Open link" if not provided. Applies only if a link is provided.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Optional user ID of the actor of the activity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts NotebookBlocks Notes
<details><summary><code>client.accounts.notebook_blocks.notes.<a href="src/usepylon/accounts/notebook_blocks/notes/client.py">list</a>(...) -> GetAccountNotebookNotesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns notes from a specific Notes block in an account notebook.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.notebook_blocks.notes.list(
    account_id="account_id",
    block_id="block_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account.
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` — The ID of the Notes block, copied from the notebook UI.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of notes to fetch. Defaults to 20. Must be greater than 0 and less than or equal to 20.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.notebook_blocks.notes.<a href="src/usepylon/accounts/notebook_blocks/notes/client.py">create</a>(...) -> CreateAccountNotebookNoteResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a note in a specific Notes block in an account notebook.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.accounts.notebook_blocks.notes.create(
    account_id="account_id",
    block_id="block_id",
    content_html="content_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID or external ID of the account.
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` — The ID of the Notes block, copied from the notebook UI.
    
</dd>
</dl>

<dl>
<dd>

**content_html:** `str` — The note body as HTML.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — An optional title for the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomFields SelectOptions
<details><summary><code>client.custom_fields.select_options.<a href="src/usepylon/custom_fields/select_options/client.py">create</a>(...) -> CreateCustomFieldSelectOptionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an option to a select or multiselect custom field.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.select_options.create(
    custom_field_id="id",
    label="label",
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_field_id:** `str` — The ID of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The display label of the option.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `str` — The API slug stored as the option value.
    
</dd>
</dl>

<dl>
<dd>

**ai_description:** `typing.Optional[str]` — The AI description used to help AI-enabled fields select this option.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_fields.select_options.<a href="src/usepylon/custom_fields/select_options/client.py">delete</a>(...) -> DeleteCustomFieldSelectOptionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an option and asynchronously clears it from affected objects.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.select_options.delete(
    custom_field_id="id",
    current_slug="current_slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_field_id:** `str` — The ID of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**current_slug:** `str` — The current option slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_fields.select_options.<a href="src/usepylon/custom_fields/select_options/client.py">update</a>(...) -> UpdateCustomFieldSelectOptionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an option's slug, label, or AI description. Slug changes preserve existing values and migrate persisted filters.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.custom_fields.select_options.update(
    custom_field_id="id",
    current_slug="current_slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_field_id:** `str` — The ID of the custom field.
    
</dd>
</dl>

<dl>
<dd>

**current_slug:** `str` — The current option slug.
    
</dd>
</dl>

<dl>
<dd>

**ai_description:** `typing.Optional[str]` — A replacement AI description. Pass an empty string to clear it.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — A replacement display label.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — A replacement API slug. Existing object values and persisted filters are migrated to this slug.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IssueGroups Children
<details><summary><code>client.issue_groups.children.<a href="src/usepylon/issue_groups/children/client.py">add</a>(...) -> IssueGroupMutationResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one or more child issues atomically. Issues already attached to this group are ignored.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issue_groups.children.add(
    issue_group_id="issue_group_id",
    child_issue_ids=[
        "child_issue_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_group_id:** `str` — The ID of the issue group.
    
</dd>
</dl>

<dl>
<dd>

**child_issue_ids:** `typing.List[str]` — The IDs of the issues to add to the group. At least one is required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issue_groups.children.<a href="src/usepylon/issue_groups/children/client.py">remove</a>(...) -> IssueGroupMutationResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one child issue. An issue group must retain at least one child.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issue_groups.children.remove(
    issue_group_id="issue_group_id",
    child_issue_id="child_issue_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_group_id:** `str` — The ID of the issue group.
    
</dd>
</dl>

<dl>
<dd>

**child_issue_id:** `str` — The ID of the child issue to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues Followers
<details><summary><code>client.issues.followers.<a href="src/usepylon/issues/followers/client.py">list</a>(...) -> GetIssueFollowersResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of followers for the specified issue.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.followers.list(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to get followers for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.followers.<a href="src/usepylon/issues/followers/client.py">add</a>(...) -> AddIssueFollowersResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

By default, adds followers. To remove followers, set the operation field to "remove".

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.followers.add(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue to add followers to.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.List[str]]` — The IDs of contacts to add as followers.
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — Operation to perform. Use "add" to add followers (default) or "remove" to remove followers.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.List[str]]` — The IDs of users to add as followers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues Messages
<details><summary><code>client.issues.messages.<a href="src/usepylon/issues/messages/client.py">list</a>(...) -> GetIssueMessagesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns messages for the specified issue, including replies and internal notes, ordered from oldest to newest.

To post a reply, use the message's top-level id—not thread_id or email_info.message_id. To post an internal note, use an internal thread's thread_id or an internal note's top-level id. Omit both limit and cursor to return all messages; when cursor is provided without limit, the page size defaults to 100.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.messages.list(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue to fetch messages for.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of messages to fetch. Must be greater than 0 and at most 1000. If omitted, all messages are returned for backward compatibility.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.messages.<a href="src/usepylon/issues/messages/client.py">delete</a>(...) -> DeleteMessageResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a message from an issue and its connected external system.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.messages.delete(
    issue_id="id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue that the message belongs to.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The ID of the message to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.messages.<a href="src/usepylon/issues/messages/client.py">update</a>(...) -> UpdateMessageResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the body of a message and syncs the edit to its connected channel (Slack, Microsoft Teams, Discord, Google Chat, Telegram, or the chat widget).
Only messages authored by the API token's user can be edited. Emails, customer messages, and redacted messages cannot be edited.
Callers without issue write access can edit only their own internal notes.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.messages.update(
    issue_id="id",
    message_id="message_id",
    body_html="body_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue that the message belongs to.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The ID of the message to edit.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The new message body in HTML. Replaces the existing body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.messages.<a href="src/usepylon/issues/messages/client.py">redact</a>(...) -> RedactMessageResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently replaces a message's stored content with redacted_body_message and optionally deletes its attachments. This action cannot be undone.
When omitted, redacted_body_message defaults to "This message has been redacted." and redact_attachments defaults to true.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.messages.redact(
    issue_id="id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue that the message belongs to.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The ID of the message to redact.
    
</dd>
</dl>

<dl>
<dd>

**redact_attachments:** `typing.Optional[bool]` — Whether to permanently delete the message's attachments. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**redacted_body_message:** `typing.Optional[str]` — Replacement message body in HTML. The caller is responsible for replacing any sensitive portions. Defaults to "This message has been redacted."
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues SurveyResponses
<details><summary><code>client.issues.survey_responses.<a href="src/usepylon/issues/survey_responses/client.py">list</a>(...) -> GetIssueSurveyResponsesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns paginated CSAT and custom survey responses associated with an issue.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.survey_responses.list(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID or number of the issue.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `typing.Optional[str]` — Filter responses by survey template ID.
    
</dd>
</dl>

<dl>
<dd>

**submitted_after:** `typing.Optional[datetime.datetime]` — Filter responses submitted after this time (RFC3339 format).
    
</dd>
</dl>

<dl>
<dd>

**submitted_before:** `typing.Optional[datetime.datetime]` — Filter responses submitted before this time (RFC3339 format).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of responses to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues Threads
<details><summary><code>client.issues.threads.<a href="src/usepylon/issues/threads/client.py">list</a>(...) -> GetIssueThreadsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all threads for the specified issue.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.threads.list(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue to fetch threads for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.threads.<a href="src/usepylon/issues/threads/client.py">create</a>(...) -> CreateIssueThreadResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new internal thread on an issue.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.threads.create(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue to create a thread for.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the thread.
    
</dd>
</dl>

<dl>
<dd>

**slack_channel_id:** `typing.Optional[str]` 

The Slack channel ID to sync the thread to. When slack_thread_ts is also provided, links that existing Slack thread. Otherwise, creates a new Slack-backed thread.
Linking an existing Slack thread imports its message history and enables ongoing synchronization. Creating or linking a Slack-backed thread requires an API token configured to act as a human Pylon user whose verified Slack identity is a member of the channel. Pylon bot users and standalone API identities are not supported because they do not have Slack-verifiable channel membership.
    
</dd>
</dl>

<dl>
<dd>

**slack_thread_ts:** `typing.Optional[str]` — The root message timestamp of an existing Slack thread to link. Requires slack_channel_id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues VoiceCalls
<details><summary><code>client.issues.voice_calls.<a href="src/usepylon/issues/voice_calls/client.py">list</a>(...) -> GetIssueVoiceCallsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns voice call records for the specified phone issue. Each call includes its recordings, with parsed transcript segments and a presigned download URL for the audio file. Recordings whose transcript has not yet completed are omitted; refetch later to see them.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.issues.voice_calls.list(
    issue_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `str` — The ID of the issue to fetch voice calls for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases Articles
<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">list</a>(...) -> GetArticlesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of articles for the specified knowledge base.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.list(
    knowledge_base_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base the articles are being fetched from.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor to use for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of articles to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The language code to fetch articles in. If not provided, returns the default language.
    
</dd>
</dl>

<dl>
<dd>

**media:** `typing.Optional[ListArticlesRequestMedia]` — Controls whether embedded media is included in article HTML. Valid values are all (default) and none. When set to none, embedded images, video, audio, and inline media are removed while descriptive text and standard links are preserved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">create</a>(...) -> CreateArticleResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new article within a knowledge base.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.create(
    knowledge_base_id="id",
    author_user_id="author_user_id",
    body_html="body_html",
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base the article is being added to.
    
</dd>
</dl>

<dl>
<dd>

**author_user_id:** `str` — The ID of the user attributed as the author of the article.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The HTML body of the article.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the article.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — The ID of the collection containing the article.
    
</dd>
</dl>

<dl>
<dd>

**is_published:** `typing.Optional[bool]` — Whether the article should be published. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**is_unlisted:** `typing.Optional[bool]` — Whether the article is accessible only via a direct link. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the article. Defaults to a slug based on the title.
    
</dd>
</dl>

<dl>
<dd>

**translations:** `typing.Optional[typing.List[ArticleTranslationInput]]` — Translations of the article content in different languages
    
</dd>
</dl>

<dl>
<dd>

**visibility_config:** `typing.Optional[ArticleVisibilityConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">get</a>(...) -> GetArticleResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single article by ID within the specified knowledge base.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.get(
    knowledge_base_id="id",
    article_id="article_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The KnowledgeBaseID of the article to fetch.
    
</dd>
</dl>

<dl>
<dd>

**article_id:** `str` — The ID of the article to fetch.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The language code to fetch the article in. If not provided, returns the default language.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">delete</a>(...) -> DeleteArticleResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an article from the knowledge base.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.delete(
    knowledge_base_id="id",
    article_id="article_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The KnowledgeBaseID of the article to delete.
    
</dd>
</dl>

<dl>
<dd>

**article_id:** `str` — The ID of the article to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">update</a>(...) -> UpdateArticleResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing article. Only provided fields are modified.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.update(
    knowledge_base_id="id",
    article_id="article_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The KnowledgeBaseID of the article to update.
    
</dd>
</dl>

<dl>
<dd>

**article_id:** `str` — The ID of the article to update.
    
</dd>
</dl>

<dl>
<dd>

**author_user_id:** `typing.Optional[str]` — The ID of the user in this organization attributed as the author of the article. Does not change version authorship.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `typing.Optional[str]` — The HTML body of the article. Saved as a new draft; the published article changes only if publish_updated_body_html or is_published is true.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — The ID of the collection containing the article.
    
</dd>
</dl>

<dl>
<dd>

**is_published:** `typing.Optional[bool]` — Whether the article should be published or unpublished.
    
</dd>
</dl>

<dl>
<dd>

**is_unlisted:** `typing.Optional[bool]` — Whether the article is accessible only via a direct link.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The language code of the translation to update. If not provided, the default language (original article) will be updated.
    
</dd>
</dl>

<dl>
<dd>

**publish_updated_body_html:** `typing.Optional[bool]` — Whether to publish the updated body_html. Defaults to false, which leaves the change as a draft.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.List[str]]` — IDs of article tags to assign. If provided, replaces all tags currently assigned to the article.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the article. For the default language, applies to the live article immediately.
    
</dd>
</dl>

<dl>
<dd>

**visibility_config:** `typing.Optional[ArticleVisibilityConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.articles.<a href="src/usepylon/knowledge_bases/articles/client.py">request_review</a>(...) -> RequestArticleReviewResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests human and/or AI review on the article's current draft version. At least one of `reviewer_user_ids` or `request_ai_review` must be provided. The article must have an unpublished current version. Requesting AI review requires the organization to have AI article review enabled.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.articles.request_review(
    knowledge_base_id="id",
    article_id="article_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base the article belongs to.
    
</dd>
</dl>

<dl>
<dd>

**article_id:** `str` — The ID of the article to request review for.
    
</dd>
</dl>

<dl>
<dd>

**request_ai_review:** `typing.Optional[bool]` — When true, also queue an AI review. Requires the organization to have AI article review enabled.
    
</dd>
</dl>

<dl>
<dd>

**reviewer_user_ids:** `typing.Optional[typing.List[str]]` — IDs of users to request a human review from. Each user must already be a configured reviewer for the article's knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases Collections
<details><summary><code>client.knowledge_bases.collections.<a href="src/usepylon/knowledge_bases/collections/client.py">list</a>(...) -> GetCollectionsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all collections for the specified knowledge base.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.collections.list(
    knowledge_base_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.collections.<a href="src/usepylon/knowledge_bases/collections/client.py">create</a>(...) -> CreateCollectionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new collection within a knowledge base.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.collections.create(
    knowledge_base_id="id",
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base the article is being added to.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the collection.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the collection.
    
</dd>
</dl>

<dl>
<dd>

**parent_collection_id:** `typing.Optional[str]` — The ID of the parent collection.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the collection. Defaults to a slug based on the title.
    
</dd>
</dl>

<dl>
<dd>

**visibility_config:** `typing.Optional[CollectionVisibilityConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.collections.<a href="src/usepylon/knowledge_bases/collections/client.py">get</a>(...) -> GetCollectionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single collection by ID within the specified knowledge base.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.collections.get(
    knowledge_base_id="id",
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `str` — The ID of the collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.collections.<a href="src/usepylon/knowledge_bases/collections/client.py">delete</a>(...) -> DeleteCollectionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a collection and all articles within it from the knowledge base. Nested collections and their articles are also deleted.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.collections.delete(
    knowledge_base_id="id",
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base that the collection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `str` — The ID of the collection to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.collections.<a href="src/usepylon/knowledge_bases/collections/client.py">update</a>(...) -> UpdateCollectionResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing collection. Only provided fields are modified.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.collections.update(
    knowledge_base_id="id",
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base that the collection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `str` — The ID of the collection to update.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the collection.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the collection.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the collection.
    
</dd>
</dl>

<dl>
<dd>

**visibility_config:** `typing.Optional[CollectionVisibilityConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases RouteRedirects
<details><summary><code>client.knowledge_bases.route_redirects.<a href="src/usepylon/knowledge_bases/route_redirects/client.py">create</a>(...) -> CreateRouteRedirectResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a path redirect within a knowledge base, mapping a source path to an article or collection.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.route_redirects.create(
    knowledge_base_id="id",
    from_path="from_path",
    object_id="object_id",
    object_type="object_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base the route redirect is being added to.
    
</dd>
</dl>

<dl>
<dd>

**from_path:** `str` — The path to redirect from.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The ID of the object to redirect to.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `str` — The type of the object to redirect to. Must be "article" or "collection".
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Language of the object to redirect to. If not specified, the default language of the knowledge base will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases Themes
<details><summary><code>client.knowledge_bases.themes.<a href="src/usepylon/knowledge_bases/themes/client.py">get</a>(...) -> GetKnowledgeBaseThemeResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a theme's editable files, including current draft and published content.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.themes.get(
    knowledge_base_id="id",
    theme_id="theme_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.themes.<a href="src/usepylon/knowledge_bases/themes/client.py">update</a>(...) -> UpdateKnowledgeBaseThemeResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces one or more complete theme files in a single atomic draft update. Use the publish endpoint to make the changes live.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon, UpdateKnowledgeBaseThemeAsset
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.themes.update(
    knowledge_base_id="id",
    theme_id="theme_id",
    assets=[
        UpdateKnowledgeBaseThemeAsset(
            asset_type="asset_type",
            content="content",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.List[UpdateKnowledgeBaseThemeAsset]` — The complete theme files to replace. Changes are saved as drafts and are not published.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.themes.<a href="src/usepylon/knowledge_bases/themes/client.py">publish</a>(...) -> PublishKnowledgeBaseThemeResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Promotes all current draft files to their published versions. Changes become live immediately when this is the knowledge base's active theme. Publishing a theme with no draft changes is a no-op.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.knowledge_bases.themes.publish(
    knowledge_base_id="id",
    theme_id="theme_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `str` — The ID of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Surveys Responses
<details><summary><code>client.surveys.responses.<a href="src/usepylon/surveys/responses/client.py">list</a>(...) -> GetSurveyResponsesResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns paginated survey responses visible to the caller, optionally filtered by time range, account, or contact.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.surveys.responses.list(
    survey_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**submitted_after:** `typing.Optional[datetime.datetime]` — Filter responses submitted after this time (RFC3339 format).
    
</dd>
</dl>

<dl>
<dd>

**submitted_before:** `typing.Optional[datetime.datetime]` — Filter responses submitted before this time (RFC3339 format).
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — Filter responses by account ID. Required with contact_id when the caller has scoped account or contact access.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — Filter responses by contact ID. Required with account_id when the caller has scoped account or contact access.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of responses to fetch. Defaults to 100. Must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks Comments
<details><summary><code>client.tasks.comments.<a href="src/usepylon/tasks/comments/client.py">list</a>(...) -> GetTaskCommentsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all comments for a task, ordered by creation time.

**Rate limit:** 300 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.comments.list(
    task_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task to fetch comments for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.comments.<a href="src/usepylon/tasks/comments/client.py">create</a>(...) -> CreateTaskCommentResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new comment on a task. The authenticated user is the author.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.comments.create(
    task_id="id",
    body_html="body_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task to add a comment to.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The body of the comment in HTML format.
    
</dd>
</dl>

<dl>
<dd>

**is_internal:** `typing.Optional[bool]` — Whether the comment is visible only to internal users.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.comments.<a href="src/usepylon/tasks/comments/client.py">delete</a>(...) -> DeleteTaskCommentResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing comment. Only the original author can delete their comment.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.comments.delete(
    task_id="id",
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task.
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `str` — The ID of the comment to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.comments.<a href="src/usepylon/tasks/comments/client.py">update</a>(...) -> UpdateTaskCommentResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing comment. Only the original author can update their comment.

**Rate limit:** 120 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.tasks.comments.update(
    task_id="id",
    comment_id="comment_id",
    body_html="body_html",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task.
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `str` — The ID of the comment to update.
    
</dd>
</dl>

<dl>
<dd>

**body_html:** `str` — The updated body of the comment in HTML format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TrainingData Documents
<details><summary><code>client.training_data.documents.<a href="src/usepylon/training_data/documents/client.py">delete</a>(...) -> DeleteTrainingDataDocumentsResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes documents from a training data configuration by document ID or external ID.

**Rate limit:** 30 requests per minute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(
    token="<token>",
    environment=PylonEnvironment.US,
)

client.training_data.documents.delete(
    training_data_id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**training_data_id:** `str` — The ID of the training data.
    
</dd>
</dl>

<dl>
<dd>

**document_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Document IDs to delete.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — External IDs to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

