# Pylon Python SDK

The official Python SDK for the [Pylon API](https://docs.usepylon.com).

> **Alpha.** The SDK is new and its interface may change between `0.x` releases.

## Installation

```bash
pip install --pre usepylon
```

`--pre` is needed while only alpha releases exist.

Requires Python 3.9 or later.

## Usage

```python
from usepylon import Pylon
from usepylon.environment import PylonEnvironment

client = Pylon(token="YOUR_API_TOKEN")

issue = client.issues.get("issue_id").data

# List methods page through results automatically.
for account in client.accounts.list():
    print(account.name)
```

Pylon accounts live in either the US or the EU region, and the client defaults to the US. EU accounts must select the EU region:

```python
client = Pylon(token="YOUR_API_TOKEN", environment=PylonEnvironment.EU)
```

`AsyncPylon` has the same methods for use with `asyncio`.

### Errors

Requests that fail raise a subclass of `ApiError` carrying the status code and response body:

```python
from usepylon.core.api_error import ApiError

try:
    client.issues.get("missing")
except ApiError as error:
    print(error.status_code, error.body)
```

## Reference

[reference.md](reference.md) documents every method. The [Pylon API documentation](https://docs.usepylon.com) covers the underlying endpoints.

## Contributing

This SDK is generated from Pylon's OpenAPI spec, so changes to `src/usepylon` are overwritten by the next sync. Please open an issue for bugs or missing endpoints.
