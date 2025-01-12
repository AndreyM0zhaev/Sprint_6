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

    def click_faq_question(self, question_number: int):
        locator = MainPageLocators.faq_question_button(question_number)
        self.find_element(locator).click()

    def get_faq_answer_text(self, answer_number: int) -> str:
        locator = MainPageLocators.faq_answer(answer_number)
        return self.find_element(locator).text

    def click_cookie_accept(self):
        return self.find_element(MainPageLocators.COOKIE_ACCEPT_BUTTON).click()
