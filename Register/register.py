# register.py
from flask import Blueprint, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from DB import Database

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user input from the registration form
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Validate input data
        if not name or not address or not email or not password or not confirm_password:
            return render_template('register.html', registerMessage='All fields are required.')

        # Perform password and confirm password validation
        if password != confirm_password:
            return render_template('register.html', registerMessage='Password and Confirm Password do not match.')

        # Check if the username or email is already registered
        db = Database()
        existing_email = db.find_user_by_email(email)

        if existing_email:
            return render_template('register.html', registerMessage='Email is already registered. Please use another one.')

        # Hash the password before inserting it into the MongoDB collection
        hashed_password = generate_password_hash(password, method='sha256')
        db.insert_user(name, address, email, hashed_password)

        return render_template('register.html', registerMessage='Registration successful!')

    return render_template('register.html')
