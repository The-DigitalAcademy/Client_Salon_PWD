from flask import Blueprint, render_template, redirect, url_for


choose_nails3_blueprint = Blueprint('choose_nails3', __name__)


@choose_nails3_blueprint.route('/choose_nails3', methods=['GET', 'POST'])
def choose_nails3():
    return render_template('choose_nails3.html')