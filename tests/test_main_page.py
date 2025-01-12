import pytest
import allure

from pages import main_page
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from constants import Constant

@allure.feature("Тесты главной страницы")
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
    @allure.story("Оформление заказа через верхнюю кнопку")
    @allure.title("Проверка полного процесса оформления заказа")
    @allure.description("""
        Тест проверяет полный процесс оформления заказа через верхнюю кнопку "Заказать".
        Шаги:
        1. Переход на сайт.
        2. Клик на верхнюю кнопку "Заказать".
        3. Заполнение формы заказа.
        4. Заполнение формы аренды.
        5. Подтверждение заказа.
        6. Проверка успешного оформления заказа.
    """)
    @pytest.mark.parametrize("order_data", ORDERS_DATA)
    def test_order_flow_with_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)

        with allure.step("Переход на сайт"):
            main_page.go_to_site()

        with allure.step("Клик на верхнюю кнопку 'Заказать'"):
            main_page.click_top_order_button()

        with allure.step("Заполнение формы заказа"):
            order_page.fill_order_form(order_data)

        with allure.step("Заполнение формы аренды"):
            rent_page.fill_rent_form(order_data)

        with allure.step("Подтверждение заказа"):
            rent_page.order_modal_displayed()

        with allure.step("Проверка успешного оформления заказа"):
            assert rent_page.order_successfully_placed(), "Заказ не был успешно оформлен"

    @allure.story("Оформление заказа через нижнюю кнопку")
    @allure.title("Проверка перехода к форме заказа через нижнюю кнопку")
    @allure.description("""
        Тест проверяет переход к форме заказа через нижнюю кнопку "Заказать".
        Шаги:
        1. Переход на сайт.
        2. Клик на нижнюю кнопку "Заказать".
    """)

    def test_flow_order_bottom_button(self, driver):
        main_page = MainPage(driver)

        with allure.step("Переход на сайт"):
            main_page.go_to_site()

        with allure.step("Клик на нижнюю кнопку 'Заказать'"):
            main_page.click_bottom_order_button()

        with allure.step("Проверка, что форма заказа отображается"):
            assert main_page.is_order_form_displayed(), "Форма заказа не отображается после клика на нижнюю кнопку"

    @allure.story("Проверка логотипа")
    @allure.title("Проверка перехода на главную страницу через логотип")
    @allure.description("""
        Тест проверяет, что логотип возвращает на главную страницу.
        Шаги:
        1. Переход на сайт.
        2. Клик на верхнюю кнопку "Заказать".
        3. Клик на логотип.
        4. Проверка, что пользователь вернулся на главную страницу.
    """)
    def test_click_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Переход на сайт"):
            main_page.go_to_site()
            assert main_page.get_current_url() == Constant.URL, "Не удалось перейти на главную страницу"

        with allure.step("Клик на верхнюю кнопку 'Заказать'"):
            main_page.click_top_order_button()
            assert main_page.get_current_url() == Constant.ORDER_URL, "Не удалось перейти на страницу заказа"

        with allure.step("Клик на логотип"):
            main_page.click_logo()
            assert main_page.get_current_url() == Constant.URL, "Не удалось вернуться на главную страницу после нажатия на логотип"

    @allure.story("Проверка редиректа на Dzen")
    @allure.title("Проверка перехода на Dzen через логотип Яндекса")
    @allure.description("""
        Тест проверяет, что клик на логотип Яндекса открывает новую вкладку с Dzen.
        Шаги:
        1. Переход на сайт.
        2. Клик на логотип Яндекса.
        3. Переключение на новую вкладку.
        4. Проверка URL новой вкладки.
    """)
    def test_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Переход на сайт"):
            main_page.go_to_site()
            assert main_page.get_current_url() == Constant.URL

        with allure.step("Клик на логотип Яндекса"):
            main_page.click_logo_yandex()

        with allure.step("Переключение на новую вкладку"):
            main_page.wait_for_new_tab_and_switch()

        with allure.step("Проверка URL новой вкладки"):
            main_page.wait_for_url_contains("https://dzen.ru/?yredirect=true")
            assert main_page.get_current_url() == Constant.DZEN_URL