from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    print("********** My Movies Database **********")

    storage = StorageCsv('movie_storage_database.csv')
    movie_app = MovieApp(storage)
    movie_app._run()

    # print("Did it run? Debug")

if __name__ == "__main__":
    main()
