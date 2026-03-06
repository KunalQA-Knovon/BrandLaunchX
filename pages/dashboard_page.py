from pages.base_page import BasePage
import re

class DashboardPage(BasePage):
    def __init__(self, page, logger_name=None):
        super().__init__(page, logger_name)

    total_Task_Count_Locator = "//span[normalize-space()='Total Task(s)']/following-sibling::h1"
    completed_Task_Count_Locator = "//span[normalize-space()='Completed Task(s)']/following-sibling::h1"
    ongoing_Task_Count_Locator = "//span[normalize-space()='Ongoing Task(s)']/following-sibling::h1"
    atRisk_Task_Count_Locator = "//span[normalize-space()='At Risk Task(s)']/following-sibling::h1"
    table_locator = "//table[contains(@class,'table1')]//tbody/tr"
    country_wise_lunch_staus_locator="//div[contains(@class,'full_box_status')]"
    country_name_locator = "xpath=.//div[contains(@class,'cntry_name')]"
    at_risk_count_locator = "xpath=.//h6[normalize-space()='Task(s) at Risk']/following-sibling::h3"
    delayed_count_locator = "xpath=.//h6[normalize-space()='Task(s) Delayed']/following-sibling::h3"
    cost_impact_locator = "//h2[contains(normalize-space(),'Cost Impact')]"
    delay_locator = "//h2[contains(normalize-space(),'Delay')]"
    launch_date = "//span[@class='launch_date']/h3"


    def total_task_count(self):
      self.page.wait_for_load_state(state="")
      return self.get_text(self.total_Task_Count_Locator)
    
    def get_Launch_date(self):
      self.page.wait_for_load_state(state="domcontentloaded")
      return self.page.locator(self.launch_date)
    

    def completed_task_count(self):
      return self.get_text(self.completed_Task_Count_Locator)
    
    def ongoing_task_count(self):
      return self.get_text(self.ongoing_Task_Count_Locator)
    

    def atRisk_task_count(self):
      return self.get_text(self.atRisk_Task_Count_Locator)
    
    def get_cost_impect(self):
      cost_impect_text = self.page.locator(self.cost_impact_locator).inner_text()
      match = re.search(r'\d+', cost_impect_text)
      if match:
         return match.group()
      else:
         None
    
    def get_delay_impect(self):
      delay_text = self.page.locator(self.delay_locator).inner_text()
      match = re.search(r'\d+', delay_text)
      if match:
         return match.group()
      else:
         None


    def get_table_data(self):
        rows = self.page.locator(self.table_locator)
        table_data = {}

        for i in range(rows.count()):
            row = rows.nth(i)
            function_name = row.locator("td").nth(0).inner_text().strip()
            total_task = row.locator("td").nth(1).inner_text().strip()
            completed_task_percentage = row.locator("td").nth(2).locator("span").inner_text().strip().replace('%',"")
            table_data[function_name]={"total_task":total_task, "percentage":completed_task_percentage}
            
        return table_data
    
    def get_country_wise_data(self):
        blocks = self.page.locator(self.country_wise_lunch_staus_locator)
        blocks.first.wait_for(state="visible", timeout=30000)

        country_data = {}

        for i in range(blocks.count()):
            block = blocks.nth(i)
            country_name = block.locator(self.country_name_locator).text_content().strip()
            
            at_risk_count = int(block.locator(self.at_risk_count_locator)
                    .nth(0).text_content().strip()
            )

            delayed_count = int(block.locator(self.delayed_count_locator)
                    .nth(0).text_content().strip()
            )

            at_risk_pct = float(block.locator(self.at_risk_count_locator)
                    .nth(1).text_content().replace("%", "").strip()
            )

            delayed_pct = float(block.locator(self.delayed_count_locator)
                    .nth(1).text_content().replace("%", "").strip()
            )

            country_data[country_name] = {
                "at_risk_count": at_risk_count,
                "delayed_count": delayed_count,
                "at_risk_pct": at_risk_pct,
                "delayed_pct": delayed_pct
            }
        return country_data
    
