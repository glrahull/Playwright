import os.path

from playwright.sync_api import Page, expect, Browser


def test_first_example(page):
    # page.set_viewport_size({"width":1080,"height":720})
    page.goto("https://insureefficient.com")
    title = page.title()
    print(title)
    assert "Insure Efficient" in title
    page.wait_for_timeout(2000)
    page.goto("https://gmail.com")
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()


def test_finding_element(page):
    page.goto("http://gmail.com")
    # page.locator("[name= 'identifier']").fill("trainer@way2automation.com")
    page.get_by_label('Email or phone', exact=True).fill("trainer@way2automation.com")
    # page.locator("button:has-text('Next')").click()
    page.locator("button").filter(has_text="Next").click()
    page.get_by_label("Enter your password").fill("sdrfffedd", timeout=5000)

    page.locator("//*[@id='passwordNext']/div/button/span").click()
    error_message = page.locator(
        "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[2]/div[2]/span").inner_text()
    print(error_message)
    assert "Wrong password" in error_message
    page.wait_for_timeout(2000)


def test_handling_dropdown(page):
    page.goto("https://www.wikipedia.org/")
    # page.select_option("select",label="Eesti")
    # page.select_option("select", value="hi")
    # page.select_option("select", index=0)
    page.wait_for_timeout(5000)

    options = page.locator("option").all()
    print(f"Total values are : {len(options)}")

    for option in options:
        text = option.inner_text()
        lang = option.get_attribute("lang")
        print(f"{text}---{lang}")


def test_handling_links(page):
    page.goto("https://www.wikipedia.org/")
    links = page.locator("a").all()
    print(f"Total values are : {len(links)}")

    for link in links:
        text = link.inner_text()
        url = link.get_attribute("lang")
        print(f"{text}---{url}")


def test_checkboxes(page):
    page.goto("http://tizag.com/html/htmlcheckboxes.php")

    block = page.locator("//table/tbody/tr/td/div[4]")
    checkboxes = block.locator("[name='sports']")
    checkboxes_count = checkboxes.count()
    print(checkboxes_count)

    for i in range(checkboxes_count):
        checkboxes.nth().click()


def test_assertions(page):
    page.goto("https://www.dofactory.com/html/input/checkbox")

    expect(page).to_have_url("https://www.dofactory.com/html/input/checkbox")
    print("Url Assertion passed")

    expect(page).not_to_have_url("error")
    print("No errors on the page hence passed")

    expect(page).to_have_title("HTML Tutorial - Checkboxes")
    print("Title assertion passed")

    link = page.locator("/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[5]/div/form/fieldset")
    expect(link).to_have_text("/tutorial/action.html")
    print("Text assertion passed")

    checkbox = page.locator("//div[4]/input[1]")
    expect(checkbox).to_be_visible()
    print("Checkbox is visible")

    expect(checkbox).to_be_checked()
    print("Checkbox is checked")


def test_webtables(page):
    page.goto("https://money.rediff.com/indices/nse/NIFTY-50?src=moneyhome_nseIndices")

    row_count = page.locator("dataTable").count()
    print("Row count is : ", row_count)

    col_count = page.locator(".index-data-wrapper > table > tbody >tr:nth-child(1) > td").count()
    print("Col count is : ", col_count)


def test_shadowroot(page):
    page.goto("chrome://downloads/")

    page.locator("#searchInput").fill("Rahul")


def test_mouseover(page):
    page.goto("https://www.way2automation.com/")

    page.locator("//*[@id='menu-item-27580']/a/span[2]").hover()
    page.locator("//*[@id='menu-item-27592']/a/span[2]").click()


def test_slider(page):
    page.goto("https://jqueryui.com/resources/demos/slider/default.html")
    slider = page.locator("#slider > span")

    page.wait_for_timeout(3000)
    bounding_box = slider.bounding_box()
    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box["y"] + bounding_box["height"] / 2
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x + 400, start_y)
    page.mouse.up()


def test_resizable(page):
    page.goto("https://jqueryui.com/resources/demos/resizable/default.html")
    slider = page.locator("#resizable")

    page.wait_for_timeout(3000)
    bounding_box = slider.bounding_box()
    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box["y"] + bounding_box["height"] / 2
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x + 400, start_y + 400)
    page.mouse.up()


