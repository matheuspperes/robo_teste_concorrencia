from flask import Blueprint, request
from robo import Controller

teste = Blueprint('teste', __name__, url_prefix='/')

@teste.route('/start', methods=['GET', 'POST'])
def start_teste():
    return Controller().start(request)
