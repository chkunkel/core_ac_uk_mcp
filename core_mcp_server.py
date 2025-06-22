"""
FastMCP wrapper for CORE API v3
Make sure you have a CORE API key: https://core.ac.uk/api-keys/register
Store it as CORE_API_KEY in a .env file or your shell env.
"""

import os, asyncio, json
import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()                           # loads .env if present
API_KEY = os.getenv("CORE_API_KEY")     # required for most CORE calls
BASE_URL = "https://api.core.ac.uk/v3"  # CORE API root

headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}

# 1️⃣  create the MCP server object
mcp = FastMCP("CORE API Server")

# 2️⃣  create a shared async httpx client
client = httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=1000.0)

@mcp.tool(description="Search CORE for works matching a free‑text query")
async def search_works_by_keywords(query: str, limit: int = 10) -> list[dict]:
    params = {"q": query, "limit": limit}
    resp = await client.get("/search/works/", params=params)  # <-- note the trailing slash
    print(json.dumps(resp.json()["results"]))
    return json.dumps(resp.json()["results"])

@mcp.tool(description="Fetch full metadata for a single CORE work")
async def download_single_work_by_identifier(identifier: str) -> dict:
    resp = await client.get(f"/works/{identifier}",params={})  # <-- optional, but good to normalize
    resp.raise_for_status()
    return str(resp.json())

if __name__ == "__main__":
    mcp.run(transport="stdio")
