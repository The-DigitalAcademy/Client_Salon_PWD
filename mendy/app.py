from flask import Flask , render_template, request 
from flask_pymongo import PyMongo

app = Flask ("_name_")

app.config["MONGO_URI"] = "mongodb://localhost:27017/Salon"  # Replace with your MongoDB connection URI
mongo = PyMongo(app)
db = mongo.db

@app.route("/login", methods=('post'))
def login ():
    if request.method == 'post':
        username = request.form.get ('username')
        password = request.form.get ('password')
        forgot_password = request.form.get ('forgot_password')


        user = {username: 'username', password: 'password', forgot_password: 'forgot_password' }

        db.salon.insert_one (user)  

    return render_template("Login.html")



if "_name_" == '_main_':

    app.run (debug=True)