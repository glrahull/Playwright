import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.set_viewport_size({"width":1920,"height":1080})
    yield page
    page.wait_for_timeout(3000)
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()