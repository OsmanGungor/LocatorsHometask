import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from constants import TIMEOUT


class BasePage:
    def __init__(self, url, driver):
        self.driver = driver
        self.baseurl = 'https://www.epam.com/'
        self.url = self.baseurl + url

    def open_page(self):
        self.driver.get(self.url)
        self.wait_page_url()
        self.wait_page_ready()

    def wait_page_url(self):
        wait = WebDriverWait(self.driver, TIMEOUT)
        wait.until(lambda driver: self.url in driver.current_url,
                   f"Page url is expected to be {self.url}")

    def wait_page_ready(self):
        wait = WebDriverWait(self.driver, TIMEOUT)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete",
                   f"Page is not in readyState 'complete'")
        time.sleep(1)

    def wait_element_displayed(self, locator):
        wait = WebDriverWait(self.driver, TIMEOUT)
        wait.until(EC.visibility_of_element_located(locator), f"Element is not displayed: {locator}")

    def js_scroll(self, locator, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
                return element
            except (StaleElementReferenceException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to scroll on the element '{locator}' after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def js_scroll_and_js_click(self, locator, retries=3, delay=2):
        self.wait_element_displayed(locator)
        for attempt in range(retries):
            try:
                element = self.js_scroll(locator)
                self.driver.execute_script("arguments[0].click();", element)
                return element
            except (StaleElementReferenceException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to click on the element '{locator}' after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def click(self, locator, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element = self.driver.find_element(*locator)
                element.click()
                return
            except (StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to click on the element after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def js_click(self, locator, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].click();", element)
                return
            except (StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to click on the element after {retries} attempts: {str(e)}")
                time.sleep(delay)
