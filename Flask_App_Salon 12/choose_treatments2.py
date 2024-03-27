from flask import Blueprint, render_template, redirect, url_for


choose_treatments2_blueprint = Blueprint('choose_treatments2', __name__)


@choose_treatments2_blueprint.route('/choose_treatments2', methods=['GET', 'POST'])
def choose_treatments2():
    return render_template('choose_treatments2.html')