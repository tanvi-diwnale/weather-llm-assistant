from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from app.tools.weather_tool import get_weather
from app.config import OPENROUTER_API_KEY
from app.config import OPENROUTER_API_KEY

print("DEBUG OPENROUTER KEY LOADED:", OPENROUTER_API_KEY)

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=OPENROUTER_API_KEY,
    temperature=0
)

weather_tool = Tool(
    name="Weather Tool",
    func=get_weather,
    description="Get current weather of a city"
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
