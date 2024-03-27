from flask import Blueprint, render_template, redirect, url_for


choose_nails2_blueprint = Blueprint('choose_nails2', __name__)


@choose_nails2_blueprint.route('/choose_nails2', methods=['GET', 'POST'])
def choose_nails2():
    return render_template('choose_nails2.html')