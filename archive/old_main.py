import random
import statistics

#color
#fuzzy matching
#histogram


def initial_welcome():
    print("********** My Movies Database **********")


def menu_choice():
    # need to fix: write in multiple lines to keep line under 140 chars
    print(
        "\nMenu:\n"
        "1. List movies\n"
        "2. Add movie\n"
        "3. Delete movie\n"
        "4. Update movie\n"
        "5. Stats\n"
        "6. Random movie\n"
        "7. Search movie\n"
        "8. Movies sorted by rating\n"
    )

    choice = 0
    while choice not in range(1, 9):
        choice = int(input("Enter choice (1-8): "))

        if choice not in range(1, 9):
            print("Not a valid option. Please try again.")

    return choice


def list_movies(movies):

    print(f"{len(movies)} movies in total")

    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movies):

    movie = input("Enter New Film Name: ")
    rating = int(input("Enter new movie rating (0-10): "))
    movies[movie] = rating
    print(f"Movie {movie} successfully added")


def delete_movie(movies):
    movie_to_delete = input("Enter movie name to delete: ")

    if movie_to_delete in movies:

        del movies[movie_to_delete]
        print(f"Movie {movie_to_delete} successfully deleted")
    else:
        print(f"Movie {movie_to_delete} not in movies")


def update_movie(movies):

    movie_to_update = input("Enter movie name: ")

    if movie_to_update in movies:
        rating_new = float(input("Enter new movie rating (0-10): "))
        movies.update({movie_to_update: rating_new})
        print(f"Movie {movie_to_update} successfully updated")
    else:
        print(f"Movie {movie_to_update} not in movies")


def sort_dict_by_value_ranking(movies):
    ranking = sorted(movies.items(), reverse=True, key=lambda x: x[1])
    return ranking


def calc_statistics(movies):

    list_of_ratings = list(movies.values())
    ranking = sort_dict_by_value_ranking(movies)

    average = round(sum(list_of_ratings) / len(movies), 2)
    median = statistics.median(list_of_ratings)

    # Gets the highest and lowest values to check if there are multiple ones with same value
    # dict = rankin, item 0 and -1 is first and last place, [1] gets the value
    highest_rating = ranking[0][1]
    lowest_rating = ranking[-1][1]

    # empty list with best movies and worst movies
    best_movies = []
    worst_movies = []

    for name, rate in ranking:
        if rate == highest_rating:
            best_movies.append((name, rate))
        elif rate == lowest_rating:
            worst_movies.append((name, rate))

    best = ""
    worst = ""

    for name, rate in best_movies:
        if best:
            best += ', '

        best += f"{name}: {rate}"

    for name, rate in worst_movies:
        if worst:
            worst += ', '
        worst += f"{name}: {rate}"

    return average, median, best, worst


def stats(movies):
    average, median, best, worst = calc_statistics(movies)

    print(f"Average rating: {average}")
    print(f"Median rating: {median}")
    print(f"Best movie: {best}")
    print(f"Worst movie: {worst}")


def random_movie(movies):
    movie, rating = random.choice(list(movies.items()))
    print(f"Your movie for tonight: {movie}, it's rated {rating}")


def search_movie(movies):
    search_for = str(input("Enter part of movie name: "))

    for movie in movies:
        if search_for.lower() in movie.lower():
            print(movie)


def movies_sorted_by_rating(movies):
    ranking = sort_dict_by_value_ranking(movies)

    for movie, rating in ranking:
        print(f"{movie}: {rating}")


def execute_function(choice, movies):

    if choice == 1:
        print("\nList Of Movies:")
        return list_movies(movies)
    elif choice == 2:
        print("\nAdd Movie:")
        return add_movie(movies)
    elif choice == 3:
        print("\nDelete Movie:")
        return delete_movie(movies)
    elif choice == 4:
        print("\nUpdate Movie:")
        return update_movie(movies)
    elif choice == 5:
        print("\nStatistics:")
        return stats(movies)
    elif choice == 6:
        print("\nRandom Movie:")
        return random_movie(movies)
    elif choice == 7:
        print("\nSearch Movie:")
        return search_movie(movies)
    elif choice == 8:
        print("\nMovies Sorted By Rating:")
        return movies_sorted_by_rating(movies)


def histogram(movies, movie):
    pass


def main():

    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 3.6,
        "The Godfather: Part II": 9.5,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 7.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    initial_welcome()

    running = True
    while running:

        choice = menu_choice()
        execute_function(choice, movies)
        continue_input = input("\nPress 'Enter' to continue or 'Q' to quit: ")

        if continue_input == True:
            continue
        elif continue_input == 'q' or continue_input == 'Q':
            break

    print("You Quit")


if __name__ == "__main__":
    main()
