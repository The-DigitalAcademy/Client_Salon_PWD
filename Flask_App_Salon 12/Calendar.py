
from flask import Blueprint, Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

Calendar_blueprint = Blueprint('Calendar', __name__)

# Replace 'db' with your MongoDB database
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SalonDB'
mongo = PyMongo(app)


@Calendar_blueprint.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        bookingdate = request.form.get('bookingdate')
        time = request.form.get('time')

        mongo.db.Calendar.insert_one({"date": bookingdate, "time": time})

        return render_template('Calendar.html')

   



