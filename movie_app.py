import statistics
import random
from web_generator import write_html


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _choose_user(self):
        users = ["user1", "user2", "user3", "user4"]

        print("Please choose the user profile for the Movie App")
        print(f"Available users: {users}")
        user = input("Please enter username: ")

        return user

    def _print_menu(self):

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

    def _get_user_choice(self):

        choice = -1
        while choice not in range(0, 10):
            choice = int(input("Enter choice (0-9): "))

            if choice not in range(0, 10):
                print("Not a valid option. Please try again.")

        return choice

    def _sort_dict_by_value_ranking(self):
        movies = self._storage._open_movies()
        ranking = sorted(movies.items(), key=lambda item: item[1]['rating'], reverse=True)
        # Debug: print(ranking)
        return ranking

    def _calc_statistics(self, movies):
        """

        :param movies: All the Movies in the given List
        :return:
        """

        list_of_ratings = []
        for movie in movies.keys():
            rating = float(movies[movie]["rating"])
            list_of_ratings.append(rating)

        ranking = self._sort_dict_by_value_ranking()

        average = statistics.mean(list_of_ratings)
        median = statistics.median(list_of_ratings)

        # Gets the highest and lowest values to check if there are multiple ones with same value
        # dict = rankin, item 0 and -1 is first and last place, [1] gets the value
        highest_rating = ranking[0][1]['rating']
        lowest_rating = ranking[-1][1]['rating']

        # empty lists with the best movies and worst movies
        best_movies = []
        worst_movies = []

        for name, details in ranking:
            if details['rating'] == highest_rating:
                best_movies.append((name, details['rating']))
            elif details['rating'] == lowest_rating:
                worst_movies.append((name, details['rating']))

        # Formats List of Best/Worst Movie Tuples to String
        best_movies_string = ', '.join(f"{title} - {rating}" for title, rating in best_movies)
        worst_movies_string = ', '.join(f"{title} - {rating}" for title, rating in worst_movies)

        return average, median, best_movies_string, worst_movies_string

    def _stats(self):
        movies = self._storage._open_movies()
        average, median, best, worst = self._calc_statistics(movies)

        print()
        print(f"Average rating: {round(average, 2)}")
        print(f"Median rating: {round(median, 2)}")
        print(f"Best movie: {best}")
        print(f"Worst movie: {worst}")

    def _random_movie(self):
        movies = self._storage._open_movies()  # Reload data
        movie = random.choice(list(movies.keys()))
        print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")

    def _search_movie(self):
        movies = self._storage._open_movies()  # Reload data
        search_for = str(input("Enter part of movie name: "))

        for movie in movies:
            if search_for.lower() in movie.lower():
                print(movie)

    def _movies_sorted_by_rating(self):
        movies = self._storage._open_movies()
        ranking = self._sort_dict_by_value_ranking()

        for movie, rating in ranking:
            print(f"{movie}: {movies[movie]['rating']}")

    def _execute_user_choice(self, choice):

        if choice == 0:
            print("See you next time!")
            return False
        elif choice == 1:
            print("\nList Of Movies:")
            return self._storage._list_movies()
        elif choice == 2:
            print("\nAdd Movie:")
            return self._storage._add_movie()
        elif choice == 3:
            print("\nDelete Movie:")
            return self._storage._delete_movie()
        elif choice == 4:
            print("\nUpdate Movie:")
            return self._storage._update_movie()
        elif choice == 5:
            print("\nStatistics:")
            return self._stats()
        elif choice == 6:
            print("\nRandom Movie:")
            return self._random_movie()
        elif choice == 7:
            print("\nSearch Movie:")
            return self._search_movie()
        elif choice == 8:
            print("\nMovies Sorted By Rating:")
            return self._movies_sorted_by_rating()
        elif choice == 9:
            movies = self._storage._open_movies()
            write_html(movies)
            print("\nWebsite was generated successfully.")

    def _run(self):
        self._print_menu()
        choice = self._get_user_choice()
        self._execute_user_choice(choice)
