from flask import Blueprint, render_template, redirect, url_for


sharon_salon_blueprint = Blueprint('sharon_salon', __name__)


@sharon_salon_blueprint.route('/sharon_salon', methods=['GET', 'POST'])
def sharon_salon():
    return render_template('sharon_salon.html')