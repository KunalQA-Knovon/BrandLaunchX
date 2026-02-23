from pytest_bdd import given, then
from playwright.sync_api import Page
from utils.config import BASE_URL
from pages.dashboard_page import DashboardPage
import logging

logger = logging.getLogger(__name__)

@given("the user is on the dashboard page")
def open_dashboard(page: Page, shared_data):
    page.goto(f"{BASE_URL}Dashboard", wait_until="networkidle")
    dashboardPage = DashboardPage(page)

    # counrty_data = dashboardPage.get_country_wise_data()
    # logger.info(f"country detail: {counrty_data}")

    # Reuse dict captured from task list
    task_list_data = shared_data.get("task_list")
    assert task_list_data is not None, "Task list data not captured!"

    totalTasks = dashboardPage.total_task_count()
    completedTasks = dashboardPage.completed_task_count()
    onGoingTasks = dashboardPage.ongoing_task_count()
    atRiskTasks = dashboardPage.atRisk_task_count()

    # validate list data against dashboard table data
    dashboard_list_data = dashboardPage.get_table_data()
    logger.info(f"dashboard detail: {dashboard_list_data}")

    for task_name in task_list_data.items():
        logger.info(f"task details on dashboard: {task_name}")
    

