from movie_app import MovieApp
from storage_json import StorageJson


def main():
    print("********** My Movies Database **********")

    storage = StorageJson('movie_storage_database.json')
    movie_app = MovieApp(storage)
    movie_app._run()

    # print("Did it run? Debug")

if __name__ == "__main__":
    main()
