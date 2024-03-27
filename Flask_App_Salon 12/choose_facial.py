from flask import Blueprint, render_template, redirect, url_for


choose_facial_blueprint = Blueprint('choose_facial', __name__)


@choose_facial_blueprint.route('/choose_facial', methods=['GET', 'POST'])
def choose_facial():
    return render_template('choose_facial.html')