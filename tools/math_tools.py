"""
Math tools for the MCP server.
"""

from mcp.server.fastmcp import FastMCP

def register_math_tools(mcp: FastMCP):
    """Register math-related tools with the MCP server."""
    
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    @mcp.tool()
    def multiply(a: int, b: int) -> int:
        """Multiply two numbers"""
        return a * b
