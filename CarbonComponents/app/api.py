import time
from flask import Blueprint
from qpylib import qpylib

apibp = Blueprint('apibp', __name__, url_prefix='/')

@apibp.route('/time')
def get_current_time():
    return {'time': time.time()}

@apibp.route('/offenses')
def get_all_offenses():
    response = qpylib.REST('get', '/api/siem/offenses')
    return {'offenses': response.json()}
