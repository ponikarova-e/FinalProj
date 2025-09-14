import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(40)
    browser.maximize_window()
    browser.get("https://www.kinopoisk.ru/")
    yield browser

    browser.quit()
