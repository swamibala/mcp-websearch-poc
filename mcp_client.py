# mcp_client.py

import asyncio
import os
import sys
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport

# --- Configuration ---
SERVER_SCRIPT = os.path.join(os.path.dirname(__file__), "mcp_server.py")

async def run_mcp_client():
    print("--- MCP Client: Connecting to Web Search Server ---")

    # 1. Define the transport (using STDIO for local execution of mcp_server.py)
    transport = PythonStdioTransport(SERVER_SCRIPT)

    # 2. Initialize the client with this transport
    async with Client(transport) as client:
        # Fetch server info explicitly
        print("Client connected successfully.")

        # 3. Discover the tools available on the server
        print("\nRequesting tool list from server...")
        tools = await client.list_tools()
        
        web_search_tool = next((t for t in tools if t.name == "perform_web_search"), None)

        if not web_search_tool:
            print("Error: 'perform_web_search' tool not found on server.")
            return

        print(f"Tool Found: {web_search_tool.name}")
        print(f"Description: {web_search_tool.description}")


        # --- Manual Tool Call (Simulating LLM's decision) ---
        search_query = "Parking nearby Marriott Hotel County Hall, London, UK"
        
        print(f"\n--- Simulating LLM Call Request: tools/call ---")
        print(f"Calling tool: {web_search_tool.name} with query: '{search_query}'")
        
        # 4. Execute the tool by sending a call request
        arguments = {"query": search_query}
        
        tool_result_response = await client.call_tool(
            name=web_search_tool.name,
            arguments=arguments
        )

        # 5. Process the result from the server
        if tool_result_response.is_error:
            print("Tool execution returned an error!")
            print(tool_result_response.data or tool_result_response.content)
        else:
            for result in tool_result_response.content:
                if result.type == "text":
                    print("Web Search Result:")
                    print("---------------------------------")
                    print(result.text)
                    print("---------------------------------")
                else:
                    print(f"Received non-text result: {result}")
    

if __name__ == "__main__":
    asyncio.run(run_mcp_client())
