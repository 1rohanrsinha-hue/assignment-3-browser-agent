import asyncio
from browser_use import Agent
from browser_use.llm import ChatOllama

asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def main():
    llm = ChatOllama(model="llama3:8b")

    agent = Agent(
        task="Open google and search for AI engineering internships",
        llm=llm,
    )

    await agent.run()

asyncio.run(main())