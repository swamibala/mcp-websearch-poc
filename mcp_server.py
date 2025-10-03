import os
from dotenv import load_dotenv
from openai import OpenAI
from fastmcp import FastMCP, Context

# Load environment variables
load_dotenv()

# --- Configuration ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "openai/gpt-oss-20b"

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Server cannot start.")

# Initialize the Groq/OpenAI client once
try:
    groq_client = OpenAI(
        api_key=GROQ_API_KEY,
        base_url=GROQ_BASE_URL,
    )
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    exit()

# --- Initialize the FastMCP Server ---
mcp = FastMCP("WebSearchToolServer")

@mcp.tool
async def perform_web_search(query: str) -> str:
    """
    Performs a real-time web search for the given query using the groq's Response API with built-in browser_search tool.

    :param query: The search term or question to look up on the web.
    :return: A synthesized text summary of the search results.
    """
    print(f"Server received: perform_web_search(query='{query}')")
    
    # 1. Internal Call to Groq API
    try:
        response = groq_client.responses.create(
            model=MODEL_NAME,
            input=query,
            tool_choice="required",
            tools=[
                {
                    "type": "browser_search" # Using groq's Response API internal built-in tool
                }
            ]
        )
        
        output_text = response.output_text
        print(f"groq API Success. Result length: {len(output_text)} chars.")
        return output_text

    except Exception as e:
        error_msg = f"groq API call failed during web search: {e}"
        print(error_msg)
        # MCP server should return an error or a descriptive string
        return f"Error executing web search: {e}"

# --- Server Startup ---
if __name__ == "__main__":
    # This runs the server using the default STDIO transport
    print("Starting MCP Server with STDIO transport...")
    mcp.run() 
    # The server is now listening for JSON-RPC messages on stdin/stdout