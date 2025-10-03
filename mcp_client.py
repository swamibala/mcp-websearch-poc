# mcp_client.py

import asyncio
import os
import sys
from fastmcp import StdioClient, StdioServerParameters, ClientSession

# --- Configuration ---
# The command to start our local server script
SERVER_COMMAND = sys.executable
SERVER_ARGS = [os.path.join(os.path.dirname(__file__), "mcp_server.py")]

async def run_mcp_client():
    print("--- MCP Client: Connecting to Web Search Server ---")

    # 1. Define the connection parameters (using STDIO for local execution)
    server_params = StdioServerParameters(command=SERVER_COMMAND, args=SERVER_ARGS)

    # 2. Initialize the client (using StdioClient for local process communication)
    client = StdioClient(server_params=server_params)

    # 3. Create a session and connect to the server
    async with client.connect() as session:
        session: ClientSession
        print(f"Client connected successfully to: {session.server_info.name}")

        # 4. Discover the tools available on the server
        print("\nRequesting tool list from server...")
        tool_list_response = await session.tooling.list()
        
        web_search_tool = next((t for t in tool_list_response.tools if t.name == "perform_web_search"), None)

        if not web_search_tool:
            print("Error: 'perform_web_search' tool not found on server.")
            return

        print(f"Tool Found: {web_search_tool.title}")
        print(f"Description: {web_search_tool.description}")

        # --- Manual Tool Call (Simulating LLM's decision) ---
        search_query = "What is the capital of Australia and its current population?"
        
        print(f"\n--- Simulating LLM Call Request: tools/call ---")
        print(f"Calling tool: {web_search_tool.name} with query: '{search_query}'")
        
        # 5. Execute the tool by sending a tools/call request
        arguments = {"query": search_query}
        
        # The client sends the call, the server executes the Groq logic, and returns the result
        tool_result_response = await session.tooling.call(
            name=web_search_tool.name,
            arguments=arguments
        )

        # 6. Process the result from the server
        print("\n--- Server Tool Execution Complete ---")
        print(f"Result Type: {tool_result_response.result.type}")
        
        if tool_result_response.result.type == 'text':
            print("Web Search Result:")
            print("---------------------------------")
            print(tool_result_response.result.text)
            print("---------------------------------")
        else:
            print(f"Received non-text result: {tool_result_response.result}")


if __name__ == "__main__":
    # Ensure the mcp_server.py file is in the same directory or adjust the path
    asyncio.run(run_mcp_client())