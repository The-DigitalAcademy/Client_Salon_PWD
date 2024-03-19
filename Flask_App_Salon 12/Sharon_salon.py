from flask import Blueprint, render_template, redirect, url_for


Sharon_salon_blueprint = Blueprint('Sharon_salon', __name__)


@Sharon_salon_blueprint.route('/Sharon_salon', methods=['GET', 'POST'])
def Sharon_salon():
    return render_template('Sharon_salon.html')