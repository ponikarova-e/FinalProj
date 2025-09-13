import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_search_matrix(browser):
    with allure.step("Находим поле поиска и вводим запрос 'Матрица'"):
        search_box = browser.find_element(By.NAME, 'kp_query')
        search_box.send_keys("Матрица")
        search_box.submit()

    with allure.step("Проверяем, что на странице есть текст 'Матрица'"):
        assert "Матрица" in browser.page_source


@pytest.mark.ui
def test_navigate_to_interstellar_page(browser):
    with allure.step("Вводим в поиск название фильма 'Интерстеллар'"
                     " и отправляем запрос"):
        search_box = browser.find_element(By.NAME, 'kp_query')
        search_box.send_keys("Интерстеллар")
        search_box.submit()

    with allure.step("Кликаем по ссылке с названием 'Интерстеллар'"):
        film_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Интерстеллар")
        film_link.click()

    with allure.step("Проверяем, что в заголовке "
                     "страницы есть 'Интерстеллар'"):
        assert "Интерстеллар" in browser.title


@pytest.mark.ui
def test_navigate_to_top_movies(browser):
    with allure.step("Переходим по ссылке 'Фильмы'"):
        top_movies_link = browser.find_element(By.LINK_TEXT, "Фильмы")
        top_movies_link.click()

    with allure.step("Кликаем по элементу с классом 'styles_name__7luvu'"):
        browser.find_element(By.CLASS_NAME, "styles_name__7luvu").click()

    with allure.step("Ожидаем, что URL содержит 'top250'"
                     " и проверяем страницу"):
        WebDriverWait(browser, 10).until(EC.url_contains("top250"))
        assert "top250" in browser.current_url
        assert "Топ 250 фильмов" in browser.page_source


@pytest.mark.ui
def test_quick_search(browser):
    with allure.step("Кликаем на кнопку с CSS-селектором"
                     " button[tabindex='-1']"):
        element = browser.find_element(By.
                                       CSS_SELECTOR, "button[tabindex='-1']")
        element.click()

    with allure.step("Ожидаем, что заголовок страницы стал "
                     "'Случайный фильм!'"):
        WebDriverWait(browser, 30).until(EC.title_is("Случайный фильм!"))

    with allure.step("Проверяем URL и заголовок страницы"):
        assert "chance" in browser.current_url
        assert "Случайный фильм!" in browser.title


@pytest.mark.ui
def test_login_page_accessibility(browser):
    with allure.step("Нажать на кнопку входа"):
        login_button = browser.find_element(By.CLASS_NAME,
                                            "styles_loginButton__6_QNl")
        login_button.click()

    with allure.step("Ожидание перехода на страницу авторизации"):
        WebDriverWait(browser, 10).until(EC.url_contains("auth"))

    with allure.step("Проверить, что в заголовке страницы "
                     "присутствует 'Авторизация'"):
        assert "Авторизация" in browser.title
