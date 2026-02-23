from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from utils.config import BASE_URL


@given("the user is on the initials task page")
def open_initialTask(page: Page):
    page.goto(f"{BASE_URL}InitialTasks", wait_until="networkidle")