"""
News tools for the MCP server.
"""

import requests
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

NEWS_API_KEY = "97489af27d6f4e18bd90c0385a39e510"
BASE_URL_NEWS = "https://newsapi.org/v2/everything"

def register_news_tools(mcp: FastMCP):
    """Register news-related tools with the MCP server."""
    
    @mcp.tool()
    def get_news(query: str = "Apple", from_date: str = "2025-08-14", sort_by: str = "popularity") -> List[Dict]:
        """Latest news articles based on a keyword and date."""
        
        params = {
            "q": query,
            "from": from_date,
            "sortBy": sort_by,
            "apiKey": NEWS_API_KEY
        }
        
        url = f"{BASE_URL_NEWS}?q={query}&from={from_date}&sortBy={sort_by}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            
            # Simplify and return relevant article information
            return [
                {
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"],
                    "source": article["source"]["name"],
                    "publishedAt": article["publishedAt"]
                }
                for article in articles
            ]
        else:
            return [{"error": f"Failed to fetch news. Status code: {response.status_code} and url: {url}"}]
