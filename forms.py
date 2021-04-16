from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField

class SignUpForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email address')
    #sport = StringField('Sport (supports "swim", "baseball", "soccer", and "none")')

    sport = SelectField(
        'Sports',
        choices=[('swim', 'Swim'), ('baseball', 'Baseball'), ('soccer', 'Soccer'), ('none', 'No Sport')]
    )
        
    submit = SubmitField("Submit")

class WeightForm(FlaskForm):

    wk1ex1 = StringField('Exercise 1')
    wk1ex2 = StringField('Exercise 2')
    wk1ex3 = StringField('Exercise 3')
    wk1ex4 = StringField('Exercise 4')
    wk1ex5 = StringField('Exercise 5')

    wk2ex1 = StringField('Exercise 1')
    wk2ex2 = StringField('Exercise 2')
    wk2ex3 = StringField('Exercise 3')
    wk2ex4 = StringField('Exercise 4')
    wk2ex5 = StringField('Exercise 5')

    submit = SubmitField("Submit")