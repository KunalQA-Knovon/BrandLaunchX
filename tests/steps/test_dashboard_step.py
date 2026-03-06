from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from pages.dashboard_page import DashboardPage
import logging
import allure
import math

logger = logging.getLogger(__name__)


@given("the user is on the Dashboard page")
def user_on_dashboard(page:Page, shared_data):
    with allure.step("User is on the Dashboard page"):
        page.goto(f"{BASE_URL}Dashboard", wait_until="networkidle")

@then("the Cost Impact value should be displayed")
def cost_impact_displayed(page:Page, shared_data):
    with allure.step("Validating Cost Impact value is displayed"):
        dashboardPage = DashboardPage(page)        
        logger.info(f"cost: {dashboardPage.get_cost_impect()}")
        


@then("the Delay value should be displayed")
def delay_value_displayed(page:Page, shared_data):
    with allure.step("Validating Delay value is displayed"):
        dashboardPage = DashboardPage(page)
        timeDelay = int(dashboardPage.get_delay_impect())
        assert timeDelay >= 0, f"Total delayed time coming invalid: {timeDelay}"
        with allure.step("Total delayed time is visible and time showing"):
            logger.info(f"Total delayed time: {timeDelay}")


@then("the Launch Date should be displayed")
def launch_date_visible(page:Page):
    with allure.step("Validating Launch Date is displayed"):    
        dashboard = DashboardPage(page)
        date = dashboard.get_Launch_date()
        expect(date).to_be_visible()
        allure.step("Launch is matching with actual launch date")


@then("the Launch Date should match with actual launch date")
def launch_date_format(page:Page):
    with allure.step("Validating Launch Date is displayed"):
        dashboard = DashboardPage(page)
        date = dashboard.get_Launch_date()
        logger.info(date)
        expect(date).to_have_text("1 Feb, 2030")

@then("the total tasks card should be visible")
def total_tasks_card_visible(page: Page):
    dashboardPage = DashboardPage(page)
    totalTasks = int(dashboardPage.total_task_count())
    assert totalTasks >= 0, f"Total tasks count invalid: {totalTasks}"
    with allure.step("Total task card is visible and count showing"):
        logger.info(f"Total tasks card count: {totalTasks}")

@then("the total tasks card count should match with tasks list")
def total_tasks_card_count(page: Page, shared_data):
    with allure.step("Validate total tasks count from task list"):
        dashboardPage = DashboardPage(page)
        list_data = shared_data.get("task_list")
        assert list_data is not None, "Task list data not captured!"
        expectedTotalCount = list_data["total_tasks"]
        actualTotalTasks = dashboardPage.total_task_count()
        assert int(actualTotalTasks) == expectedTotalCount,(
            f"Total task counts not matched. Expected {expectedTotalCount}, got {actualTotalTasks}")


@then("the completed tasks card should be visible")
def completed_tasks_card_visible(page: Page):
    dashboardPage = DashboardPage(page)
    completedTasks = int(dashboardPage.completed_task_count())
    assert completedTasks >= 0, f"Completed tasks count invalid: {completedTasks}"
    with allure.step("Completed task card is visible and count showing"):
        logger.info(f"Completed tasks card count: {completedTasks}")

@then("the completed tasks card count should match with tasks list")
def completed_tasks_card_count(page: Page, shared_data):
    with allure.step("Validate completed tasks count from task list"):
        dashboardPage = DashboardPage(page)
        list_data = shared_data.get("task_list")
        assert list_data is not None, "Task list data not captured!"
        expectedCompletedCount = list_data["Completed"]
        actualCompletedTasks = dashboardPage.completed_task_count()
        assert int(actualCompletedTasks) == expectedCompletedCount,(
            f"Completed task counts not matched. Expected {expectedCompletedCount}, got {actualCompletedTasks}")


@then("the ongoing tasks card should be visible")
def ongoing_tasks_card_visible(page: Page):
    dashboardPage = DashboardPage(page)
    actualOnGoingTasks = int(dashboardPage.ongoing_task_count())
    assert actualOnGoingTasks >= 0, f"Ongoing tasks count invalid: {actualOnGoingTasks}"
    with allure.step("Ongoing task card is visible and count showing"):
        logger.info(f"Ongoing tasks card count: {actualOnGoingTasks}")




