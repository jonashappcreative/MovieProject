import random
import statistics
import movie_storage
from web_generator import write_html
from storage_json import StorageJson

# used to reload the module each time it was used in menu
import importlib

# color
# fuzzy matching
# histogram


def initial_welcome():
    print("********** My Movies Database **********")


def menu_choice():
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


def list_movies():
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
    # data_storage =
    # Define which data storage should be used (which user, filetype)

    movies = movie_storage.open_movies()
    print(f"{len(movies)} movies in total")

    for movie, details in movies.items():
        print(f"{movie}: {details['rating']}")


def add_movie_api():
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # Get the data from the JSON file
    movies = movie_storage.open_movies()
    new_movie = input("Enter New Film Name: ")

    if new_movie in movies.keys():
        print("This movie already exists! Did you want to update instead?")
        return

    movie_storage.add_movie_by_api(new_movie)


def delete_movie(movies):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movie_to_delete = input("Enter movie name to delete: ")

    if movie_to_delete in movies:
        movie_storage.delete_movie_from_database(movie_to_delete)
        print(f"Movie {movie_to_delete} successfully deleted")
    else:
        print(f"Movie {movie_to_delete} not in movies")


def update_movie_main():
    """
    Not used anymore after API
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """

    movie_to_update = input("Enter movie name: ")
    movie_storage.update_movie(movie_to_update)


def sort_dict_by_value_ranking(movies):
    ranking = sorted(movies.items(), key=lambda item: item[1]['rating'], reverse=True)
    # Debug: print(ranking)
    return ranking


def calc_statistics(movies):
    """

    :param movies: All the Movies in the given List
    :return:
    """
    list_of_ratings = []
    for movie in movies.keys():
        rating = float(movies[movie]["rating"])
        list_of_ratings.append(rating)

    ranking = sort_dict_by_value_ranking(movies)

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


def stats(movies):
    average, median, best, worst = calc_statistics(movies)

    print()

    print(f"Average rating: {round(average, 2)}")
    print(f"Median rating: {round(median, 2)}")
    print(f"Best movie: {best}")
    print(f"Worst movie: {worst}")


def random_movie(movies):
    movie = random.choice(list(movies.keys()))
    print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")


def search_movie(movies):
    search_for = str(input("Enter part of movie name: "))

    for movie in movies:
        if search_for.lower() in movie.lower():
            print(movie)


def movies_sorted_by_rating(movies):
    ranking = sort_dict_by_value_ranking(movies)

    for movie, rating in ranking:
        print(f"{movie}: {movies[movie]['rating']}")


def generate_website(movies):
    write_html(movies)


def choose_user_database():

    users = ["user1", "user2", "user3"]

    print("Please choose the user profile for the Movie App")
    print(f"Available users: {users}")
    user = input("Please enter username: ")

    return user


def execute_function(choice, storage):
    if choice == 0:
        print("Bye")
        return False
    elif choice == 1:
        print("\nList Of Movies:")
        return storage._list_movies()
    elif choice == 2:
        print("\nAdd Movie:")
        return storage._add_movie()
    elif choice == 3:
        print("\nDelete Movie:")
        return storage._delete_movie()
    elif choice == 4:
        print("\nUpdate Movie:")
        return storage._update_movie_main()
    elif choice == 5:
        print("\nStatistics:")
        movies = storage._open_movies()
        return stats(movies)
    elif choice == 6:
        print("\nRandom Movie:")
        movies = storage._open_movies()        # Reload data
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


def main():

    user1 = StorageJson("movie_storage_database.json")
    user2 = StorageJson("user2.json")
    user3 = StorageJson("user3.json")

    initial_welcome()
    user = choose_user_database()

    if user == "user1":
        print("You Choose User 1")
        user = user1

    elif user == "user2":
        print("You Choose User 2")
        user = user2

    elif user == "user3":
        print("You Choose User 3")
        user = user3

    # Asks the user for which user (or database) to select
    # movie_storage = choose_user_database()

    running = True
    while running:

        # Reloads the Module so the database refreshes
        importlib.reload(movie_storage)

        choice = menu_choice()

        if choice == 0:
            print("Bye!")
            quit()

        execute_function(choice, storage=user)

        try:
            continue_input = input("\nPress 'Enter' to continue or 'Q' to quit: ")
        except ValueError:
            continue_input = True

        if continue_input.lower() == 'q':
            break
        elif continue_input:
            print("EXECUTED")
            movies = movie_storage.open_movies()  # Ensure fresh data after any operation

    print("You Quit")


if __name__ == "__main__":
    main()
