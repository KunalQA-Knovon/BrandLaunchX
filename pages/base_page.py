from playwright.sync_api import expect, Page
from utils.logger import get_logger

class BasePage:
    def __init__(self, page:Page, logger_name=None):
        self.page = page

        name = logger_name if logger_name else self.__class__.__name__
        self.logger = get_logger(name)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.logger.info(f"User navigated to: {url}")
        self.page.goto(url)

    def click(self, locator: str):
        try:
            element = self.page.locator(locator)
            element.wait_for(state="visible")
            element.click()
        except Exception as e:
            self.logger.info(f"Failed to check this {locator}: {e}")
        
    def fill_by_locator(self, locator: str, value):
        try:
            element = self.page.locator(locator)
            element.fill(value)
        except Exception as e:
            self.logger.info(f"Failed to check this {locator}: {e}")

    def fill_by_role(self, role: str, name: str, value):
        try:
            element = self.page.get_by_role(role, name=name)
            element.fill(value)
        except Exception as e:
            self.logger.error(f"Failed to fill role={role}, name={name}: {e}")
            raise

    def fill_by_placeholder(self, placeholder: str, value):
        try:
            element = self.page.get_by_placeholder(placeholder)
            element.fill(value)
        except Exception as e:
            self.logger.error(f"Failed to fill placeholder={placeholder}: {e}")
            raise

    def selectValue(self, locator, value):
        self.page.locator(locator).select_option(value=value)

    def get_text(self, locator: str) -> str:
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=10000)
        return element.text_content()

    def wait_for_visible(self, locator: str):
        self.page.locator(locator).wait_for(state="visible")

    def assert_title(self, title: str):
        expect(self.page).to_have_title(title)

    def assert_url(self, url: str):
        expect(self.page).to_have_url(url)
