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


