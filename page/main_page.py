from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    @allure.step("Ввести в поиск текст: '{query}'")
    def enter_search_query(self, query: str):
        search_box = self.browser.find_element(By.NAME, 'kp_query')
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    @allure.step("Нажать на ссылку фильма с названием,"
                 " содержащим '{partial_text}'")
    def click_film_link(self, partial_text: str):
        film_link = self.browser.find_element(By.PARTIAL_LINK_TEXT,
                                              partial_text)
        film_link.click()

    @allure.step("Перейти по ссылке с текстом '{link_text}'")
    def click_link_by_text(self, link_text: str):
        link = self.browser.find_element(By.LINK_TEXT, link_text)
        link.click()

    @allure.step("Кликнуть на элемент с классом '{class_name}'")
    def click_element_by_class(self, class_name: str):
        element = self.browser.find_element(By.CLASS_NAME, class_name)
        element.click()

    @allure.step("Кликнуть на кнопку с CSS-селектором '{css_selector}'")
    def click_button_css_selector(self, css_selector: str):
        button = self.browser.find_element(By.CSS_SELECTOR, css_selector)
        button.click()

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        login_button = self.browser.find_element(By.CLASS_NAME,
                                                 "styles_loginButton__6_QNl")
        login_button.click()

    @allure.step("Ожидание перехода на страницу авторизации")
    def wait_for_auth_page(self):
        self.wait.until(EC.url_contains("auth"))

    @allure.step("Проверка заголовка страницы содержит '{text}'")
    def check_page_title_contains(self, text: str):
        assert text in self.browser.title, \
            (f"Ожидалось, что в title будет '{text}',"
             f" но получили '{self.browser.title}'")
