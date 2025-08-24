from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def current_time() -> dict:
    return {
        "current_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description=(
        "Tool agent"
    ),
    instruction=(
        """You are a helpful assistnat that can use the following tools: 
        - current_time
        """
    ),
    tools=[current_time]
)