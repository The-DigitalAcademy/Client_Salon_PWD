from flask import Blueprint, render_template, redirect, url_for


Services_sharon_blueprint = Blueprint('Services_sharon', __name__)


@Services_sharon_blueprint.route('/Services_sharon', methods=['GET', 'POST'])
def Services_sharon():
    return render_template('Services_sharon.html')