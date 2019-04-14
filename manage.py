#the Manager class from flask-script that will initialize our extension and the Server class that help us launch our server.
# a flask extension called Flask-Script that is a command line parser that will allow us to create startup configurations.
from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)     # We use the add_command method to create a new command 'server' which will launch our application server.

@manager.command                         #to create a new command.
def test():                              #the test function that loads all the test files and runs them all
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
    #  calling the run method on the Manager instance this will run the application.