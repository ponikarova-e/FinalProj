import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.main_page import MainPage


@pytest.mark.ui
def test_search_matrix(browser):
    page = MainPage(browser)
    page.enter_search_query("Матрица")

    with allure.step("Проверяем, что на странице есть текст 'Матрица'"):
        assert "Матрица" in browser.page_source


@pytest.mark.ui
def test_navigate_to_interstellar_page(browser):
    page = MainPage(browser)
    page.enter_search_query("Интерстеллар")
    page.click_film_link("Интерстеллар")

    with allure.step("Проверяем, что в заголовке "
                     "страницы есть 'Интерстеллар'"):
        assert "Интерстеллар" in browser.title


@pytest.mark.ui
def test_navigate_to_top_movies(browser):
    page = MainPage(browser)
    page.click_link_by_text("Фильмы")
    page.click_element_by_class("styles_name__7luvu")

    with allure.step("Ожидаем, что URL содержит 'top250' "
                     "и проверяем страницу"):
        WebDriverWait(browser, 10).until(EC.url_contains("top250"))
        assert "top250" in browser.current_url
        assert "Топ 250 фильмов" in browser.page_source


@pytest.mark.ui
def test_quick_search(browser):
    page = MainPage(browser)
    page.click_button_css_selector("button[tabindex='-1']")

    with allure.step("Ожидаем, что заголовок "
                     "страницы стал 'Случайный фильм!'"):
        WebDriverWait(browser, 30).until(EC.title_is("Случайный фильм!"))

    with allure.step("Проверяем URL и заголовок страницы"):
        assert "chance" in browser.current_url
        assert "Случайный фильм!" in browser.title


@pytest.mark.ui
def test_login_page_accessibility(browser):
    page = MainPage(browser)
    page.click_login_button()
    page.wait_for_auth_page()
    page.check_page_title_contains("Авторизация")
