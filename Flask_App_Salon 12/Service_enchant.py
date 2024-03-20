from flask import Blueprint, render_template, redirect, url_for


Service_enchant_blueprint = Blueprint('Service_enchant', __name__)


@Service_enchant_blueprint.route('/Service_enchant', methods=['GET', 'POST'])
def Service_enchant():
    return render_template('Service_enchant.html')