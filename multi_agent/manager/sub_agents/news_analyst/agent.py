from google.adk.agents import Agent
from google.adk.tools import google_search

news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="An agent to for news analyst",
    instruction="""
        You're a helpful assistant that can analyze news articles and provide summary of the news,
        When asked about news, you should use the google_search tool to search for the news.
        
        If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
        """,
    tools=[google_search]
)