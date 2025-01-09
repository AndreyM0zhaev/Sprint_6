import pytest
from selenium import webdriver


from constants import Constant


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(Constant.URL)
    yield browser
    browser.quit()


@pytest.fixture(params=[
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
])
def order_data(request):
    return request.param

