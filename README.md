A simple MCP server wrapping parts of the CORE.ac.uk API:

API documentation: https://api.core.ac.uk/docs/v3

## Installation

## API Key Setup

You need to obtain an API Key on the website first.

Then create a `.env` file in the main directory with the following content:
   ```
   CORE_API_KEY=<your key>
   ```
You don't need quotes or the < > brackets around your key.

## Server Configuration

Run in console as `python core_mcp_server.py`

Add the following config to the program of your choice:
```
{
  "mcpServers": {
    "CORE API Server": {
        "type": "streamable-http",
        "url": "http://127.0.0.1:8000/mcp",
        "note": "For Streamable HTTP connections, add this URL directly in your MCP Client"
    }
    }
}
```

## Available Functions

