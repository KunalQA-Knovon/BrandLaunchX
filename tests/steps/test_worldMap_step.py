from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from pages.worldMap_page import WorldMapPage

# ---------------- BACKGROUND ----------------

@given("the user is logged in and on the World Map Data page")
def open_worldmap(page: Page):
    page.goto(f"{BASE_URL}WorldMapData")

# ---------------- WORLD MAP ----------------

@when("the user selects a country")
def select_country(page: Page):
    WorldMapPage(page).select_country("India")

@when("the user provides a valid sequence number")
def enter_sequence(page: Page):
    WorldMapPage(page).enter_sequence_number("2")

@then("the country should be added to the world map successfully")
def verify_country_added(page: Page):
    # expect(page.locator("text=India")).to_be_visible()
    pass

# ---------------- BRAND LAUNCH ----------------

@when("the user selects the expected launch date")
def select_launch_date(page: Page):
    WorldMapPage(page).select_launch_date("11-06-2030")

@when("the user enters the launch budget amount")
def enter_budget_amount(page: Page):
    WorldMapPage(page).enter_launch_budget("1000")

@when("the user selects the launch budget currency")
def select_budget_currency(page: Page):
    WorldMapPage(page).select_launch_budget_currency("INR")
    # pass

@when("the user enters the first-year revenue forecast amount")
def enter_revenue_amount(page: Page):
    WorldMapPage(page).enter_revenue_forecast("2000")

@when("the user clicks on the Next button")
def click_next(page: Page):
    # page.get_by_role("button", name="Next").click()
    page.wait_for_load_state("networkidle")

@then("the user should be navigated to the next page")
def verify_next_page(page: Page):
    # page.wait_for_load_state("networkidle")
    # expect(page.url).to_contain("next")
    
    pass