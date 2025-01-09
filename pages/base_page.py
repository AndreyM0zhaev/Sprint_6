from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constant

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constant.URL

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find element {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).text

    def click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()