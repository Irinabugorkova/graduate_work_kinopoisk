"""
Page Object для главной страницы Кинопоиска.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Page Object для главной страницы Кинопоиска."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем главную страницу Кинопоиска")
    def open(self):
        """Открывает главную страницу."""
        self.driver.get("https://www.kinopoisk.ru")
        self.accept_cookies()

    @allure.step("Принимаем cookies, если нужно")
    def accept_cookies(self):
        """Принимает cookies."""
        try:
            allow_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "gdpr-popup-v3-button-all"))
            )
            allow_button.click()
        except Exception:
            pass

    @allure.step("Проверяем, что поле поиска активно")
    def is_search_field_active(self):
        """Проверяет активность поля поиска."""
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "kp_query"))
        )
        return search_input.is_enabled()

    @allure.step("Вводим запрос в строку поиска: {query}")
    def search_query(self, query):
        """Выполняет поиск по запросу."""
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "kp_query"))
        )
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Кликаем на первый результат поиска фильма")
    def click_first_movie_result(self):
        """Кликает на первый результат поиска."""
        first_result = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "div.search_results div.most_wanted a.js-serp-metrika")
            )
        )
        first_result.click()

    @allure.step("Кликаем на кнопку Войти")
    def click_login_button(self):
        """Кликает на кнопку входа."""
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "styles_loginButton__6_QNl")
            )
        )
        login_button.click()

    @allure.step("Проверяем, что открыта страница входа")
    def is_login_page_opened(self):
        """Проверяет открытие страницы входа."""
        return ("login" in self.driver.current_url or
                "Войти" in self.driver.page_source)

    @allure.step("Кликаем на результат поиска актёра: {actor_name}")
    def click_actor_result(self, actor_name):
        """Кликает на результат поиска актера."""
        actor_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, actor_name)
            )
        )
        actor_link.click()

    @allure.step("Проверяем, что открыта страница актёра: {actor_name}")
    def is_actor_page_opened(self, actor_name):
        """Проверяет открытие страницы актера."""
        return ("name" in self.driver.current_url and
                actor_name in self.driver.page_source)

    @allure.step("Кликаем на кнопку Расширенный поиск")
    def click_advanced_search(self):
        """Кликает на кнопку расширенного поиска."""
        advanced_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "a.styles_advancedSearch__gn_09["
                 "aria-label='Расширенный поиск']")
            )
        )
        advanced_button.click()

    @allure.step("Проверяем, что открыт расширенный поиск")
    def is_advanced_search_opened(self):
        """Проверяет открытие расширенного поиска."""
        return "/s/" in self.driver.current_url
