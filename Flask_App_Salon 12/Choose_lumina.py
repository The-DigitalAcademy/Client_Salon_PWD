from flask import Blueprint, render_template, redirect, url_for


Choose_lumina_blueprint = Blueprint('Choose_lumina', __name__)


@Choose_lumina_blueprint.route('/Choose_lumina', methods=['GET', 'POST'])
def Choose_lumina():
    return render_template('Choose_lumina.html')