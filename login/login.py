# login.py
from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
from DB import Database

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from the login form
        email = request.form['email']
        password = request.form['password']

        # Validate input data
        if not email or not password:
            return render_template('login.html', loginMessage='Email and password are required.')

        # Validate user credentials
        db = Database()
        user = db.find_user_by_email(email)

        if user and check_password_hash(user['password'], password):
            # Perform login actions (e.g., set session variables)
            session['user_id'] = str(user['_id'])  # Assuming you have a user ID in your database
            return redirect(url_for('home'))  # Redirect to the home page after successful login
        else:
            return render_template('login.html', loginMessage='Invalid username or password.')

    return render_template('login.html')
