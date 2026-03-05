# MCP Multi-Server Agent (Math + Weather)

## Overview

This project demonstrates how to build an **Agentic AI system using the Model Context Protocol (MCP)**. The agent connects to multiple MCP servers and dynamically discovers and uses their tools to respond to user queries.

The system integrates a **Math MCP Server** and a **Weather MCP Server**, allowing the agent to perform arithmetic operations and retrieve weather information based on the user's request.

The agent is built using **LangChain**, **Groq LLM**, and **MCP adapters**, enabling seamless communication between the AI model and external tool servers.

---

## Architecture

The system follows a multi-server MCP architecture where the AI agent interacts with external tools through MCP servers.

```
User Query
    │
    ▼
AI Agent (LLM)
    │
    ├── Math MCP Server (Local - stdio)
    │       • Add numbers
    │       • Subtract numbers
    │       • Multiply numbers
    │
    └── Weather MCP Server (HTTP - streamable transport)
            • Retrieve weather information
```

The agent automatically selects and invokes the appropriate tool depending on the user's request.

---

## Key Features

* Multi-server MCP integration
* Dynamic tool discovery from MCP servers
* AI agent capable of tool-based reasoning
* Support for both **stdio** and **HTTP MCP transports**
* Integration with **Groq LLM** for fast inference
* Built using **LangChain agents**

---

## MCP Servers Used

### Math MCP Server

Provides arithmetic tools that allow the agent to perform mathematical operations.

### Weather MCP Server

Provides weather information for a given city through an MCP-accessible tool.

---

## Technologies Used

* **Model Context Protocol (MCP)**
* **LangChain**
* **LangChain MCP Adapters**
* **Groq LLM**
* **Python**
* **Asyncio**

---

## How the System Works

1. The agent receives a user query.
2. The agent analyzes whether the task requires a tool.
3. Available tools are fetched dynamically from MCP servers.
4. The agent invokes the appropriate tool.
5. The result is returned to the user.

---

## Example Queries

```
What is 5 * 100 + 200?
```

```
What is the weather in California?
```

The agent determines whether the query requires the **Math tool** or **Weather tool** and executes it accordingly.

---

## Learning Outcomes

This project demonstrates important concepts in **Agentic AI systems**:

* Tool-based reasoning with LLM agents
* Multi-server MCP architecture
* Integration of external tools with AI agents
* Asynchronous agent workflows

---

## Author

This project was built as part of learning and experimenting with **Agentic AI, MCP-based tool ecosystems, and LangChain agents**.
