from flask import Blueprint, render_template, redirect, url_for


service_serene_blueprint = Blueprint('spar', __name__)


@service_serene_blueprint.route('/service_serene', methods=['GET', 'POST'])
def service_serene():
    return render_template('service_serene.html')