import pytest
import os
import sys
from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser

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
    context = browser.new_context()
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
