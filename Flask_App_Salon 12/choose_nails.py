from flask import Blueprint, render_template, redirect, url_for


choose_nails_blueprint = Blueprint('choose_nails', __name__)


@choose_nails_blueprint.route('/choose_nails', methods=['GET', 'POST'])
def choose_nails():
    return render_template('choose_nails.html')