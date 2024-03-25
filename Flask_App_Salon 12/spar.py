from flask import Blueprint, render_template, redirect, url_for


spar1_blueprint = Blueprint('spar1', __name__)


@spar1_blueprint.route('/spar', methods=['GET', 'POST'])
def spar():
    return render_template('spar.html')