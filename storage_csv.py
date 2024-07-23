from istorage import IStorage
import csv
import api_testing


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

    def _save_movies(self, lines):

        with open(self.file_path, "w") as fileobj:
            fileobj.writelines(lines)
            fileobj.close()

        '''
        JSON EQUIVALENT:
        with open(self.file_path, "w") as fileobj:
        json.dump(movies, fileobj, indent=4)
        '''

    def _add_movie(self):
        """
        Add a film to the movies list.
        Does not need any arguments as we are puling the movie data from the API anyway
        :return: None
        """
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

        with open(self.file_path, "r") as fileobj:
            lines = fileobj.readlines()

        # Adds the new movie information to the CSV Database as New Line
        new_line = title + "," + year + "," + rating + "," + poster_image_url + "\n"
        lines.append(new_line)

        self._save_movies(lines)
        print(f"Movie {title} successfully added")

        return




    def _delete_movie(self):
        """
        Deletes a film from the list. Does not need a title since we ask in the function.
        A check if there are even films to delete firsthand would be great.
        :return: None
        """
        pass

    def _update_movie(self):
        pass
