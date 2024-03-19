from flask import Blueprint, render_template, redirect, url_for


forgot_password_blueprint = Blueprint('forgot_password', __name__)


@forgot_password_blueprint.route('/forgot_password', methods=['GET', 'POST'])
def spar():
    return render_template('forgot_password.html')