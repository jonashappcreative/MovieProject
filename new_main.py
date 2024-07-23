from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def choose_user():

    users = ["user1", "user2", "user3", "user4"]

    print("\nPlease choose the user profile for the Movie App")
    print(f"Available users: {users}")
    user = input("Please enter username: ")

    if user == "user1":
        print("You choose User 1")
        storage = StorageJson("movie_storage_database.json")

    elif user == "user2":
        print("You choose User 2")
        storage = StorageJson("user2.json")

    elif user == "user3":
        print("You choose User 3")
        storage = StorageJson("user3.json")

    elif user == "user4":
        print("You choose User 4")
        storage = StorageCsv("movie_storage_database.csv")

    return storage

def main():
    print("********** My Movies Database **********")

    storage = choose_user()
    movie_app = MovieApp(storage)
    movie_app._run()


if __name__ == "__main__":
    main()
