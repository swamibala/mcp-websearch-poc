# MCP Tool: Web Search with OpenAI Response API
This project serves as a Proof of Concept for exposing a "Web Search" capability as a Model Context Protocol (MCP) server. 
It leverages the groq API's compatibility with the OpenAI Response API to access an advanced, real-time browsing capability.

## 🌟 Key Features

* **Model Integration:** Uses the **`openai/gpt-oss-120b`** model via the Groq API.
* **MCP Implementation:** Exposes the search functionality as a standardized MCP server using the `fastmcp` Python library.
* **Advanced Tooling:** Demonstrates the use of OpenAI's specialized **`browser_search`** tool for comprehensive web content retrieval.

* **Out Of Scope**
* Structured Output: The tool can return a structured response, though the final output is synthesized text from the LLM. But, combining structured output + tool invocation is not currently supported (per qroq docs). So, this proof of concept does not have structured output
* browser_search tool has been used instead of web_search

## 🔎 Tool Capability: Browser Search (PoC Note)

The Groq platform supports a highly capable tool for web access:

> **Browser Search:** Unlike the traditional "Web Search" which retrieves simple text snippets, Groq's `browser_search` mimics human browsing behavior by navigating websites interactively. This provides a more comprehensive and detailed result, making it ideal for this Proof of Concept.
>
> **Note for Production:** For highly latency-sensitive use cases, Groq recommends using the standard `Web Search` tool if available, but for this PoC, `browser_search` demonstrates the advanced capabilities well.

## 🛠️ Setup and Installation

### Prerequisites

1.  Python 3.10+
2.  A Groq API Key (available from [https://console.groq.com](https://console.groq.com)).

### Steps

1.  **Clone the Repository & Setup Environment:**

    ```bash
    git clone mcp-websearch-poc
    cd mcp-websearch-poc
    
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt # Requires openai, python-dotenv, fastmcp
    ```

3.  **Configure API Key:**

    Create a file named **`.env`** in the root directory and add your Groq API key:

    ```bash
    # .env file content
    GROQ_API_KEY="sk-gq-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```
    *(Ensure `.env` is added to your `.gitignore` for security)*

## 🚀 Usage

The project is structured as a client/server demonstration over the **STDIO** transport method (the client executes the server script and communicates via standard input/output).

### Running the MCP Client

Execute the client script, which will automatically start the server, discover the tools, and trigger a web search call.

```bash
python mcp_client.py
