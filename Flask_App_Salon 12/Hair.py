from flask import Blueprint, render_template, redirect, url_for


hair_blueprint = Blueprint('hair_salon', __name__)


@hair_blueprint.route('/hair_salon', methods=['GET', 'POST'])
def hair_salon():
    return render_template('hair_salon.html')
    





