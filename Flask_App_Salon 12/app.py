from flask import Flask, render_template, session
from login import login_blueprint
from register import register_blueprint
from Hair import hair_blueprint
from register import register_blueprint
from nails import nails_blueprint
from facial import facial_blueprint
from spar import spar_blueprint
from Glit_glamour import Glit_glamour_blueprint
from forgot_password import forgot_password_blueprint
from Lumina_salon import Lumina_salon_blueprint
from Sharon_salon import Sharon_salon_blueprint
from Enchant_spar import Enchant_spar_blueprint
from Serene_salon import Serene_salon_blueprint
from Belle_salon import Belle_salon_blueprint
from Services_sharon import Services_sharon_blueprint
from Service_lumina import Service_lumina_blueprint
from Service_enchant import Service_enchant_blueprint
from enchant_salon import enchant_salon_blueprint
from Service_glit import Service_glit_blueprint
from Service_serene import Service_serene_blueprint
from Choose_lumina import Choose_lumina_blueprint
from choose2_lumina import choose2_lumina_blueprint
from choose_facial import choose_facial_blueprint
from Classic_facial import Classic_facial_blueprint
from Facial_reflox import Facial_reflox_blueprint
from Shiatsu_facial import Shiatsu_facial_blueprint
from choose_body import choose_body_blueprint
from choose_treatment import choose_treatment_blueprint
from choose_treatments2 import choose_treatments2_blueprint
from choose_treatments3 import choose_treatments3_blueprint
from choose_nails import choose_nails_blueprint
from choose_nails1 import choose_nails1_blueprint
from choose_nails2 import choose_nails2_blueprint
from choose_nails3 import choose_nails3_blueprint
from Calendar import Calendar_blueprint






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
app.register_blueprint(facial_blueprint)
app.register_blueprint(forgot_password_blueprint)
app.register_blueprint(Glit_glamour_blueprint)
app.register_blueprint(Lumina_salon_blueprint)
app.register_blueprint(Sharon_salon_blueprint)
app.register_blueprint(Enchant_spar_blueprint)
app.register_blueprint(Serene_salon_blueprint)
app.register_blueprint(Belle_salon_blueprint)
app.register_blueprint(Services_sharon_blueprint)
app.register_blueprint(Service_lumina_blueprint)
app.register_blueprint(Service_enchant_blueprint)
app.register_blueprint(enchant_salon_blueprint)
app.register_blueprint(Service_glit_blueprint)
app.register_blueprint(Service_serene_blueprint)
app.register_blueprint(Choose_lumina_blueprint)
app.register_blueprint(choose2_lumina_blueprint)
app.register_blueprint(choose_facial_blueprint)
app.register_blueprint(Classic_facial_blueprint)
app.register_blueprint(Facial_reflox_blueprint)
app.register_blueprint(Shiatsu_facial_blueprint)
app.register_blueprint(choose_body_blueprint)
app.register_blueprint(choose_treatment_blueprint)
app.register_blueprint(choose_treatments2_blueprint)
app.register_blueprint(choose_treatments3_blueprint)
app.register_blueprint(choose_nails_blueprint)
app.register_blueprint(choose_nails1_blueprint)
app.register_blueprint(choose_nails2_blueprint)
app.register_blueprint(choose_nails3_blueprint)
app.register_blueprint(Calendar_blueprint)




@app.route('/')
def landing():
    user_email = session.get('email')
    return render_template('landing.html', user_email=user_email)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
