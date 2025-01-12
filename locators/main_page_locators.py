from selenium.webdriver.common.by import By

class MainPageLocators:

    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]

    @staticmethod
    def faq_question_button(question_number):
        return (By.ID, f"accordion__heading-{question_number}")

    @staticmethod
    def faq_answer(answer_number):
        return (By.ID, f"accordion__panel-{answer_number}")