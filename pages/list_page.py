from pages.base_page import BasePage
import allure
from utils.screenshotUtils import take_screenshot


class listTask(BasePage):

    task_list = "//ul[contains(@id,'sortable')]//div[contains(@class,'task-name')]"
    task_detail = "//div[contains(@class,'aU_task_otr') and contains(@class,'show_rightMdl')]"
    task_name = "//div[contains(@class,'t_header')]//input[@type='text']"
    functional_name = "//label[normalize-space()='Functional Type']/following-sibling::select"
    task_status = "//label[normalize-space()='Task Status']/following-sibling::select"
    is_completed = "//div[contains(@class,'t_header')]/button[contains(@class,'btn')]"

    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)

    def get_task(self, task_id: str) -> str:
        return f"//div[contains(@id,'{task_id}')]"

    def get_task_list_id(self):
        """Get all available task IDs"""
        with allure.step("Get task list IDs"):
            self.page.wait_for_load_state("domcontentloaded")
            tasks = self.page.locator(self.task_list).all()

            return [
                task.get_attribute("id")
                for task in tasks
                if task.get_attribute("id")
            ]

    def access_each_task(self):
        """
        Access each task and collect:
        - Total tasks
        - Completed tasks
        - Task status counts
        - Functional type counts
        """
        task_ids = self.get_task_list_id()
        task_counts = {}

        for index, task_id in enumerate(task_ids, start=1):
            with allure.step(f"Process Task {index} | ID: {task_id}"):

                try:
                    # Open task
                    task = self.page.locator(self.get_task(task_id))
                    task.wait_for(state="visible", timeout=5000)
                    task.click()

                    # ---- Completion Status ----
                    complete_btn = self.page.locator(self.is_completed)
                    complete_btn.wait_for(state="visible", timeout=5000)
                    complete_status = complete_btn.inner_text().strip()

                    if complete_status == "Completed":
                        task_counts["Completed"] = task_counts.get("Completed", 0) + 1

                    # ---- Task Status ----
                    status_dd = self.page.locator(self.task_status)
                    status_dd.wait_for(state="visible", timeout=5000)
                    status_text = status_dd.locator("option:checked").inner_text().strip()

                    if complete_status != "Completed":
                        task_counts[status_text] = task_counts.get(status_text, 0) + 1

                    # ---- Functional Type ----
                    func_text = "empty"
                    try:
                        func_dd = self.page.locator(self.functional_name)
                        func_dd.wait_for(state="visible", timeout=5000)
                        func_text = func_dd.locator("option:checked").inner_text().strip()

                        task_counts[func_text] = task_counts.get(func_text, 0) + 1
                    except Exception:
                        take_screenshot(self.page, "functional_type_error")
                        task_counts["functional_error"] = task_counts.get("functional_error", 0) + 1

                    # ---- Total Tasks ----
                    task_counts["total_tasks"] = task_counts.get("total_tasks", 0) + 1

                    # ---- Completed by Functional Type ----
                    if complete_status == "Completed":
                        completed_key = f"{func_text}_completed"
                        task_counts[completed_key] = task_counts.get(completed_key, 0) + 1

                except Exception as e:
                    take_screenshot(self.page, f"task_failed_{task_id}")
                    self.logger.error(f"Task ID {task_id} failed: {str(e)}")
                    task_counts["task_failed"] = task_counts.get("task_failed", 0) + 1

        return task_counts