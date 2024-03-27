from flask import Blueprint, render_template, redirect, url_for


choose_body_blueprint = Blueprint('choose_body', __name__)


@choose_body_blueprint.route('/choose_body', methods=['GET', 'POST'])
def choose_body():
    return render_template('choose_body.html')