from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class MainPage(BasePage):

    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_logo(self):
        self.click(MainPageLocators.LOGO)

    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    def click_faq_question(self, question_number: int):
        locator = MainPageLocators.faq_question_button(question_number)
        self.click(locator)

    def get_faq_answer_text(self, answer_number: int) -> str:
        locator = MainPageLocators.faq_answer(answer_number)
        return self.get_text(locator)

    def click_cookie_accept(self):
        self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_new_tab_and_switch(self):
        self.wait.until(lambda d: len(d.window_handles) > 1, "Новая вкладка не открылась в течение тайм-аута")
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)

    def wait_for_url_contains(self, url_part):
        self.wait.until(lambda d: url_part in d.current_url, f"URL не содержит {url_part} в течение тайм-аута")

    def is_order_form_displayed(self):
        try:
            return self.find_element(OrderPageLocators.ORDER_FORM).is_displayed()
        except:
            return False
