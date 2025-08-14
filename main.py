"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
from tools import (
    register_math_tools,
    register_weather_tools,
    register_news_tools,
    register_dog_tools,
    register_greeting_tools
)

# Create an MCP server
mcp = FastMCP("Demo")

# Register all tools
register_math_tools(mcp)
register_weather_tools(mcp)
register_news_tools(mcp)
register_dog_tools(mcp)
register_greeting_tools(mcp)