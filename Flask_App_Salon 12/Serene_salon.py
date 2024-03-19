from flask import Blueprint, render_template, redirect, url_for


Serene_salon_blueprint = Blueprint('Serene_salon', __name__)


@Serene_salon_blueprint.route('/Serene_salon', methods=['GET', 'POST'])
def Serene_salon():
    return render_template('Serene_salon.html')