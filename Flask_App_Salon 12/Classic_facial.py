from flask import Blueprint, render_template, redirect, url_for


Classic_facial_blueprint = Blueprint('Classic_facial', __name__)


@Classic_facial_blueprint.route('/Classic_facial', methods=['GET', 'POST'])
def Classic_facial():
    return render_template('Classic_facial.html')