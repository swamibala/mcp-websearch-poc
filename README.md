# MCP WebSearch - Proof of Concept

This project demonstrates how to expose **groq’s Response API and built-in Browser Search Tool** as a **Model Context Protocol (MCP) server**, imitating **compatible OpenAI’s Responses API & built-in Web Search Tool**.  

It serves as a **proof of concept** to show how Groq’s **Responses API** and **browser search tool** can be integrated into an MCP server using `fastmcp`.

---

## ✨ Features

- **uv project setup** for Python package management.  
- **qroq Responses API is OpenAI Response API compatible**.  
- **Browser Search Tool** integrated with MCP, enabling real-time interactive web browsing.  
- **FastMCP** framework to expose the search functionality as an MCP tool.  

---

## 📌 About [qroq Response API](!https://console.groq.com/docs/responses-api)

### Responses API
groq’s **Responses API** is fully compatible with OpenAI’s Responses API, which means you can use the same SDKs and integration patterns.  
- Supports **text + image inputs**  
- Produces **text outputs**  
- Handles **stateful conversations**  
- Enables **function calling** for external system integrations  

In this PoC, the Responses API is leveraged with the **built-in `browser_search` tool**.

---

### Browser Search Tool
Unlike simple web search, groq’s **browser search** simulates **human-like browsing behavior**, interacting with pages for richer results.  
- Provides more **detailed search results** than traditional web search.  
- Useful for **real-time information retrieval**.  
- **Supported models:**  
  - `openai/gpt-oss-20b`  
  - `openai/gpt-oss-120b`  

⚠️ **Limitations:**  
- **Web Search tool is not supported** for OpenAI models. So, groq's Browser Search Tool has been used.
- **Structured outputs are not compatible** with browser search (reason why structured output wasn’t implemented in this PoC).  

---

## ⚙️ Setup & Installation
### 1. Prerequisites
- Python **>=3.12**
- A valid **GROQ_API_KEY** (sign up at [groq](https://groq.com/))

### 2. Install dependencies
```
uv sync
```

### 3. Environment Variables
```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the MCP Client which starts MCP Server internally
```
uv run mcp_client.py
```
---

## 🔎 MCP Tool: perform_web_search
The server exposes one MCP tool:
```
@mcp.tool
async def perform_web_search(query: str) -> str:
    """
    Performs a real-time web search for the given query using the 
    groq Responses API with built-in browser_search tool.
    """
```

Input: query (string)
Output: Synthesized text summary from browser search

Example invocation:
```
{
  "method": "perform_web_search",
  "params": {
    "query": "Parking nearby Marriott Hotel County Hall, London, UK"
  }
}
```

## ⚠️ **Limitations:**  
- **Web Search tool is not supported** for OpenAI models.  
- **Structured outputs are not compatible** with browser search (reason why structured output wasn’t implemented in this PoC).  
