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


