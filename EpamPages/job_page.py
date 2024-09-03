from selenium.webdriver.common.by import By
from EpamPages.base_page import BasePage


class JobPage(BasePage):
    def __init__(self, driver):
        super().__init__('careers/job-listings/job', driver)
        self.job_title_locator = (By.CLASS_NAME, "vacancy-details-23__job-title")

    def get_title_text(self):
        title = self.driver.find_element(*self.job_title_locator)
        title_text = title.text
        return title_text
