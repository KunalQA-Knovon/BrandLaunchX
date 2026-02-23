
import os
import sys
import allure

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pages.base_page import BasePage
from utils.config import BASE_URL, EMAIL, PASSWORD

class loginPage(BasePage):

    usernameLocator="input[type=email]"
    passwordLocator = "input[type=password]"
    loginButtonLocator ='button:has-text("Login")'

    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)

    def enterUsername(self, username):
        self.fill_by_locator(self.usernameLocator, username)
    
    def enterPassword(self, password):
        self.fill_by_locator(self.passwordLocator, password)

    def loginButton(self):
        self.click(self.loginButtonLocator)

    def open_login_page(self):
        self.navigate(f"{BASE_URL}login")
    
    def login_with_valid_credentials(self):
        self.enterUsername(EMAIL)
        self.enterPassword(PASSWORD)
        self.loginButton()