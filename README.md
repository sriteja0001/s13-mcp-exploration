<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">AI Makerspace: MCP Event</h1>

This project is a demonstration of the MCP (Model Context Protocol) server, which utilizes the Tavily API for web search capabilities. The server is designed to run in a standard input/output (stdio) transport mode.

## Project Overview

The MCP server is set up to handle web search queries using the Tavily API. It is built with the following key components:

- **TavilyClient**: A client for interacting with the Tavily API to perform web searches.

## Prerequisites

- Python 3.13 or higher
- A valid Tavily API key

## ⚠️NOTE FOR WINDOWS:⚠️

You'll need to install this on the *Windows* side of your OS. 

This will require getting two CLI tool for Powershell, which you can do as follows:

- `winget install astral-sh.uv`
- `winget install --id Git.Git -e --source winget`

After you have those CLI tools, please open Cursor *into Windows*.

Then, you can clone the repository using the following command in your Cursor terminal:

```bash
git clone https://github.com/AI-Maker-Space/MCP-Session-Code.git
```

After that, you can follow from Step 2. below!

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Configure environment variables**:
Copy the `.env.sample` to `.env` and add your Tavily API key:
   ```
   TAVILY_API_KEY=your_api_key_here
   ```

3. 🏗️ **Add a new tool to your MCP Server** 🏗️

Create a new tool in the `server.py` file, that's it!

## Running the MCP Server

To start the MCP server, you will need to add the following to your MCP Profile in Cursor:

> NOTE: To get to your MCP config. you can use the Command Pallete (CMD/CTRL+SHIFT+P) and select "View: Open MCP Settings" and replace the contents with the JSON blob below.

```
{
    "mcpServers":  {
        "mcp-server": {
            "command" : "uv",
            "args" : ["--directory", "/PATH/TO/REPOSITORY", "run", "server.py"]
        }
    }
}
```

The server will start and listen for commands via standard input/output.

## Usage

The server provides a `web_search` tool that can be used to search the web for information about a given query. This is achieved by calling the `web_search` function with the desired query string.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

# MCP Session Code

This repository contains various MCP (Model Context Protocol) server implementations and a LangGraph application that interacts with them.

## Environment Setup

To run the LangGraph application, you need to create a `.env` file in the root directory with the following variables:

```bash
# OpenAI API Key (required for LangGraph agent)
OPENAI_API_KEY=your_openai_api_key_here

# Metals API Key (required for metals.py server)
METALS_DEV_API_KEY=your_metals_api_key_here
```

## Files

- `metals.py` - MCP server for getting metal prices
- `metals_langgraph.py` - Interactive LangGraph application
- `metals_langgraph_simple.py` - Simple LangGraph demonstration
- `dice_roller.py` - MCP server for rolling dice
- `server.py` - General MCP server example

## Usage

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Create a `.env` file with your API keys

3. Run the LangGraph application:
   ```bash
   python metals_langgraph.py
   ```

   Or run the simple demonstration:
   ```bash
   python metals_langgraph_simple.py
   ```
