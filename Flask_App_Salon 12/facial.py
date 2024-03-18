from flask import Blueprint, render_template, redirect, url_for


facial_blueprint = Blueprint('facial', __name__)


@facial_blueprint.route('/facial', methods=['GET', 'POST'])
def facial():
    return render_template('facial.html')