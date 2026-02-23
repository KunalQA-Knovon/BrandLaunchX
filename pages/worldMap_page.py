import allure
from utils.config import BASE_URL
from pages.base_page import BasePage

class WorldMapPage(BasePage):

    country_value_locator = "select.custom-select"
    sequence_locator = "//input[@id='countrySeq']"
    date_locator = "input[name='launchDate']"
    launch_budget_locator = "input[name='budget']"
    currency_locator = "[name='budgetCode']"
    revenue_locator = "input[name='forecastBudget']"

    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)

    @allure.step("Verify World Map page URL")
    def verify_world_map_page(self):
        self.logger.info(f"User is on: {BASE_URL}WorldMapData")
        self.assert_url(f"{BASE_URL}WorldMapData")

    # ---------- Actions ----------

    @allure.step("User selected country: {country}")
    def select_country(self, country: str):
        self.logger.info(f"User selected the country: {country}")
        self.selectValue(self.country_value_locator, country)
        
    @allure.step("User entered sequence: {value}")
    def enter_sequence_number(self, value: str):
        self.logger.info(f"User enter sequence: {value}")
        self.fill_by_locator(self.sequence_locator, value)

    @allure.step("User enter launch date: {date}")
    def select_launch_date(self, date: str):
        self.logger.info(f"User enter launch date: {date}")
        self.fill_by_locator(self.date_locator, date)
    
    @allure.step("User enter launch budget: {amount}")
    def enter_launch_budget(self, amount: str):
        self.logger.info(f"User enter launch budget: {amount}")
        self.fill_by_locator(self.launch_budget_locator, amount)

    @allure.step("User select currency: {currency}")
    def select_launch_budget_currency(self, currency: str):
        self.logger.info(f"User select currency: {currency}")
        self.selectValue(self.currency_locator, currency)

    @allure.step("User entered forecast revenue: {amount}")
    def enter_revenue_forecast(self, amount: str):
        self.logger.info(f"User entered forecast revenue: {amount}")
        self.fill_by_locator(self.revenue_locator, amount)
    