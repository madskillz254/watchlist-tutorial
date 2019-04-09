# This is where we will write code to make requests to our API.
from app import app
import urllib.request,json
# urllib.request module that will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import movie

Movie = movie.Movie


# Getting api key
api_key = app.config['MOVIE_API_KEY']
# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]


def get_movies(category):
    '''
    Function that gets the json response to our url request
    We use the .format() method on the base_url and pass in the movie category and the api_key. This will replace the {} 
    curly brace placeholders in the base_url with the category and api_key respectively.
    '''
    get_movies_url = base_url.format(category,api_key)

# This creates get_movies_url as the final URL for our API request.
# We then use with as our context manager to send a request using the urllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url
# We use the read() function to read the response and store it in a get_movies_data variable.
# We then convert the JSON response to a Python dictionary using json.loads function
# We then check if the response contains any data
# from the json response , we have a property  results which is a list that contains the movie objects
# This property is what we use to check if the response contains any data.If it does we call a process_results() function that takes in the list of dictionary objects and returns a list of movie objects .
# We then return movie_results which is a list of movie objects.

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read() 
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

# create a function process_results() that takes in a list of dictionaries
# create an empty list movie_results this is where we will store our newly created movie objects.
# We then loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values...ie movie-item.get("overview")..the argument passed here is the name given in the python dictionary in results list
# if the movie_item has a poster then we create the movie object to prevent errors for movies without posters

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    
    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results


# now create our movie details page in our application. First we need to get the movie.
#  function that takes in a movie id and returns a movie object.
# We create a get_movie_details URL by formatting the base URL with the idand API key.
# We then create a request and load the data and create a movie object.
def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object


# We are going to implement a search functionality from our API. Let us first create the search request.
# We use the countfilter that counts all the items in a list.
def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results


