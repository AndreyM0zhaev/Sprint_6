from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from locators.rent_page_locators import RentPageLocators


class RentPage(BasePage):

    def fill_rent_form(self, order_data):

        data = order_data

        date_input = self.find_element(locator=RentPageLocators.DATE_FIELD)
        date_input.click()
        date_input.clear()
        date_input.send_keys(data['date'])
        date_input.send_keys(Keys.ENTER)

        self.click(RentPageLocators.RENTAL_PERIOD_DROPDOWN)
        dropdown_menu = self.wait_until_visible(RentPageLocators.DROPDOWN_MENU)

        period_option_locator = RentPageLocators.RENTAL_PERIOD_OPTION(data['rental_period'])
        period_option = dropdown_menu.find_element(*period_option_locator)
        period_option.click()

        color_id = "black" if data['color'] == "чёрный жемчуг" else "grey"
        self.click(RentPageLocators.COLOR_CHECKBOX(color_id))

        self.find_element(locator=RentPageLocators.COMMENT_FIELD).send_keys(data['comment'])

        self.click(RentPageLocators.ORDER_BUTTON)


    def order_modal_displayed(self):

        self.wait_until_visible(RentPageLocators.MODAL)
        self.click(RentPageLocators.CONFIRM_YES_BUTTON)

    def order_successfully_placed(self):

        self.wait_until_visible(RentPageLocators.ORDER_COMPLETE)
        self.click(RentPageLocators.SHOW_STATUS_BUTTON)
