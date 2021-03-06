#the Manager class from flask-script that will initialize our extension and the Server class that help us launch our server.
# a flask extension called Flask-Script that is a command line parser that will allow us to create startup configurations.
from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Review
from  flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('development')
#test for testing ,development-during development and production -during production

manager = Manager(app)
manager.add_command('server',Server)     # We use the add_command method to create a new command 'server' which will launch our application server.

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command                         #to create a new command.
def test():                              #the test function that loads all the test files and runs them all
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# Flask script allows us to create a Python shell inside our application.
@manager.shell                  # to create a shell contex
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )


if __name__ == '__main__':
    manager.run()
    #  calling the run method on the Manager instance this will run the application

    
# python3 manage.py shell-- use this to access the shell                                                                           to create new user--user_christine = User(username = 'Christine') -- db.session.add_all([user_lisa,user_victor])--used to add multiple data to db
# SQLAlchemy uses sessions as a storage location for our database changes. They mark changes as ready for saving and committing. eg db.session.add(user_christine)   db.session.commit() --to save changes to db
# ------
# about flask-migration
# To use migrations we first need to Initialize our application to use Migrations. ie python3 manage.py db init
# This will create a migrations folder in our root directory. This will be where our migration versions will be stored.
# python3 manage.py db migrate -m "Initial Migration"-----to create first migration version 
# python3.6 manage.py db upgrade ---this upgrades us to that version of the database--to downgrade just use downgrade instead of upgrade

# !!crucial tip!!
# if you encounter errors and decide to delete the migrations app also head to your database and drop the alembic_version table to avoid errors
# heroku addons:create heroku-postgresql --(name of db)   this code just sets up the db on heroku and deals with the db url ..define this new Database URI inside our config.py
#but to actually create a database schema on Heroku Ie specify the rows and columns youll have to type ---- heroku run python3 manage.py db upgrade