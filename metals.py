from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import os
import requests

load_dotenv()

mcp = FastMCP("metals-mcp-server")
api_key = os.getenv("METALS_DEV_API_KEY")
base_url = "https://api.metals.dev/v1"

@mcp.tool()
def get_metal_price(metal: str) -> str:
    """Get the current spot price for a specific metal (e.g., 'gold', 'silver', 'platinum', 'palladium')"""
    try:
        params = {
            "api_key": api_key,
            "currency": "USD",
            "unit": "toz"
        }
        response = requests.get(f"{base_url}/latest", params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                metals = data.get("metals", {})
                price = metals.get(metal.lower())
                if price:
                    return f"Current {metal} price: ${price} per troy ounce"
                else:
                    return f"Metal '{metal}' not found. Available metals: {list(metals.keys())}"
            else:
                return f"API Error: {data.get('error_message', 'Unknown error')}"
        else:
            return f"Error fetching {metal} price: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_all_metals() -> str:
    """Get current spot prices for all available metals"""
    try:
        params = {
            "api_key": api_key,
            "currency": "USD",
            "unit": "toz"
        }
        response = requests.get(f"{base_url}/latest", params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                metals = data.get("metals", {})
                result = "Current metal prices:\n"
                for metal, price in metals.items():
                    result += f"{metal.capitalize()}: ${price} per troy ounce\n"
                return result
            else:
                return f"API Error: {data.get('error_message', 'Unknown error')}"
        else:
            return f"Error fetching metal prices: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")