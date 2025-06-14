import pytest
from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI


@pytest.mark.asyncio
async def test_way2automation():
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
                then verify the message contains "This is just a dummy form, you just clicked SUBMIT BUTTON"
                """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
                                   api_key="AIzaSyBXbSq1m50QHmKCfrNpVybqA9SkiV0DlLk")
    )
    result = await agent.run()
    final_result = result.final_result()
    print(final_result)

    expected_message = "This is not just a dummy form, you just clicked SUBMIT BUTTON"
    assert expected_message in final_result, f"Expected message not found! Actual result: {final_result}"
