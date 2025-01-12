import pytest

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
        main_page.click_bottom_order_button()


    def test_click_logo(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_site()
        assert main_page.get_current_url() == Constant.URL, "Не удалось перейти на главную страницу"

        main_page.click_top_order_button()
        assert main_page.get_current_url() == Constant.ORDER_URL, "Не удалось перейти на страницу заказа"

        main_page.click_logo()
        assert main_page.get_current_url() == Constant.URL, "Не удалось вернуться на главную страницу после нажатия на логотип"

    def test_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        assert main_page.get_current_url() == Constant.URL

        main_page.click_logo_yandex()
        main_page.wait_for_new_tab_and_switch()
        main_page.wait_for_url_contains("https://dzen.ru/?yredirect=true")

        assert main_page.get_current_url() == Constant.DZEN_URL
