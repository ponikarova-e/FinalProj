import pytest
from api.FilmApi import FilmApi


@pytest.mark.api
def test_get_movie_by_id():
    movie_id = 2213
    response = FilmApi.get_movie_by_id (movie_id)
    assert response.status_code == 200
    data = response.json()
    assert data.get("kinopoiskId") == movie_id
    assert "nameOriginal" in data


@pytest.mark.api
def test_search_movies():
    keyword = "мстители"
    response = FilmApi.search_movies(keyword)
    assert response.status_code == 200
    data = response.json()
    assert "films" in data and len(data["films"]) > 0


@pytest.mark.api
def test_get_person_by_id():
    person_id = 32169
    response = FilmApi.get_person_by_id(person_id)
    assert response.status_code == 200
    data = response.json()
    assert data.get("personId") == person_id
    assert "nameRu" in data


@pytest.mark.api
def test_get_top_250_movies():
    response = FilmApi.get_top_250_movies()
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert data["total"] > 0


@pytest.mark.api
def test_get_films_premieres():
    response = FilmApi.get_films_premieres(2025, "OCTOBER")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data['items']) > 0
