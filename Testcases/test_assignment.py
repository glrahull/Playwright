from playwright.sync_api import sync_playwright

def test_1st_search(page):
    page.goto("http://www.google.com")
    page.locator("#APjFqb").fill("way2automation")
    page.locator("button").filter(has_text="Google Search").click()
    link = page.locator("/html/body/div[3]/div/div[12]").all()

    print(f"Total values are : {len(link)}")

def test_make_mytrip(page):
    page.goto("https://makemytrip.com")
    page.wait_for_timeout(5000)
    options = page.locator("//input[@type='text']").all()
    print(f"Total values are : {len(options)}")

    for option in options:
        text = option.inner_text()
        lang= option.get_attribute("lang")
        print(f"{text}---{lang}")