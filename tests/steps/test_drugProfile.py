from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from utils.config import BASE_URL


@given("the user is on the Drug Profile page")
def open_drugProfile(page: Page):
    page.goto(f"{BASE_URL}DrugProfile", wait_until="networkidle")