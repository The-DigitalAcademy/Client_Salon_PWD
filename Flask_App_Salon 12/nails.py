from flask import Blueprint, render_template, redirect, url_for


nails_blueprint = Blueprint('nails', __name__)


@nails_blueprint.route('/nails', methods=['GET', 'POST'])
def hair_salon():
    return render_template('nails.html')