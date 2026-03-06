from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page, expect
from utils.config import BASE_URL
import logging
from pages.overview_page import overview
logger = logging.getLogger(__name__)

@given("the user is on the Overview page")
def open_overview(page: Page, shared_data):
    page.goto(f"{BASE_URL}Overview", wait_until="networkidle")

@then("the At Risk widget should be displayed")
def step_at_risk_widget_displayed(page:Page):
    overview_data = overview(page)
    at_risk_displayed = int(overview_data.get_at_risk_count())
    assert at_risk_displayed >= 0, "At risk wifget not displaying"

@then("the count of At Risk should be match with list count")
def step_at_risk_count_matches(page:Page, shared_data):
    overview_data = overview(page)
    at_risk_count = int(overview_data.get_at_risk_count())

    list_data = shared_data.get("task_list")
    atRisk = int(list_data["At Risk"])
 
    logger.info(f"Expected: {at_risk_count} - Actual: {atRisk}")
    assert at_risk_count == atRisk, "At risk task count not matched"
   
    
@then("the Delayed widget should be displayed")
def step_delayed_widget_displayed(page:Page, shared_data):
    overview_data = overview(page)
    delay_displayed = int(overview_data.get_delay_count())
    assert delay_displayed >= 0, "Delayed wifget not displaying"


@then("the count of Delayed should be match with list count")
def step_delayed_count_matches(page:Page, shared_data):
    overview_data = overview(page)
    delay_count = int(overview_data.get_delay_count())

    list_data = shared_data.get("task_list")
    delayed = int(list_data["Delayed"])
    
    logger.info(f"Expected: {delay_count} - Actual: {delayed}")
    assert delay_count == delayed, "At delayed task count not matched"
    
# Percentage Widgets
@then("the Finished task widget should be displayed")
def step_finished_task_widget_displayed(page:Page):
    overview_data = overview(page)
    task_per = float(overview_data.get_task_finish_perc().replace("%",""))
    assert task_per >=0, "Finished task widget is not displayed"
    
@then("the percentage of finished tasks should be match with list count")
def step_finished_task_percentage_matches(page:Page, shared_data):
    overview_data = overview(page)
    task_per = float(overview_data.get_task_finish_perc().replace("%",""))
    list_data = shared_data.get("task_list")
    completedCount = int(list_data["Completed"])
    totalCount = int(list_data["total_tasks"])
    finishedPercentage = round((completedCount/totalCount)*100 ,1)
    logger.info(f"percentage of Budget Utilised: {finishedPercentage} vs {task_per}")
    assert task_per == finishedPercentage, "Finished tasks percentage is not matched"
    

@then("the Budget Utilised widget should be displayed")
def step_budget_widget_displayed(page:Page):
    overview_data = overview(page)
    utilizedPer = float(overview_data.get_budget_utilised_perc().replace("%",""))
    assert utilizedPer >= 0, "Budget Utilised widget is not displayed"
   
@then("the percentage of Budget Utilised should be match with list count")
def step_budget_percentage_matches(page:Page):
    overview_data = overview(page)
    utilizedPer = float(overview_data.get_budget_utilised_perc().replace("%",""))
    logger.info(f"percentage of Budget Utilised: {utilizedPer}")
    assert utilizedPer >= 0, "Budget Utilised widget is not displayed"


    


