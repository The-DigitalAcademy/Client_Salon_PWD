from flask import Blueprint, render_template, redirect, url_for


Shiatsu_facial_blueprint = Blueprint('Shiatsu_facial', __name__)


@Shiatsu_facial_blueprint.route('/Shiatsu_facial', methods=['GET', 'POST'])
def Shiatsu_facial():
    return render_template('Shiatsu_facial.html')