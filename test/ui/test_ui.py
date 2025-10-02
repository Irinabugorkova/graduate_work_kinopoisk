"""
UI тесты для Кинопоиска.
Упрощенная версия с методами против капчи
"""

import pytest
import allure
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


@pytest.mark.ui
@allure.feature("UI Tests")
class TestMainPage:
    """Тесты пользовательского интерфейса для Кинопоиска."""

    def human_delay(self):
        """Случайная человеческая задержка"""
        time.sleep(random.uniform(2.0, 4.0))

    def human_type(self, element, text):
        """Человеческий ввод текста"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))

    @allure.story("Поиск")
    @allure.title("Поле поиска активно")
    def test_search_field_is_active(self, browser):
        """Проверяет активность поля поиска."""
        page = MainPage(browser)
        page.open()
        self.human_delay()
        assert page.is_search_field_active()

    @allure.story("Поиск")
    @allure.title("Поиск фильма Эверест")
    def test_search_movie_ui(self, browser):
        """Проверяет поиск фильма."""
        page = MainPage(browser)
        page.open()
        self.human_delay()

        # Человеческий поиск вместо быстрого
        search_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "kp_query"))
        )
        search_input.clear()
        self.human_type(search_input, "Эверест")
        search_input.send_keys(Keys.ENTER)

        self.human_delay()
        page.click_first_movie_result()

        WebDriverWait(browser, 10).until(
            lambda d: "film" in d.current_url
        )
        assert "film" in browser.current_url

    @allure.story("Навигация")
    @allure.title("Проверка расширенного поиска")
    def test_advanced_search_button(self, browser):
        """Проверяет работу расширенного поиска."""
        page = MainPage(browser)
        page.open()
        self.human_delay()
        page.click_advanced_search()
        assert page.is_advanced_search_opened()

    @allure.story("Авторизация")
    @allure.title("Кнопка входа работает")
    def test_login_button_functionality(self, browser):
        """Проверяет работу кнопки входа."""
        page = MainPage(browser)
        page.open()
        self.human_delay()
        page.click_login_button()
        self.human_delay()
        assert page.is_login_page_opened()

    @allure.story("Поиск")
    @allure.title("Поиск актёра Джош Бролин")
    def test_search_actor_by_name(self, browser):
        """Проверяет поиск актера."""
        page = MainPage(browser)
        page.open()
        self.human_delay()

        # Человеческий поиск
        search_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "kp_query"))
        )
        search_input.clear()
        self.human_type(search_input, "Джош Бролин")
        search_input.send_keys(Keys.ENTER)

        self.human_delay()
        page.click_actor_result("Джош Бролин")

        WebDriverWait(browser, 10).until(
            lambda d: "name" in d.current_url
        )
        assert page.is_actor_page_opened("Джош Бролин")
