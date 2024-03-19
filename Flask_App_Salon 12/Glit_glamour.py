from flask import Blueprint, render_template, redirect, url_for


Glit_glamour_blueprint = Blueprint('Glit_glamour', __name__)


@Glit_glamour_blueprint.route('/Glit_glamour', methods=['GET', 'POST'])
def Glit_glamour():
    return render_template('Glit_glamour.html')