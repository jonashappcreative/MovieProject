from istorage import IStorage
import csv
# import api_testing


class StorageCsv(IStorage):

    def __init__(self, file_path):
        self.file_path = file_path

    def _open_movies(self):

        movies = {}

        with open(self.file_path, "r") as fileobj:
            lines = fileobj.readlines()

            for line in lines:
                splitted_line = line.split(",")

                movies[splitted_line[0]] = {
                    "rating": splitted_line[1],
                    "year": splitted_line[2],
                    "posterImageUrl": splitted_line[3]
                }

        return movies

    def _list_movies(self):

        movies = self._open_movies()
        print(f"{len(movies)} movies in total")

        for movie, details in movies.items():
            print(f"{movie}: {details['rating']}")

    def _save_movies(self):

        with open(self.file_path, "w") as fileobj:


    def _add_movie(self):
        """
        Add a film to the movies list.
        Does not need any arguments as we are puling the movie data from the API anyway
        :return: None
        """
        pass

    def _delete_movie(self):
        """
        Deletes a film from the list. Does not need a title since we ask in the function.
        A check if there are even films to delete firsthand would be great.
        :return: None
        """
        pass

    def _update_movie(self):
        pass
