"""
API тесты для Кинопоиска.
"""
import sys
import os
import requests
import allure
import pytest
from config import BASE_URL, HEADERS
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


@pytest.mark.api
@allure.feature("API Tests для Кинопоиска")
class TestKinopoiskAPI:
    """API тесты для Кинопоиска."""

    @allure.title("Поиск фильма по латинице: Inception")
    @allure.description("GET /movie с параметром search=Inception")
    def test_search_movie_latin(self):
        """Проверяет поиск фильма по латинскому названию."""
        with allure.step("Запрос поиска фильма Inception"):
            response = requests.get(
                f"{BASE_URL}/movie?search=Inception", headers=HEADERS
            )
        with allure.step("Проверка статуса ответа 200"):
            assert response.status_code == 200

    @allure.title("Поиск фильма по ID: 447301")
    @allure.description("GET /movie/447301")
    def test_search_movie_by_id(self):
        """Проверяет поиск фильма по ID."""
        with allure.step("Запрос фильма по ID"):
            response = requests.get(
                f"{BASE_URL}/movie/447301", headers=HEADERS
            )
        with allure.step("Проверка статуса ответа 200"):
            assert response.status_code == 200

    @allure.title("Поиск фильма по кириллице: Матрица")
    @allure.description("GET /movie с параметром search=Матрица")
    def test_search_movie_cyrillic(self):
        """Проверяет поиск фильма по кириллическому названию."""
        with allure.step("Запрос поиска фильма Матрица"):
            response = requests.get(
                f"{BASE_URL}/movie?search=Матрица", headers=HEADERS
            )
        with allure.step("Проверка статуса ответа 200"):
            assert response.status_code == 200

    @allure.title("Поиск актёра: Киану Ривз")
    @allure.description("GET /person с параметром search=Киану Ривз")
    def test_search_actor(self):
        """Проверяет поиск актера по имени."""
        with allure.step("Запрос поиска актера Киану Ривз"):
            response = requests.get(
                f"{BASE_URL}/person?search=Киану Ривз", headers=HEADERS
            )
        with allure.step("Проверка статуса ответа 200"):
            assert response.status_code == 200

    @allure.title("Поиск фильма без авторизации")
    @allure.description("GET /movie без заголовка авторизации")
    def test_search_movie_without_auth(self):
        """Проверяет, что без авторизации возвращается 401."""
        with allure.step("Запрос без API-ключа"):
            response = requests.get(f"{BASE_URL}/movie?search=Начало")
        with allure.step("Проверка статуса ответа 401"):
            assert response.status_code == 401
