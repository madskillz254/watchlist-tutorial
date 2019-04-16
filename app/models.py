from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))    # modifies the load_userfunction by passing in a user_id to the function that queries the database and gets a User with that ID.


# here we create movie instances from the requests gotten from the api...basically we create atemplatee of what we actually want from the api...a template of the expected outcome
class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count


# to allow users to give reviews for movies they like.
#a class defines how o build an object like how high how low etc
class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

#to save the reviews
    def save_review(self):
        Review.all_reviews.append(self)

#to delete or clear the reviews
    @classmethod    
    def clear_reviews(cls):
        Review.all_reviews.clear()

#  a method that will display all the reviews for a particular movie.
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(UserMixin,db.Model):               # We create a User class that will help us create new users. We pass in db.Model as an argument. This will connect our class to our database and allow communication.
        __tablename__ = 'users'      #__tablename__ variable allows us to give the tables in our database proper names. If not used SQLAlchemy will assume that the tablename is the lowercase of the class name.
        id = db.Column(db.Integer,primary_key = True)
        username = db.Column(db.String(255),index = True)
        email = db.Column(db.String(255),unique = True,index = True)
        role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))     # This tells SQLAlchemy that this is a foreign key and is the ID of a Role model.
        bio = db.Column(db.String(255))                               # users biography 
        profile_pic_path = db.Column(db.String())                     #stores the path of the profile photo

        pass_secure = db.Column(db.String(255))                  
        @property                                                # use the @property decorator to create a write only class property password
        def password(self):
            raise AttributeError('You cannot read the password attribute')
            
        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)        #generates a password hash.


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)     #takes in a hash password and a password entered by a user and checks if the password matches to return a True or False response.


        def __repr__(self):
            return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")     #We use db.relationship to create a virtual column that will connect with the foreign key. We pass in 3 arguments. The first one is the class that we are referencing which is User

    def __repr__(self):
        return f'User {self.name}'

        # a Role class that will define all the different roles. eg admin and user


# create a One-Many relationship between our models. This is that one role can be shared by many different users.
# A Foreign key is a field in one table that references a primary key in another table.















        # Since a single user will represent a row in our table. We create columns using the db.Column class which will represent a single column. We pass in the type of the data to be stored as the first argument. db.Integer specifies the data in that column should be an Integer.
        #  Every row must have a primary key set to it. By default the Column class has primary_key set to False. We want to set it to True on the id column to set it as the primary_key column.
        # Thedb.String class specifies the data in that column should be a string with a maximum of 255 characters.

        # The __repr__method is not really important. It makes it easier to debug our applications.
