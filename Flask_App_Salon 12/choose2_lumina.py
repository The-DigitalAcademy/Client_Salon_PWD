from flask import Blueprint, render_template, redirect, url_for


choose2_lumina_blueprint = Blueprint('choose2_lumina', __name__)


@choose2_lumina_blueprint.route('/choose2_lumina', methods=['GET', 'POST'])
def choose2_lumina():
    return render_template('choose2_lumina.html')