from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_order_form(self, order_data):
        data = order_data

        self.click(MainPageLocators.TOP_ORDER_BUTTON)

        self.find_element(OrderPageLocators.FIRST_NAME_INPUT).send_keys(data['first_name'])
        self.find_element(OrderPageLocators.LAST_NAME_INPUT).send_keys(data['last_name'])
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(data['address'])

        metro_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_input.send_keys(data['metro'])
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(data['phone'])

        self.click(OrderPageLocators.NEXT_BUTTON)
