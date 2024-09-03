from selenium.webdriver.common.by import By
from EpamPages.base_page import BasePage


class JobListingPage(BasePage):
    def __init__(self, driver):
        super().__init__('careers/job-listings', driver)
        self.result_text_locator = (By.XPATH, "//header[@class='search-result__header']/h1")
        self.view_and_apply_button_locator = (
            By.XPATH, "(//a[contains(@class,'button-text') and contains(@href,'job.')])[1]")
        self.view_and_apply_button_locator_partiallinktext = (By.LINK_TEXT, "View and apply")

    def click_apply(self):
        super().js_scroll_and_js_click(self.view_and_apply_button_locator)

    def click_apply_with_partitallinktext(self):
        apply_buttons_elements = self.driver.find_elements(*self.view_and_apply_button_locator_partiallinktext)
        if not apply_buttons_elements:
            apply_buttons_elements[0].click()
        else:
            f"Button is not found"
