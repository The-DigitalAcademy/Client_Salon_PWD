from flask import Flask, render_template, session
from login import login_blueprint
from register import register_blueprint
from Hair import hair_blueprint
from nails import nails_blueprint
from spar import spar_blueprint
from DB import init_db

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret'  # Set a secret key for flash messages
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SalonDB'

# Initialize database
init_db(app)
# Register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(hair_blueprint)
app.register_blueprint(nails_blueprint)
app.register_blueprint(spar_blueprint)



@app.route('/')
def landing():
    user_email = session.get('email')
    return render_template('landing.html', user_email=user_email)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
