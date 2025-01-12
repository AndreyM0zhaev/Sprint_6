from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constant

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constant.URL
        self.wait = WebDriverWait(self.driver, 10)

    def wait_until_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator), message=f'Элемент {locator} не видим')

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Не удалось найти элементы {locator}')

    def get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Элемент {locator} не виден').text

    def click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Элемент {locator} не кликабелен').click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
