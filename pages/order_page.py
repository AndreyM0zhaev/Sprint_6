from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_order_form(self, order_data):
        data = order_data
        self.find_element(locator=MainPageLocators.TOP_ORDER_BUTTON).click()
        self.find_element(locator=OrderPageLocators.FIRST_NAME_INPUT).send_keys(data['first_name'])
        self.find_element(locator=OrderPageLocators.LAST_NAME_INPUT).send_keys(data['last_name'])
        self.find_element(locator=OrderPageLocators.ADDRESS_INPUT).send_keys(data['address'])
        metro_input = self.find_element(locator=OrderPageLocators.METRO_STATION_INPUT)
        metro_input.send_keys(data['metro'])
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        self.find_element(locator=OrderPageLocators.PHONE_INPUT).send_keys(data['phone'])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)).click()
