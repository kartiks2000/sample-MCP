"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
import requests
from typing import List, Dict

# Create an MCP server
mcp = FastMCP("Demo")

# Your WeatherAPI key (replace with your own)
API_KEY = "5cff526d514b453cbc6215809251308" # expired (dont try using this)
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> dict:
    """Fetch current weather data for a given city using WeatherAPI"""
    
    # Construct the complete URL for the API request
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    
    # Send GET request
    response = requests.get(url)
    
    # If the response is successful (status code 200), parse the data
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant weather data
        weather = {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature_c": data["current"]["temp_c"],  # Celsius
            "temperature_f": data["current"]["temp_f"],  # Fahrenheit
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_kph": data["current"]["wind_kph"],  # wind speed in km/h
            "precip_mm": data["current"]["precip_mm"],  # precipitation in mm
        }
        
        return data
    else:
        return {"error": "Could not fetch weather data: " + url}

NEWS_API_KEY = "97489af27d6f4e18bd90c0385a39e510"
BASE_URL_NEWS = "https://newsapi.org/v2/everything"

# News API tool
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


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."