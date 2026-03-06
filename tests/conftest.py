import pytest
import os
import sys
from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Browser
import allure
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.config import HEADLESS, BROWSER, BASE_URL, EMAIL, PASSWORD
from pages.login_Page import loginPage

     
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        if BROWSER == "chrome":
            browser = p.chromium.launch(channel="chrome", headless=HEADLESS)
        elif BROWSER == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)
        elif BROWSER == "edge":
            browser = p.chromium.launch(channel="edge", headless=HEADLESS)
        
        else:
            raise ValueError(f"Invalid BROWSER value: {BROWSER}. Must be 'chromium', 'firefox', or 'edge'.")

        yield browser
        browser.close()
    

@pytest.fixture(scope="session")
def context(browser:Browser):
    context = browser.new_context(viewport=None)
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    page.goto(f"{BASE_URL}login", wait_until="networkidle", timeout=60000)
    loginPageData = loginPage(page)
    loginPageData.login_with_valid_credentials()
    page.wait_for_timeout(timeout=5000)

    yield page


@pytest.fixture(scope="session")
def shared_data():
    """Dictionary shared across feature files."""
    return {}

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     # 🔥 capture on SETUP or CALL failure
#     if rep.failed and rep.when in ("setup", "call"):
#         page = item.funcargs.get("page", None)

#         if page:
#             try:
#                 if not page.is_closed():
#                     screenshot = page.screenshot(full_page=True)
#                     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#                     allure.attach(
#                         screenshot,
#                         name=f"{item.name}_{rep.when}_FAIL_{timestamp}",
#                         attachment_type=allure.attachment_type.PNG
#                     )
#             except Exception as e:
#                 print("Screenshot capture failed:", e)