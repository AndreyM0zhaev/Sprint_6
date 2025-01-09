from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        self.find_element(locator=RentPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        wait = WebDriverWait(self.driver, 10)
        dropdown_menu = wait.until(
            EC.visibility_of_element_located(RentPageLocators.DROPDOWN_MENU)
        )
        period_option = dropdown_menu.find_element(By.XPATH, f"//div[@role='option'][contains(text(), '{data['rental_period']}')]")
        period_option.click()

        color_id = "black" if data['color'] == "чёрный жемчуг" else "grey"
        self.driver.find_element(By.ID, color_id).click()

        self.find_element(locator=RentPageLocators.COMMENT_FIELD).send_keys(data['comment'])
        self.find_element(locator=RentPageLocators.ORDER_BUTTON).click()


    def order_modal_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RentPageLocators.MODAL))
        self.find_element(locator=RentPageLocators.CONFIRM_YES_BUTTON).click()


    def order_successfully_placed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RentPageLocators.ORDER_COMPLETE))
        self.find_element(locator=RentPageLocators.SHOW_STATUS_BUTTON).click()

