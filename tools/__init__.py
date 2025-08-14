"""
Tools package for the MCP server.
"""

from .math_tools import register_math_tools
from .weather_tools import register_weather_tools
from .news_tools import register_news_tools
from .dog_tools import register_dog_tools
from .greeting_tools import register_greeting_tools

__all__ = [
    "register_math_tools",
    "register_weather_tools", 
    "register_news_tools",
    "register_dog_tools",
    "register_greeting_tools"
]
