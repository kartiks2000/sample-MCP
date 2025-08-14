"""
Dog tools for the MCP server.
"""

import requests
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

DOG_API_KEY = "live_pUsYTB3BrPGPDgyHNOOfuxFanTIflrmQeDaJbP08q0iuo0rhKdyNrKQeIMt1W2Et"  # Replace with your actual API key
DOG_API_URL = "https://api.thedogapi.com/v1/images/search"

def register_dog_tools(mcp: FastMCP):
    """Register dog-related tools with the MCP server."""
    
    @mcp.tool()
    def get_dog_pics(limit: int = 2) -> List[Dict]:
        """Fetch random dog pictures using TheDogAPI."""
        
        headers = {
            "x-api-key": DOG_API_KEY
        }
        
        params = {
            "limit": limit
        }

        response = requests.get(DOG_API_URL, headers=headers, params=params)

        if response.status_code == 200:
            return [
                {
                    "url": image["url"],
                    "id": image["id"],
                    "width": image["width"],
                    "height": image["height"]
                }
                for image in response.json()
            ]
        else:
            return [{"error": f"Failed to fetch dog images. Status: {response.status_code}", "details": response.text}]
