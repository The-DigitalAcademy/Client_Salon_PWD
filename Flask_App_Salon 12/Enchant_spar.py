from flask import Blueprint, render_template, redirect, url_for


Enchant_spar_blueprint = Blueprint('Enchant_spar', __name__)


@Enchant_spar_blueprint.route('/Enchant_spar', methods=['GET', 'POST'])
def Enchant_spar():
    return render_template('Enchant_spar.html')