from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson


def choose_user():
    """
    A function that covers the initial choice of which user is using the Movie App.
    The users are currently hard coded into a list of users, but can be later saved in a user's database.
    Each user is currently connected to its databases filepath.

    :return: The Object of the Storage Type and Filepath that will be used in the MovieApp.
    """
    users = ["user1", "user2", "user3", "user4"]

    print("\nPlease choose the user profile for the Movie App")
    print(f"Available users: {users}")
    user = input("Please enter username: ")

    if user == "user1":
        print("You choose User 1")
        storage = StorageJson("Data/movie_storage_database.json")

    elif user == "user2":
        print("You choose User 2")
        storage = StorageJson("Data/user2.json")

    elif user == "user3":
        print("You choose User 3")
        storage = StorageJson("Data/user3.json")

    elif user == "user4":
        print("You choose User 4")
        storage = StorageCsv("Data/movie_storage_database.csv")

    else:
        print("You choose User 1 as default")
        storage = StorageJson("Data/movie_storage_database.json")

    return storage


def main():
    """
    Runs the MovieApp using the Storage Item chosen in the prior function.
    Executed until run is stopped by the user by the bool running_choice.
    :return: Nothing
    """
    print("********** My Movies Database **********")

    storage = choose_user()
    movie_app = MovieApp(storage)

    running_status = True

    while running_status:
        running_status = movie_app._run()


if __name__ == "__main__":
    main()
