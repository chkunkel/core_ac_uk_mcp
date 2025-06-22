A simple MCP server wrapping parts of the CORE.ac.uk API:

API documentation: https://api.core.ac.uk/docs/v3

## Installation

1. Clone repository:

   ```
   git clone https://github.com/chkunkel/core_ac_uk_mcp
   cd core_ac_uk_mcp
   ```

2. Install dependencies with uv:

   ```bash
   uv sync
   ```
   
   When installed, run:

    ```bash
    uv run core_mcp_server_local.py
    ```
    
   Output (if successful):

    ```bash
    INFO     Starting MCP server 'CORE\xa0API\xa0Server' with transport 'stdio'
    ```
    
    With an API key installed in the environment, the MCP server is ready.

    
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

