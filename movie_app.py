import statistics


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage._list_movies()
        ...

    def _command_movie_stats(self):
        pass

    def _generate_website(self):
        pass

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

    def _run(self):
        self._print_menu()
        choice = self._get_user_choice()
        self._execute_user_choice(choice)
