from flask import Blueprint, render_template, redirect, url_for


Facial_reflox_blueprint = Blueprint('Facial_reflox', __name__)


@Facial_reflox_blueprint.route('/Facial_reflox', methods=['GET', 'POST'])
def Facial_reflox():
    return render_template('Facial_reflox.html')