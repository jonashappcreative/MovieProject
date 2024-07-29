import json

import api_testing
from istorage import IStorage


class StorageJson(IStorage):
    """
    Docstring:
    This Class inherit all the empty functions from the interface (IStorage)
    and abstract methods make sure everything gets used

    """

    def __init__(self, file_path):
        self.file_path = file_path

    def _open_movies(self):

        with open(self.file_path, "r") as fileobj:
            movies = json.load(fileobj)
            return movies

    def _list_movies(self):

        movies = self._open_movies()
        print(f"{len(movies)} movies in total")

        for movie, details in movies.items():
            print(f"{movie}: {details['rating']}")

    def _save_movies(self, movies):

        with open(self.file_path, "w") as fileobj:
            json.dump(movies, fileobj, indent=4)

    def _add_movie(self, **kwargs):
        """
            Adds a movie to the movie's database.
            Loads the information from the JSON file, add the movie,
            and saves it. The function doesn't need to validate the input.
            :param **kwargs:
            """
        # Get the data from the JSON file
        movies = self._open_movies()
        search_title = input("Enter New Film Name: ")

        if search_title in movies:
            print("This movie already exists! Did you want to update instead?")
            return

        try:
            title, year, rating, poster_image_url = api_testing.search_film(search_title)

        # Exits this part of the Code when a None is returned by API, Warning was already Printed to user
        except TypeError:
            print("Error! A Type Error Occurred!")
            return

        # Adds the new movie information to the JSON Database
        movies[title] = {"rating": rating, "year": year, "poster image url": poster_image_url}
        self._save_movies(movies)

        print(f"Movie {title} successfully added")

    def _delete_movie(self):
        """
        Deletes a movie from the movie's database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self._open_movies()
        movie_to_delete = input("Enter movie name to delete: ")

        if movie_to_delete in movies:
            del movies[movie_to_delete]
            print(f"Movie {movie_to_delete} successfully deleted")
        else:
            print(f"Movie {movie_to_delete} not in movies")

        self._save_movies(movies)

    def _update_movie(self):
        movie_to_delete = input("Enter movie name to update: ")
        custom_title = input("Enter your new title: ")
        custom_rating = input("Enter your new rating: ")
        movies = self._open_movies()

        movies[custom_title] = movies[movie_to_delete]
        movies[custom_title]["rating"] = custom_rating

        del movies[movie_to_delete]

        self._save_movies(movies)
