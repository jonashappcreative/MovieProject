import random
import statistics
from archive import old_movie_storage
from web_generator import write_html
from storage_json import StorageJson
from archive.old_main_phase2 import calc_statistics

# used to reload the module each time it was used in menu
import importlib


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        # movies = movie_storage.open_movies()  # My Old line of Code
        print(f"{len(movies)} movies in total")

        for movie, details in movies.items():
            print(f"{movie}: {details['rating']}")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()

        average, median, best, worst = calc_statistics(movies)
        print()

        print(f"Average rating: {round(average, 2)}")
        print(f"Median rating: {round(median, 2)}")
        print(f"Best movie: {best}")
        print(f"Worst movie: {worst}")

    def _generate_website(self):
        movies = self._storage.list_movies()
        write_html(movies)

    def _search_movie(self):
        movies = self._storage.list_movies()
        search_for = str(input("Enter part of movie name: "))

        for movie in movies:
            if search_for.lower() in movie.lower():
                print(movie)

    def _add_movie_by_api(self, search_title):

        movies = self._storage.list_movies()

        try:
            title, year, rating, poster_image_url = api_testing.search_film(search_title)

        # Exits this part of the Code when a None is returned by API, Warning was already Printed to user
        except TypeError:
            return

        movies[title] = {"rating": rating, "year": year, "poster image url": poster_image_url}
        print(f"Movie {title} successfully added")
        save_movies(movies)

    def _movies_sorted_by_rating(self):
        movies = self._storage.list_movies()
        ranking = old_movie_storage.sort_dict_by_value_ranking(movies)

        for movie, rating in ranking:
            print(f"{movie}: {movies[movie]['rating']}")

    def _menu_choice(self):
        # need to fix: write in multiple lines to keep line under 140 chars
        print(
            "\nMenu:\n"
            "0. Exit\n"
            "1. List movies\n"
            "2. Add movie\n"
            "3. Delete movie\n"
            "4. Update movie\n"
            "5. Stats\n"
            "6. Random movie\n"
            "7. Search movie\n"
            "8. Movies sorted by rating\n"
            "9. Generate Website\n"
        )

        choice = -1
        while choice not in range(0, 10):
            choice = int(input("Enter choice (0-9): "))

            if choice not in range(0, 10):
                print("Not a valid option. Please try again.")

        return choice


    def _execute_function(self, choice):

        choice = self._menu_choice()

        if choice == 0:
            print("Bye!")
            return False
        elif choice == 1:
            print("\nList Of Movies:")
            return self._command_list_movies()
        elif choice == 2:
            print("\nAdd Movie:")
            return self._add_movie()
        elif choice == 3:
            print("\nDelete Movie:")
            return storage._delete_movie()
        elif choice == 4:
            print("\nUpdate Movie:")
            return storage._update_movie_main()
        elif choice == 5:
            print("\nStatistics:")
            movies = storage._open_movies()
            return self._command_movie_stats()
        elif choice == 6:
            print("\nRandom Movie:")
            movies = self._storage._open_movies()  # Reload data
            return random_movie(movies)
        elif choice == 7:
            print("\nSearch Movie:")
            movies = storage._open_movies()  # Reload data
            return search_movie(movies)
        elif choice == 8:
            movies = storage._open_movies()  # Reload data before sorting
            print("\nMovies Sorted By Rating:")
            return movies_sorted_by_rating(movies)
        elif choice == 9:
            movies = storage._open_movies()  # Reload data before sorting
            generate_website(movies)
            print("\nWebsite was generated successfully.")

    def run(self):

        running = True
        while running:

            # Reloads the Module so the database refreshes
            importlib.reload(old_movie_storage)
            running = self._execute_function()

        if not running:
            quit()

        try:
            continue_input = input("\nPress 'Enter' to continue or 'Q' to quit: ")
        except ValueError:
            continue_input = True

        if continue_input.lower() == 'q':
            print("Bye!")
        elif continue_input:
            print("EXECUTED")
            movies = self._open_movies()  # Ensure fresh data after any operation

        print("You Quit")

        # Print menu
        # Get use command
        # Execute command
