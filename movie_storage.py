import importlib
import json
import api_testing
from storage_json import StorageJson


def open_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """

    print("OPENED WRONG FILEPATH HERE")
    FILE_PATH = "movie_storage_database.json"

    with open(FILE_PATH, "r") as fileobj:
        data = json.load(fileobj)
        return data


def save_movies(movies):
    with open("movie_storage_database.json", "w") as fileobj:
        json.dump(movies, fileobj, indent=4)
    importlib.reload(json)


def add_movie_to_database(new_movie, rating, year):
    """
    Adds a movie to the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = open_movies()
    movies[new_movie] = {"rating": rating, "year": year}
    save_movies(movies)


def add_movie_by_api(search_title):

    movies = open_movies()

    try:
        title, year, rating, poster_image_url = api_testing.search_film(search_title)

    # Exits this part of the Code when a None is returned by API, Warning was already Printed to user
    except TypeError:
        return

    movies[title] = {"rating": rating, "year": year, "poster image url": poster_image_url}
    print(f"Movie {title} successfully added")
    save_movies(movies)


def delete_movie_from_database(movie_to_delete):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.

    -> Going to be transfered to Storage JSON Functions!
    """
    movies = open_movies()
    del movies[movie_to_delete]
    save_movies(movies)


def update_movie(movie_to_update):
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = open_movies()

    if movie_to_update in movies.keys():
        rating_new = float(input("Enter new movie rating (0-10): "))
        year_new = int(input("Enter the movie's year: "))
        movies.update({movie_to_update: {
            "rating": rating_new,
            "year": year_new
        }
        })
        print(f"Movie {movie_to_update} successfully updated")
    else:
        print(f"Movie {movie_to_update} not in movies")

    save_movies(movies)
