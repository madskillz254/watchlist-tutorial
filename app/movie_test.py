# to test that the movie class in the models folder works well
import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))
        # isinstance() function that checks if the object self.new_movie is an instance of the Movie class.
    

# We see some new syntax here self.assertEqual() this is a TestCase method that checks for an expected result. The first argument is the expected result and the second argument is the result that is actually gotten.  Here, we are checking if the name and description 
# of our new object is what we actually inputted.
# use the assertTrue method provided by the TestCase class to check if the return value is True

if __name__ == '__main__':
    unittest.main()
