from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from conftest import driver

class MainPage(BasePage):

    def click_top_order_button(self):
        self.find_element(locator=MainPageLocators.TOP_ORDER_BUTTON).click()


    @staticmethod
    def click_bottom_order_button(driver):
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        button.click()


    def click_logo(self):
        self.find_element(locator=MainPageLocators.LOGO).click()

    def click_logo_yandex(self):
        self.find_element(locator=MainPageLocators.LOGO_YANDEX).click()

    def click_dropdown_content(self, question_locator, answer_locator, expected_answer_text):

        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        self.click(question_locator)

        actual_answer_text = self.get_text(answer_locator)
        assert actual_answer_text == expected_answer_text, \
            f"Expected '{expected_answer_text}', but got '{actual_answer_text}'"




