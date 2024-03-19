from flask import Blueprint, render_template, redirect, url_for


Lumina_salon_blueprint = Blueprint('Lumina_salon', __name__)


@Lumina_salon_blueprint.route('/Lumina_salon', methods=['GET', 'POST'])
def Lumina_salon():
    return render_template('Lumina_salon.html')