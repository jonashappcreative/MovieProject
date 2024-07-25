import api_testing
from istorage import IStorage


# I kind of didn't use the CSV import but handled everything as If it would be a blank text file


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
        """
        Gets a list of lines that should be saved to the file at the filepath.

        :param lines: A list of all the lines that should be in the new file
        :return: Nothing, but writes the CSV File Database with the updated movies.
        """
        with open(self.file_path, "w") as fileobj:
            fileobj.writelines(lines)
            fileobj.close()

        '''
        JSON EQUIVALENT:
        with open(self.file_path, "w") as fileobj:
        json.dump(movies, fileobj, indent=4)
        '''

    def _save_movies_from_dict(self, dict_to_save):

        new_file_lines = []

        for key in dict_to_save.keys():
            new_line = (key + "," +
                        dict_to_save[key]["rating"] + "," +
                        dict_to_save[key]["year"] + "," +
                        dict_to_save[key]["posterImageUrl"]
                        )

            new_file_lines.append(new_line)

        self._save_movies(new_file_lines)

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
        new_line = title + "," + rating + "," + year + "," + poster_image_url + "\n"
        lines.append(new_line)

        self._save_movies(lines)
        print(f"Movie {title} successfully added")
        return

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
            self._save_movies_from_dict(movies)
            print(f"Movie {movie_to_delete} successfully deleted")
        else:
            print(f"Movie {movie_to_delete} not in movies")

    def _update_movie(self):
        """
        Add a film to the movies list.
        Does not need any arguments as we are puling the movie data from the API anyway
        :return: None
        """
        movies = self._open_movies()
        search_title = input("Enter New Film Name: ")

        if search_title not in movies:
            print("This movie does not exists! Maybe a typo?")
            return

        with open(self.file_path, "r") as fileobj:
            lines = fileobj.readlines()

        new_rating = input("Please enter your new rating: ")
        title, year, rating, poster_image_url = api_testing.search_film(search_title)

        for line in range(0, len(lines)):
            if search_title in lines[line]:
                lines[line] = f"{title + "," + new_rating + "," + year + "," + poster_image_url}"
            else:
                continue

        self._save_movies(lines)
        print(f"Ranking of movie {title} successfully updated")

        return
