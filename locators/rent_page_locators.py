from selenium.webdriver.common.by import By

class RentPageLocators:

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    MODAL = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
    ORDER_COMPLETE = (By.XPATH,  "//div[@class='Order_ModalHeader__3FDaJ']")
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Посмотреть статус']")
    DROPDOWN_MENU = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]")
    ORDER_CANCEL = (By.XPATH, "//button[contains(text(),'Отменить заказ')]")

    @staticmethod
    def RENTAL_PERIOD_OPTION(period_text):
        return (By.XPATH, f"//div[@role='option'][contains(text(), '{period_text}')]")

    @staticmethod
    def COLOR_CHECKBOX(color_id):
        return (By.ID, color_id)

