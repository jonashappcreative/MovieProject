# import istorage
import storage_json
from movie_app import MovieApp


def main():

    # This somehow needs to be automated and flexible enough
    # to have users added automatically if not in list yet

    '''
    user1 = storage_json.StorageJson("../movie_storage_database.json")
    user2 = storage_json.StorageJson("../user2.json")
    user3 = storage_json.StorageJson("../user3.json")

    print("********** My Movies Database **********")
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
    '''

    storage = storage_json.StorageJson('movie_storage_database.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
