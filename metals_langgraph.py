# code inspiration from https://github.com/langchain-ai/langchain-mcp-adapters
import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI

load_dotenv()

# Check if OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. "
        "Please create a .env file with your OpenAI API key: OPENAI_API_KEY=your_key_here"
    )

async def create_metals_agent():
    # Initialize the chat model with OpenAI
    model = ChatOpenAI(model="gpt-4o-mini")
    
    # Set up the MCP client to connect to your metals server
    client = MultiServerMCPClient(
        {
            "metals": {
                "command": "python",
                "args": ["/Users/sriteja/aibootcamp/MCP-Session-Code/metals.py"],
                "transport": "stdio",
            }
        }
    )
    
    # Get the tools from the MCP server
    tools = await client.get_tools()
    
    def call_model(state: MessagesState):
        response = model.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}
    
    # Build the StateGraph
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    
    graph = builder.compile()
    return graph

async def main():
    # Create the agent
    graph = await create_metals_agent()
    
    # Example interactions
    print("=== Metals MCP LangGraph Agent ===")
    print("Ask questions about metal prices!")
    print("Examples:")
    print("- What's the current price of gold?")
    print("- Get me all metal prices")
    print("- What's the silver price?")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        try:
            response = await graph.ainvoke({"messages": user_input})
            print(f"Agent: {response['messages'][-1].content}\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    asyncio.run(main())