### Important Commands

Steps to intialize the uv package
```
uv init 
```

Command to installing package in environment
```
uv add mcp
uv add fastmcp 
```
Command to list all the packages installed in environment
```
uv pip list 
```
To update the installed packages version based on pyproject.toml
```
uv sync
```
To run the model
```
uv run train_model.py 
```

Command to run npx MCP server tool
```
npx @modelcontextprotocol/inspector python salary_mcp_server.py
```