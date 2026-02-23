from pages.base_page import BasePage
class listTask(BasePage):

    task_list = "//ul[contains(@id,'sortable')]//div[contains(@class,'task-name')]"
    task_detail = "//div[@class='aU_task_otr show_rightMdl']"
    task_name = "//div[@class='aU_task_otr show_rightMdl']//div[contains(@class,'t_header')]//input[@type='text']"
    functional_name = "//label[normalize-space()='Functional Type']/following-sibling::select"
    task_status = "//label[normalize-space()='Task Status']/following-sibling::select"
    is_completed = "//div[@class='aU_task_otr show_rightMdl']//div[contains(@class,'t_header')]/button[contains(@class,'btn')]"

    def get_task(self, task_id: str) -> str:
        return f"//div[contains(@id,'{task_id}')]"

    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)

    def get_task_list_id(self):

        '''Getting list id's of every task'''

        self.page.wait_for_load_state("domcontentloaded")
        lists = self.page.locator(self.task_list).all()
        list_id = []

        for task in lists:
            id  = task.get_attribute("id")
            list_id.append(id)

        return list_id
    

    def access_each_task(self):
        ''' 
        Access all tasks
        Getting counts of completed tasks
        Getting counts of tasks status - OnGoing/AsRisk/Delayed
        Getting counts of functional type counts
        Getting counts of total tasks
        
        '''
        ids = self.get_task_list_id()
        task_count_by_functional_status = {}

        for task_id in ids:

            # Accessing every task
            xpath = self.get_task(task_id)
            task = self.page.locator(xpath)
            task.wait_for(state="visible")
            task.click()

            # Getting task status complete/incomplete count
            task_complete_status = self.page.locator(self.is_completed)
            task_complete_status.wait_for(state="visible")
            status_text = task_complete_status.inner_text()
            if status_text == "Completed":
                task_count_by_functional_status[status_text] = task_count_by_functional_status.get(status_text, 0)+1

            # Getting task status on time/ at risk/ delayed count
            taskStatus = self.page.locator(self.task_status)
            taskStatus.wait_for(state="visible")
            status = taskStatus.locator("option:checked").inner_text()
            if status_text !="Completed":
                task_count_by_functional_status[status] = task_count_by_functional_status.get(status, 0)+1
            
            # Getting function type count
            task_func_name = self.page.locator(self.functional_name)
            task_func_name.wait_for(state="visible")
            func_text = task_func_name.locator("option:checked").inner_text()
            if func_text:
                task_count_by_functional_status[func_text] = task_count_by_functional_status.get(func_text, 0)+1
            else:
                task_count_by_functional_status["empty"] = task_count_by_functional_status.get("empty", 0)+1

            # String total tasks counts  
            task_count_by_functional_status["total tasks"] = task_count_by_functional_status.get("total tasks", 0)+1
            
            # Getting completed tasks count
            if status_text == "Completed":
                completedFunc = f"{func_text.replace(" ", "_").strip()}_completed"
                task_count_by_functional_status[completedFunc] = task_count_by_functional_status.get(completedFunc, 0)+1

        return task_count_by_functional_status
