from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI



async def main():
    agent = Agent(
        task="""
            open website http://qa.way2automation.com
            then Enter name as Rahul Kumar
            then Enter phone number as 9876453545
            then enter email as trainer@way2automation.com
            then select country guyana
            then Enter city Mumbai
            then Enter username admin
            then enter password
            then Click on submit button
            then Check what message is coming and print the message
            """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
                                   api_key="AIzaSyBXbSq1m50QHmKCfrNpVybqA9SkiV0DlLk")
    )
    await agent.run()


asyncio.run(main())
