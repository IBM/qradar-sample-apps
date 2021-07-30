from flask import Blueprint, request
from qpylib import qpylib

apibp = Blueprint('apibp', __name__, url_prefix='/')

@apibp.route('offenses')
def get_offenses():
    range = request.args.get('range')
    response = qpylib.REST('get', '/api/siem/offenses', None, headers={'Range': range})
    return {'offenses': response.json()}

@apibp.route('offenses/<id>')
def get_offense_by_id(id):
    response = qpylib.REST('get', ('/api/siem/offenses/' + id))
    return {'offense': response.json()}
