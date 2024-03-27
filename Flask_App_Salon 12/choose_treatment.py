from flask import Blueprint, render_template, redirect, url_for


choose_treatment_blueprint = Blueprint('choose_treatment', __name__)


@choose_treatment_blueprint.route('/choose_treatment', methods=['GET', 'POST'])
def choose_treatment():
    return render_template('choose_treatment.html')