"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("Demo")

# Your WeatherAPI key (replace with your own)
API_KEY = "5cff526d514b453cbc6215809251308"
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
        # weather = {
        #     "city": data["location"]["name"],
        #     "region": data["location"]["region"],
        #     "country": data["location"]["country"],
        #     "temperature_c": data["current"]["temp_c"],  # Celsius
        #     "temperature_f": data["current"]["temp_f"],  # Fahrenheit
        #     "condition": data["current"]["condition"]["text"],
        #     "humidity": data["current"]["humidity"],
        #     "wind_kph": data["current"]["wind_kph"],  # wind speed in km/h
        #     "precip_mm": data["current"]["precip_mm"],  # precipitation in mm
        # }
        
        return data
    else:
        return {"error": "Could not fetch weather data: " + url}

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