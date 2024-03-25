from flask import Blueprint, render_template, redirect, url_for


Service_serene_blueprint = Blueprint('Service_serene', __name__)


@Service_serene_blueprint.route('/Service_serene', methods=['GET', 'POST'])
def Service_serene():
    return render_template('Service_serene.html')