def test_resizable(page):
    page.goto("https://jqueryui.com/resources/demos/droppable/default.html")
    draggable = page.locator("#draggable")
    droppable = page.locator("#droppable")

    page.wait_for_timeout(3000)

    draggable_box = draggable.bounding_box()
    droppable_box = droppable.bounding_box()
    page.mouse.move(
        draggable_box["x"] + draggable_box["width"] / 2,
        draggable_box["y"] + draggable_box["height"] / 2
    )
    page.mouse.down()

    page.mouse.move(
        droppable_box["x"] + draggable_box["width"] / 2,
        draggable_box["y"] + draggable_box["height"] / 2
    )
    page.mouse.up()


def test_right_click(page):
    page.goto("https://deluxe-menu.com/popup-mode-sample.html")
    page.locator("//p[2]/img").click(button="right")


def test_alert(page):
    def dialog_handler(dialog):
        page.wait_for_timeout(2000)
        print(dialog.message)
        dialog.accept()

    page.goto("https:gmail.com")
    page.locator("[type='submi']").click()
    page.wait_for_timeout(2000)


def test_iframe(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit", timeout=60000)
    frame = page.frame_locator("#iframeResult")
    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Rahul")
    frame.locator("#lname").clear()
    frame.locator("#lname").fill("kumar")

    frame.locator("[type='submit']").click()


def test_tabsandpopup(page):
    page.goto("https://sso.teachable.com/secure/673/identity/sign_up/otp", timeout=60000)

    with page.expect_popup() as popup_info:
        page.locator("text=Privacy").nth(0).click()

    popup = popup_info.value
    popup.locator("//*@id='header-sign-up-btn']").click()
    popup.locator("#name").fill("trainer@way2automation.com")

    page.wait_for_timeout(3000)
    popup.close()

    page.wait_for_timeout(3000)


def test_javascript(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit", timeout=60000)
    page.wait_for_timeout(3000)
    frame = page.frame_locator("#iframeResult")
    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Rahul")
    frame.locator("#lname").clear()
    frame.locator("#lname").fill("kumar")
    frame.locator("[type='submit']").evaluate("(element) =>{element.style.border = '3px solid red';}")
    frame.locator("[type='submit']").screenshot(path="screenshot/element.png")
    page.wait_for_timeout(3000)
    page.screenshot(path="screenshot/page.png")
    # frame.locator("[type='submit']").click()


def test_http_authentication(page, browser: Browser):
    context = browser.new_context(
        http_credentials={"username": "admin", "password": "admi8n"}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth", timeout=60000)


def test_file_upload(page):
    page.goto("https://way2automation.com/way2auto_jquery/registration.php#load_box", timeout=60000)
    page.locator("#register_form > fieldset:nth-child(9) > input[type=file]").set_input_files(
        "C://Users/rahul/Downloads/DG_CCM4WAGENT_TPSCHEDULESC_D206499351_D206499351_1749531874386.pdf")
    page.wait_for_timeout(5000)


def test_multiple_file_upload(page):
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_fileupload_multiple", timeout=60000)
    frame = page.frame_locator("#iframeResult")
    frame.locator("#myFile").set_input_files([
        "C:\\Users/rahul\\Downloads\\DG_CCM4WAGENT_TPSCHEDULESC_D206499351_D206499351_1749531874386.pdf",
        "C:\\Users/rahul\\Downloads\\b91694da-b907-4754-8f15-a2b5d100c782.pdf"
    ])


def test_download_file(page, project_directory=None):
    page.goto("https://www.selenium.dev/downloads/", timeout=60000)

    with page.expect_download() as download_info:
        page.locator("body > div > main > div:nth-child(5) > div.col-sm-6.py-3.ps-0.pe-3 > div > div > p:nth-child(1) > a").click()

    download = download_info.value

    project_directory= os.path.join(os.path.dirname(os.getcwd()), "downloads")
    os.makedirs(project_directory, exist_ok=True)
    file_path = os.path.join(project_directory, "selenium.jar")
    download.save_as(file_path)

    print(f"file is downloaded to : {file_path}")
