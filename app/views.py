from flask import render_template,request,redirect,url_for #The request object is provided by flask and it encapsulates our HTTP request with all its arguments to the view function.
from app import app #imports app instance
from .request import get_movies,get_movie,search_movie
from .models import review
from .forms import ReviewForm
Review = review.Review


# We can now make the API call to get a particular category of movies

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query') #We get the query in our view function using request.args.get()function. 

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))# We then pass in the url_for function that passes in the search view function together with the dynamic movie_name which assign it to our form Input value.redirect takes the application to search view function
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie ) #the message in blue represents the variable in the template while the white one is the one shown in the views.py

# to show dynamic routes..the dynamic part is also placed as an argument in the function

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id) #get_reviews class method that takes in a movie ID and will return a list of reviews for that movie. We then pass in the reviews list to our template

    return render_template('movie.html',title = title,movie = movie,reviews = reviews)


#  then create the search view function that will display our search items from the API.
@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)


@app.route('/movie/review/new/<int:id>', methods = ['GET','POST']) #We also add the methods argument to our decorator which tells flask to register the view function as a handler for both GET and POST requests. When methods argument is not given the view function is registered to handle GET requests only.
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit(): #returns True when the form is submitted and all the data has been verified by the validators
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)
