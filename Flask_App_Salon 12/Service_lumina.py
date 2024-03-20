from flask import Blueprint, render_template, redirect, url_for


Service_lumina_blueprint = Blueprint('Service_lumina', __name__)


@Service_lumina_blueprint.route('/Service_lumina', methods=['GET', 'POST'])
def Service_lumina():
    
    return render_template('Service_lumina.html')