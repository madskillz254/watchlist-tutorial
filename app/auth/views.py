from flask import render_template,redirect,url_for, flash,request   #The flash function helps us display error messages to the user.
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message  #--Sending Welcome Email



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title=title)


# We create an instance of the LoginForm and pass it into the login.htmltemplate. 
# Then we check if the form is validated where we search for a user from our database with the email we receive from the form.
# We then use the verify_password method to confirm that the password entered matches with the password hash stored in the database. 
# If they match, we use the login_user function provided by the flask_login extension to record the user as logged for that current session. 
# It takes user object and the remember form data. If True it sets a long time cookie in your browser.



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

# We then call the function  mail_message() inside our register view functio
#  We pass in the the subject and template file where our message body will be stored. 
#  We then pass in the new user's email address which we get from the registration form. We then pass in a user as a keyword argument.



@auth.route('/logout')
@login_required
def logout():
    logout_user()    # calls the flask_login's logout_userfunction. This will logout the user from our application
    return redirect(url_for("main.index"))   #We then redirect the user to the index page.