from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from utils.config import BASE_URL
import logging
from pages.overview_page import overview
logger = logging.getLogger(__name__)

@given("the user is on the overview detail page")
def open_overview(page: Page, shared_data):
    page.goto(f"{BASE_URL}Overview")
    overview_data = overview(page)
    at_risk_count = overview_data.get_at_risk_count()
    delay_count = overview_data.get_delay_count()

    finished_per = overview_data.get_task_finish_perc()
    logger.info(f"finished percentage: {finished_per}")

    budget_perc = overview_data.get_budget_utilised_perc()
    logger.info(f"budget perc: {budget_perc}")

    task_detail = shared_data.get("task_list")
    assert task_detail is not None, "Task list data not captured!"

    for task_key, task_value in task_detail.items():
        logger.info(f"task details on overview: {task_key} : {task_value}")