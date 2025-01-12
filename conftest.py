import pytest
from selenium import webdriver

from constants import Constant

@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы веб-драйвера.
    Возвращает экземпляр драйвера для использования в тестах.
    """
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(Constant.URL)
    yield browser
    browser.quit()
