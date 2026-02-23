from pytest_bdd import given, then
from playwright.sync_api import Page
from utils.config import BASE_URL
from pages.list_page import listTask
import logging

logger = logging.getLogger(__name__)

@given("the user is on the task list page")
def open_listTask(page: Page, shared_data):
    page.goto(f"{BASE_URL}List", wait_until="networkidle")
    tasks = listTask(page)
    data = tasks.access_each_task()
    shared_data["task_list"] = data