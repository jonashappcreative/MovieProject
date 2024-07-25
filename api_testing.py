import requests

# Needs a git ignore and separate API Var Import
API_KEY = 'bd0f0f8a'

def search_film(search_title):
    """
    Gets the required Data for the data files based on users search, handles the API Request
    :param search_title: The users search for a title inclusing spaces
    :return: title, year, rating, poster_image_url Tuple as processed in api_data_handling
    """

    search_title = search_title.replace(' ', '%20')
    api_url = f"https://www.omdbapi.com/?i=tt3896198&apikey={API_KEY}&t={search_title}"
    # print(api_url)
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert response to JSON format
        film_data = response.json()

        if film_data["Response"]:
            return api_data_handling(film_data)
        if not film_data["Response"]:
            print(film_data["Error"])
            print("Please start process again and try another film title")

    else:
        print("Failed to retrieve data:", response.status_code)


def api_data_handling(data):
    """
    Gets the required Data from the JSON Document the API Provided
    :param data: DICT from API
    :return: Tuple: title, year, rating, poster_image_url
    """
    try:
        title = data["Title"]
        year = data["Year"]
        rating = data["imdbRating"]
        poster_image_url = data["Poster"]

        # print(title, year, rating, poster_image_url)
        return title, year, rating, poster_image_url

    # Looking for a Type Error raised by type title == None: Indicates no entry in database
    except KeyError:
        print("Couldn't find title in the Database! Please Try Again")
