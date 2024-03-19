from flask import Blueprint, render_template, redirect, url_for


Belle_salon_blueprint = Blueprint('Belle_salon', __name__)


@Belle_salon_blueprint.route('/Belle_salon', methods=['GET', 'POST'])
def Belle_salon():
    return render_template('Belle_salon.html')
