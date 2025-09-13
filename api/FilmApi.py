import allure
import requests

from config import API_URL, API_KEY

headers = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json"
}


class FilmApi:
    @staticmethod
    def get_movie_by_id(movie_id):
        url = f"{API_URL}/api/v2.2/films/{movie_id}"
        with allure.step(f"Получение информации о фильме с ID {movie_id}"):
            response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def search_movies(keyword, page=1):
        url = f"{API_URL}/api/v2.1/films/search-by-keyword"
        params = {'keyword': keyword, 'page': page}
        with allure.step(f"Поиск фильмов по ключевому слову '{keyword}',"
                         f" страница {page}"):
            response = requests.get(url, params=params, headers=headers)
        return response

    @staticmethod
    def get_person_by_id(person_id):
        url = f"{API_URL}/api/v1/staff/{person_id}"
        with allure.step(f"Получение информации о человеке с ID {person_id}"):
            response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def get_top_250_movies():
        url = f"{API_URL}/api/v2.2/films/collections"
        params = {"type": "TOP_250_MOVIES"}
        with allure.step("Получение топ-250 фильмов"):
            response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def get_films_premieres(year, month):
        url = f"{API_URL}/api/v2.2/films/premieres"
        params = {'year': year, 'month': month}
        with allure.step(f"Получение премьер кино за {month}/{year}"):
            response = requests.get(url, headers=headers, params=params)
        return response
