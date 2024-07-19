from istorage import IStorage
import json
import importlib
###
import movie_storage
from main_phase2 import add_movie_api


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

    def _save_movies(self):

        with open(self.file_path, "w") as fileobj:
            json.dump(movies, fileobj, indent=4)
        importlib.reload(json)

    def _list_movies(self):

        movies = self._open_movies()
        print(f"{len(movies)} movies in total")

        for movie, details in movies.items():
            print(f"{movie}: {details['rating']}")

    def _add_movie(self, title, year, rating, poster):
        """
            Adds a movie to the movies database.
            Loads the information from the JSON file, add the movie,
            and saves it. The function doesn't need to validate the input.
            """
        # Get the data from the JSON file
        movies = self._open_movies()
        new_movie = input("Enter New Film Name: ")

        if title in movies:
            print("This movie already exists! Did you want to update instead?")
            return
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self.add_movie_by_api(new_movie)
        self._save_movies(movies)
        print(f"Movie {title} successfully added")


    def _delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = _open_movies()
        del movies[movie_to_delete]
        _save_movies(movies)

    def _update_movie(self, title, rating):
        pass
