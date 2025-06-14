import json

import pytest
from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from patchright.async_api import async_playwright


@pytest.mark.asyncio
async def test_way2automation():
    agent = Agent(
        task="""
                Identify and return the HTML element locators (CSS and XPATH) in strict JSON format ONLY
                for the following form fields on https://demo.wpeverest.com/user-registration/online-event-registration-form/, the output should be a valid JSON object without extra text
                and create CSS with attribute and value, like:
                {
                    "First Name": "CSS_SELECTOR",
                    "Last Name": "CSS_SELECTOR",
                    "User Name": "CSS_SELECTOR",
                    "User Password": "CSS_SELECTOR"        
                }
                """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
                                   api_key="AIzaSyBXbSq1m50QHmKCfrNpVybqA9SkiV0DlLk")
    )
    result = await agent.run()
    final_result = result.final_result()
    print(final_result)

    try:
        final_result = json.loads(final_result)
    except json.JSONDecodeError:
        raise  ValueError(f"Invalid JSON Response from AI: {final_result}")

    print("Extracted Locators are : ", final_result)


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.wpeverest.com/user-registration/online-event-registration-form/")

        await page.fill(final_result["First Name"], value="Rahul")
        await page.fill(final_result["Last Name"], value="Kumar")
        await page.fill(final_result["User Name"], value="Rahul@way2automation.com")
        await page.fill(final_result["User Password"], value="sdjifjnfe")

        await page.wait_for_timeout(3000)
        await browser.close()