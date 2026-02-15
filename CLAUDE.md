# Waldur API Client SDK

This is an auto-generated Python SDK for the Waldur API with ~2,300 endpoints across 285 domains.

## LLM Navigation

Before exploring the source code, read these files in order:

1. `llms.txt` — Overview, quick start, and list of all API domains
2. `api-map.md` — Every endpoint grouped by domain with method, path, and description
3. `llms-full.txt` — Complete reference with all parameters for every endpoint

These files are also available inside the package at `waldur_api_client/llms.txt` etc.,
so they are accessible in pip-installed copies via `site-packages/waldur_api_client/`.

## SDK Usage Pattern

```python
from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.<domain> import <operation_id>

client = AuthenticatedClient(base_url="https://instance.waldur.com/", token="...")
result = <operation_id>.sync(client=client, ...)
```

Each endpoint module provides: `sync()`, `sync_detailed()`, `sync_all()`, `asyncio()`, `asyncio_detailed()`, `asyncio_all()`.
