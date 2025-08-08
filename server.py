from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dice_roller import DiceRoller

load_dotenv()

mcp = FastMCP("mcp-server")
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    search_results = client.get_search_context(query=query)
    return search_results

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

"""
Add your own tool here, and then use it through Cursor!
"""
@mcp.tool()
def get_inspirational_quote(query: str) -> str:
    """Get a random inspirational quote to motivate and inspire"""
    import random
    
    quotes = [
        "Be good. - Sriteja",
        "Be cool. - Sriteja",
        "Be nice. - Sriteja",
        "Be amazing. - Sriteja",
        "Be inspirational. - Sriteja",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
        "The mind is everything. What you think you become. - Buddha",
        "Life is 10% what happens to you and 90 percent how you react to it. - Charles R. Swindoll"
    ]
    
    return str(random.choice(quotes))

if __name__ == "__main__":
    mcp.run(transport="stdio")