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
    uv run <path_to_directory>/core_mcp_server_local.py
    ```
    Please add the path to the file, you don't need quotes or the < > brackets around your key.
    
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
    "core_ac_uk_server": {
      "command": "uv",
      "args": [
        "run",
        "<SCRIPT_PATH>/core_mcp_server_local.py"
      ],
      "env": {},
      "working_directory": null,
      "start_on_launch": true
    }
  }
}
```
Replace `<SCRIPT_PATH>` by the respective path to the script


## Available Functions (so far)
- `search_works_by_keywords`
- `download_single_work_by_identifier`

