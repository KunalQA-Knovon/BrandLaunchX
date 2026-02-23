from pages.base_page import BasePage
class overview(BasePage):

    at_risk_task_indicator = "//div[contains(@class,'progress_1')]//h4[contains(@class,'m-auto')]"
    delay_task_indicator = "//div[contains(@class,'progress_2')]//h4[contains(@class,'m-auto')]"
    finished_impact_navigator = "//div[contains(@class,'progress_3')]//h4[contains(@class,'m-auto')]"
    budge_utilised_navigator = "//div[contains(@class,'progress_4')]//h4[contains(@class,'m-auto')]"
    
    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)
    
    def get_at_risk_count(self):
        self.wait_for_visible(self.at_risk_task_indicator)
        return self.get_text(self.at_risk_task_indicator)
    
    def get_delay_count(self):
        element = self.page.locator(self.delay_task_indicator)
        element.wait_for(state="visible")
        return element.inner_text()
    
    def get_task_finish_perc(self):
        element = self.page.locator(self.finished_impact_navigator)
        element.wait_for(state="visible")
        return element.inner_text()
    
    def get_budget_utilised_perc(self):
        element = self.page.locator(self.budge_utilised_navigator)
        element.wait_for(state="visible")
        return element.inner_text()
    
    
    