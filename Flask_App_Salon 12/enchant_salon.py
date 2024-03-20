from flask import Blueprint, render_template, redirect, url_for


enchant_salon_blueprint = Blueprint('enchant_salon', __name__)


@enchant_salon_blueprint.route('/enchant_salon', methods=['GET', 'POST'])
def enchant_salon():
    return render_template('enchant_salon.html')