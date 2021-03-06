from flask import render_template,request,redirect,url_for,abort  #The request object is provided by flask and it encapsulates our HTTP request with all its arguments to the view function. --abort function, that stops a request, and returns a response according to the status code passed in
from . import main
import markdown2                                                     # responsible for the conversion from markdown to HTML.
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm,UpdateProfile
from ..models import Review,User
from .. import db,photos                               #we will need it when saving profile information changes to the database.
from flask_login import login_required, current_user   #login_required decorator will intercept a request and check if the user is authenticated and if not the user will be redirected to the login page.

#  We use one dot .modulename to import modules that are located within the same package, and two dots ..modulename for modules located in a package higher up in the project hierarchy.
# We can now make the API call to get a particular category of movies

@main.route('/')
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
        return redirect(url_for('main.search',movie_name=search_movie))# We then pass in the url_for function that passes in the search view function together with the dynamic movie_name which assign it to our form Input value.redirect takes the application to search view function
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie ) #the message in blue represents the variable in the template while the white one is the one shown in the views.py

# to show dynamic routes..the dynamic part is also placed as an argument in the function

@main.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id) #get_reviews class method that takes in a movie ID and will return a list of reviews for that movie. We then pass in the reviews list to our template

    return render_template('movie.html',title = title,movie = movie,reviews = reviews)


#  then create the search view function that will display our search items from the API.
@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST']) #We also add the methods argument to our decorator which tells flask to register the view function as a handler for both GET and POST requests. When methods argument is not given the view function is registered to handle GET requests only.
@login_required
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit(): #returns True when the form is submitted and all the data has been verified by the validators
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)


@main.route('/review/<int:id>')
@login_required
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)




# url_for() functions in Blueprints
# Flask adds a namespace to all endpoints from a blueprint. The namespace is generally the name of the blueprint. 
# For example the index() view function is registerd as url_for('main.index'). url_for also supports a shorthand format using .. url_for('main.index') can be shortened to url_for('.index')

# a profile view function.

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()       #We query the database to find a user with the same username.
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



# We first import the photos instance from our application factory module. We then create a route that will process our form submission request. This route only accepts post requests.
# We then query the database to pick a user with the same username we passed in. We then use the flask request function to check if any parameter with the name photo has been passed into the request.
# We use the save method to save the file into our application. We then create a path variable to where the file is stored. We then update the profile_pic_path property in our user table and store the path to the file.
# We finally commit the changes to the database and redirect the user back to the profile page.