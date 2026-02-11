from __future__ import annotations
from typing import Any
import acp.schema
from fastmcp.mcp_config import MCPConfig
from pydantic import ValidationError
from kimi_cli.acp.types import MCPServer
from kimi_cli.exception import MCPConfigError

def acp_mcp_servers_to_mcp_config(mcp_servers: list[MCPServer]) -> MCPConfig:
    """
    Acp Mcp Servers To Mcp Config.
    
    Args:
    mcp_servers: Description.
    
    Returns:
        Description.
    """
    if not mcp_servers:
        return MCPConfig()

    try:
        return MCPConfig.model_validate(
            {"mcpServers": {server.name: _convert_acp_mcp_server(server) for server in mcp_servers}}
        )
    except ValidationError as exc:
        raise MCPConfigError(f"Invalid MCP config from ACP client: {exc}") from exc

# Internal Function Index:
#
#   [func] _convert_acp_mcp_server




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


def _convert_acp_mcp_server(server: MCPServer) -> dict[str, Any]:
    """Convert an ACP MCP server to a dictionary representation."""
    match server:
        case acp.schema.HttpMcpServer():
            return {
                "url": server.url,
                "transport": "http",
                "headers": {header.name: header.value for header in server.headers},
            }
        case acp.schema.SseMcpServer():
            return {
                "url": server.url,
                "transport": "sse",
                "headers": {header.name: header.value for header in server.headers},
            }
        case acp.schema.McpServerStdio():
            return {
                "command": server.command,
                "args": server.args,
                "env": {item.name: item.value for item in server.env},
                "transport": "stdio",
            }
