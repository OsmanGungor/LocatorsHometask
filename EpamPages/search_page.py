from selenium.webdriver.common.by import By
from EpamPages.base_page import BasePage


class Searchpage(BasePage):
    def __init__(self, driver):
        super().__init__('search', driver)
        self.result_link_locator = (By.XPATH, "//a[@class ='search-results__title-link']")

    def get_result_text(self):
        elements = self.driver.find_elements(*self.result_link_locator)
        text_list = []
        for element in elements:
            text_of_the_element = element.text
            text_list.append(text_of_the_element)
        return text_list
