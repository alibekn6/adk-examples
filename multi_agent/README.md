# Multi-Agent Systems in ADK

This example demonstrates how to build a collaborative multi-agent system using the Agent Development Kit (ADK). In this setup, specialized agents work together to tackle complex tasks by focusing on distinct areas of expertise.

## Overview

Multi-agent systems enable advanced coordination by delegating specialized tasks to agents optimized for specific domains. Through delegation and inter-agent communication, they can efficiently solve problems that are challenging for a single agent to handle.

## Required Project Structure

To ensure ADK correctly discovers your agents, your project must follow this specific structure:

```
parent_folder/
├── root_agent_folder/           # Main agent package (e.g., "manager")
│   ├── __init__.py              # Must import agent.py
│   ├── agent.py                 # Must define a variable named root_agent
│   ├── .env                     # Environment variables
│   └── sub_agents/              # Directory for all sub-agents
│       ├── __init__.py          # Either empty or imports sub-agents
│       ├── agent_1_folder/      # Sub-agent package
│       │   ├── __init__.py      # Must import agent.py
│       │   └── agent.py         # Must define an agent variable
│       ├── agent_2_folder/
│       │   ├── __init__.py
│       │   └── agent.py
│       └── ...
```

### Key Components

- **Root Agent Package:**
  - Contains the main agent definition in `agent.py` where the `root_agent` variable is defined.

- **Sub-agents Directory:**
  - A dedicated folder (typically named `sub_agents`) that contains each specialized agent in its own package with a similar structure.

- **Sub-agent Integration:**
  - The root agent must import sub-agents to enable collaboration. For example:
  ```python
  from .sub_agents.funny_nerd.agent import funny_nerd
  from .sub_agents.stock_analyst.agent import stock_analyst
  ```

- **Command Location:**
  - Always run `adk web` from the parent directory (e.g., the folder containing all agent packages), not from within an individual agent directory.

## Multi-Agent Architecture Options

ADK supports two primary approaches for building multi-agent systems:

### 1. Sub-Agent Delegation Model

In this model, the root agent delegates responsibility entirely to specialized sub-agents:

```python
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="You are a manager agent that delegates tasks to specialized agents...",
    sub_agents=[stock_analyst, funny_nerd],
)
```

**Characteristics:**
- Full delegation: the sub-agent’s response is final.
- The root agent acts as a router, directing queries to the appropriate specialist.

### 2. Agent-as-a-Tool Model

In this approach, specialized agents are wrapped using the `AgentTool` utility, allowing the root agent to use them as tools:

```python
from google.adk.tools.agent_tool import AgentTool

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="You are a manager agent that leverages specialized agents as tools...",
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)
```

**Characteristics:**
- The root agent integrates results from sub-agents while maintaining overall control.
- Multiple tool calls can be combined in a single response for a flexible interaction.

## Example Setup

In this multi-agent example, the manager agent collaborates with several specialized agents:

1. **Stock Analyst (Sub-agent):** Provides real-time market insights and financial data.
2. **Funny Nerd (Sub-agent):** Generates humorous, tech-focused commentary.
3. **News Analyst (Agent Tool):** Summarizes the latest technology news.

The manager agent routes user queries to the appropriate specialist based on context.

## Getting Started

Before running the multi-agent system, ensure you have the following setup:

1. **Activate the Virtual Environment**
   ```bash
   # On macOS/Linux:
   source ../.venv/bin/activate
   # On Windows CMD:
   ..\.venv\Scripts\activate.bat
   # On Windows PowerShell:
   ..\.venv\Scripts\Activate.ps1
   ```

2. **Configure API Keys**
   - Rename `.env.example` to `.env` in the root agent folder.
   - Add your Google API key to the `GOOGLE_API_KEY` variable in the `.env` file.

## Running the Example

1. Navigate to the parent directory containing your agent folders.
2. Start the interactive web UI by running:
   ```bash
   adk web
   ```
3. Open the provided URL (typically http://localhost:8000) in your browser.
4. Select the "manager" agent from the UI dropdown menu.
5. Begin interacting with your agent using the text input.

### Troubleshooting

If the multi-agent setup does not appear correctly:
- Confirm that you are running `adk web` from the correct parent directory (e.g., the directory containing all agent packages).
- Verify that each agent's `__init__.py` correctly imports its respective `agent.py` file.
- Ensure the root agent properly imports and integrates all sub-agents.

### Sample Prompts

- "What are the latest stock market trends?"
- "Tell me a funny programming joke."
- "Give me the latest tech news."
- "What time is it?"

## Additional Resources

- [ADK Multi-Agent Systems Documentation](https://google.github.io/adk-docs/agents/multi-agent-systems/)
- [Agent Tools Documentation](https://google.github.io/adk-docs/tools/function-tools/#3-agent-as-a-tool)

