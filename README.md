# MCP Multi-Tool Agent (Math + Weather)

## Overview

This project demonstrates how to build an **Agentic AI system using the Model Context Protocol (MCP)**.
The agent dynamically connects to multiple MCP servers and uses their tools to answer user queries.

In this project, the agent connects to:

* **Math MCP Server** (local process via `stdio`)
* **Weather MCP Server** (HTTP via `streamable-http`)

The agent automatically selects the correct tool based on the user's request.

---

# Architecture

```
User Query
    │
    ▼
LangChain Agent (LLM)
    │
    ├── Math MCP Server (stdio)
    │        ├── add
    │        ├── subtract
    │        └── multiply
    │
    └── Weather MCP Server (HTTP)
             └── get_weather
```

The agent retrieves tools from MCP servers dynamically and invokes them when required.

---

# Project Structure

```
project/
│
├── mathserver.py
├── weather.py
├── client.py
├── .env
└── README.md
```

---

# Math MCP Server

The math server exposes basic arithmetic tools.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b

@mcp.tool()
def subtract(a:int,b:int)->int:
    """Subtract two numbers"""
    return a-b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

This server communicates using **standard input/output**, allowing the agent to run it as a subprocess.

---

# Weather MCP Server

The weather server provides weather information for a given city.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city:str)->str:
    """Get the weather for a given city"""
    return f"The weather in {city} is sunny"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
```

This server runs over **HTTP**, enabling remote MCP tool access.

---

# Agent Client

The client connects to multiple MCP servers and creates an AI agent.

```python
client = MultiServerMCPClient({
    "math":{
        "command":"python",
        "args":["mathserver.py"],
        "transport":"stdio"
    },
    "weather":{
        "url":"http://localhost:8000/mcp",
        "transport":"streamable-http"
    }
})
```

The agent retrieves tools from both servers and uses them to answer questions.

---

# Running the Project

## 1 Install dependencies

```
pip install mcp langchain langchain-mcp-adapters langchain-groq python-dotenv
```

---

## 2 Set API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

---

## 3 Start Weather Server

```
python weather.py
```

---

## 4 Run the Agent

```
python client.py
```

---

# Example Output

```
Math Response: 700
Weather Response: The weather in California is sunny
```

---

# Key Concepts Demonstrated

* Model Context Protocol (MCP)
* Multi-server MCP architecture
* Tool discovery from MCP servers
* Agent tool invocation
* stdio vs HTTP MCP transports
* LangChain agent integration

---

# Why MCP?

MCP allows AI systems to **connect to external tools in a standardized way**, enabling:

* Tool discovery
* Secure tool execution
* Modular AI architectures
* Multi-agent workflows

---

# Future Improvements

* Integrate real weather APIs
* Add database MCP server
* Add web search tools
* Deploy MCP servers to cloud

---

# Author

Built as part of exploring **Agentic AI and MCP-based tool ecosystems**.
