from flask import Blueprint, render_template, redirect, url_for


spar_blueprint = Blueprint('spar', __name__)


@spar_blueprint.route('/spar', methods=['GET', 'POST'])
def spar():
    return render_template('spar.html')