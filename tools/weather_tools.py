"""
Weather tools for the MCP server.
"""

import requests
from mcp.server.fastmcp import FastMCP

# Your WeatherAPI key (replace with your own)
API_KEY = "5cff526d514b453cbc6215809251308" # expired (dont try using this)
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def register_weather_tools(mcp: FastMCP):
    """Register weather-related tools with the MCP server."""
    
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
