from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from EpamPages.base_page import BasePage
from constants import TIMEOUT


class CareerSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__('careers', driver)
        self.keyword_box_locator = (By.ID, 'new_form_job_search-keyword')
        self.find_button_locator = (By.XPATH, "//fieldset[@class='recruiting-search__filter']/following-sibling::button")
        self.location_dropdown_locator = (By.CSS_SELECTOR, '.select2-container :first-child .select2-selection')
        self.remote_checkbox_locator = (By.XPATH, "//input[contains(@class,'recruiting-search__checkbox')]")

    def fill_keyword_box_click(self, keyword):
        super().js_scroll_and_js_click(self.keyword_box_locator).send_keys(keyword)

    def select_location(self, location):
        wait = WebDriverWait(self.driver, TIMEOUT)
        dropdown = wait.until(EC.presence_of_element_located(self.location_dropdown_locator))
        dropdown.click()

        options = self.driver.find_elements(By.CSS_SELECTOR, '.select2-results__option')
        desired_option = None
        for option in options:
            txt = option.text.strip()
            if txt == location:
                desired_option = option
                break

        if desired_option:
            desired_option.click()
        else:
            print(f"Desired option {location} not found")

    def check_remote_checkbox(self):
        super().js_click(self.remote_checkbox_locator)

    def click_find_button(self):
        super().click(self.find_button_locator)


