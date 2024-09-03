from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from EpamPages.base_page import BasePage
from constants import TIMEOUT


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__('', driver)
        self.services_locator = (By.LINK_TEXT, 'Services')
        self.carriers_locator = (By.PARTIAL_LINK_TEXT, "Careers")
        # getting element by TAG_NAME to fullfill hometask
        self.magnifier_locator = (By.TAG_NAME, "span")
        self.searchtextbox_locator = (By.NAME, "q")
        self.findbutton_locator = (By.CLASS_NAME, 'bth-text-layer')

    def open_page(self):
        super().open_page()
        assert WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(self.services_locator))

    def click_carriers(self):
        super().click(self.carriers_locator)

    def click_magnifier(self):
        elements = self.driver.find_elements(*self.magnifier_locator)
        # i catched lots of span element, with for loop i catch the one with the desired attribute
        for element in elements:
            if element.get_attribute("class") == 'search-icon dark-iconheader-search__search-icon':
                element.click()
                break

    def populate_search_field(self, text_to_search):
        super().js_scroll_and_js_click(self.searchtextbox_locator).send_keys(text_to_search)
        super().click(self.findbutton_locator)
