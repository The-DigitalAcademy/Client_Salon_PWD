from flask import Blueprint, render_template, redirect, url_for


choose_nails1_blueprint = Blueprint('choose_nails1', __name__)


@choose_nails1_blueprint.route('/choose_nails1', methods=['GET', 'POST'])
def choose_nails1():
    return render_template('choose_nails1.html')