from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:5000/Salon"
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG"] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

bootstrap = Bootstrap(app)
mongo = PyMongo(app)
db = mongo.db


class SignupForm(FlaskForm):
    username = StringField('Name & Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    username = StringField('Name & Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@app.route("/index", methods=["POST", "GET"])
def index():
    form = SignupForm()

    if form.validate_on_submit():
        # Get the user data from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
       
        # Insert the user document into the collection
        user = {
            'username': username,
            'email': email,
            'password': password,
            
        }
        db.Salon.insert_one(user)

        return render_template('index.html', form=form, success=True)

    return render_template('index.html', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Get the user data from the form
        username = form.username.data
        password = form.password.data

        # Insert the user document into the collection
        user = {
            'username': username,
            'password': password
        }
        db.Salon.insert_one(user)

        return render_template('login.html', form=form, success=True)

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)1