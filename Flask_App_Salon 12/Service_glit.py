from flask import Blueprint, render_template, redirect, url_for


Service_glit_blueprint = Blueprint('Service_glit', __name__)


@Service_glit_blueprint.route('/Service_glit', methods=['GET', 'POST'])
def Service_glit():
    return render_template('Service_glit.html')