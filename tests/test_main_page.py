import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from constants import Constant


class TestMainPage:
    ORDERS_DATA = [
        {
            "first_name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, ул. Ленина, д. 1",
            "metro": "Белорусская",
            "phone": "+79991234567",
            "date": "2022-01-01",
            "rental_period": "сутки",
            "color": "чёрный жемчуг",
            "comment": "комментарий_1",
        },
        {
            "first_name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский пр., д. 25",
            "metro": "Красногвардейская",
            "phone": "+79876543210",
            "date": "2022-02-01",
            "rental_period": "семеро суток",
            "color": "серая безысходность",
            "comment": "комментарий_2",
        }
    ]

    @pytest.mark.parametrize("order_data", ORDERS_DATA)
    def test_order_flow_with_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)

        main_page.go_to_site()
        main_page.click_top_order_button()
        order_page.fill_order_form(order_data)
        rent_page.fill_rent_form(order_data)
        rent_page.order_modal_displayed()
        rent_page.order_successfully_placed()


    def test_flow_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_bottom_order_button(driver)


    def test_click_logo(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_site()
        assert driver.current_url == Constant.URL, "Не удалось перейти на главную страницу"

        main_page.click_top_order_button()
        assert driver.current_url == Constant.ORDER_URL, "Не удалось перейти на страницу заказа"

        main_page.click_logo()
        assert driver.current_url == Constant.URL, "Не удалось вернуться на главную страницу после нажатия на логотип"

    def test_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        assert driver.current_url == Constant.URL
        main_page.click_logo_yandex()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1, "Новая вкладка не открылась в течение тайм-аута")
        new_tab = driver.window_handles[1]
        driver.switch_to.window(new_tab)

        WebDriverWait(driver, 15).until(
            lambda d: "https://dzen.ru/?yredirect=true" in d.current_url)

        assert driver.current_url == Constant.DZEN_URL





