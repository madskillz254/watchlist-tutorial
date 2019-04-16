from flask_wtf import FlaskForm  #this will help us create a Form class
from wtforms import StringField,TextAreaField,SubmitField #will help us create a text field, a text Area field and a submit button
from wtforms.validators import Required  #will prevent the user from submitting the form without Inputting a value

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
    # We Initialize the Field types by passing in two parameters. The first is the label and the second is a list of Validators where we initialize the Required validator.
 


# We want to update our bio to say something interesting about us.


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')