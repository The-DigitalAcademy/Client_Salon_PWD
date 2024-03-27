from flask import Blueprint, render_template, redirect, url_for


choose_treatments3_blueprint = Blueprint('choose_treatments3', __name__)


@choose_treatments3_blueprint.route('/choose_treatments3', methods=['GET', 'POST'])
def choose_treatments3():
    return render_template('choose_treatments3.html')