@then("the ongoing tasks card count should match with tasks list")
def ongoing_tasks_card_count(page: Page, shared_data):

    allure.dynamic.feature("Dashboard")
    allure.dynamic.story("Summary Cards")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("component", "Dashboard")
    allure.dynamic.label("type", "Smoke")
    allure.dynamic.label("owner", "QA-Team")

    with allure.step("Validate ongoing tasks count from task list"):
        dashboardPage = DashboardPage(page)
        list_data = shared_data.get("task_list")
        assert list_data is not None, "Task list data not captured!"
        expectedOnGoingCount = list_data["On Time"]
        actualOnGoingTasks = dashboardPage.ongoing_task_count()
        assert int(actualOnGoingTasks) == expectedOnGoingCount,(
            f"Completed task counts not matched. Expected {expectedOnGoingCount}, got {actualOnGoingTasks}"
            )


@then("the at risk tasks card should be visible")
def at_risk_tasks_card_visible(page: Page):
    dashboardPage = DashboardPage(page)
    actualatRiskTasks = int(dashboardPage.atRisk_task_count())
    assert actualatRiskTasks >= 0, f"AtRisk tasks count invalid: {actualatRiskTasks}"
    with allure.step(f"At Risk task card is visible and count showing: {actualatRiskTasks}"):
        logger.info(f"At Risk tasks card count: {actualatRiskTasks}")


@then("the at risk tasks card count should match with tasks list")
def at_risk_tasks_card_count(page: Page, shared_data):
    
    dashboardPage = DashboardPage(page)
    list_data = shared_data.get("task_list")
    assert list_data is not None, "Task list data not captured!"
    expectedRiskCount = list_data["At Risk"]
    actualRiskTasks = dashboardPage.atRisk_task_count()
    with allure.step(f"Validate risk tasks count from task list. Expected counts: {expectedRiskCount}, Actual counts: {actualRiskTasks}"):
        assert int(actualRiskTasks) == expectedRiskCount,(
            f"Completed task counts not matched. Expected {expectedRiskCount}, got {actualRiskTasks}")


@then(parsers.parse('the function "{function_name}" should be displayed'))
def validate_function_displayed(page: Page, function_name):
    dashboard = DashboardPage(page)
    data = dashboard.get_table_data()

    assert function_name in data, f"{function_name} not found in dashboard"
    logger.info(f"{function_name} passed")


@then(parsers.parse('the total task count for "{function_name}" should match with task list'))
def validate_task_count(page: Page, function_name, shared_data):
    dashboard = DashboardPage(page)
    listData = shared_data.get("task_list")
    assert listData is not None, "Task list data not captured!"
    listCount = int(listData[function_name])
    data = dashboard.get_table_data()
    dashboardCount = int(data[function_name]["total_task"])
    assert dashboardCount==listCount, f"Count of {function_name} not matched. Expected count: {listCount}, got: {dashboardCount}"
    

@then(parsers.parse('the completed percentage for "{function_name}" should be match between 0 and 100'))
def validate_percentage(page: Page, function_name, shared_data):
    dashboard = DashboardPage(page)
    listData = shared_data.get("task_list") or {}

    # Always return 0 if key not found
    funcTotalCount = int(listData.get(function_name.strip(), 0))
    funcCompletedCount = int(listData.get(f"{function_name.strip()}_completed", 0))

    if funcCompletedCount == 0:
        finalPer = float(0)
    finalPer = round(((funcCompletedCount/funcTotalCount)*100),1)
    data = dashboard.get_table_data()
    funcPercentage = float(data[function_name]["percentage"])
    logger.info(f"{finalPer} vs {funcPercentage}")
    assert finalPer==funcPercentage, f"Count of {function_name} not matched. Expected count: {finalPer}, got: {funcPercentage}"


@then("the sum of Completed, Ongoing, delayed and At Risk tasks should be equal to Total Tasks")
def calculate_total_counts_of_tasks(page:Page,shared_data):
    with allure.step("Matching sum of Completed, Ongoing, delayed and At Risk tasks with total tasks count"):
        list_data = shared_data.get("task_list")
        assert list_data is not None, "Task list data not captured!"
        onTime = int(list_data["On Time"])
        atRisk = int(list_data["At Risk"])
        completed = int(list_data["Completed"])
        delayed = int(list_data["Delayed"])

        totalCount =  onTime+atRisk+completed+delayed
        total_tasks = int(list_data["total_tasks"])
        assert totalCount==total_tasks, f"Total tasks count not matched. Expected{total_tasks}, got{totalCount}"
        