from flask import Blueprint, render_template, request, redirect
from .ref_data import delete_reference_data, get_reference_data_value, update_reference_data_value

# pylint: disable=invalid-name
viewsbp = Blueprint('views', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    return render_template('index.html', value=get_reference_data_value())


@viewsbp.route('/set_reference_data', methods=['POST'])
def set_reference_data():
    value = request.form['value']
    update_reference_data_value(value)
    return redirect('/', code=303)


@viewsbp.route('/uninstall_delete_reference_data', methods=['POST'])
def uninstall_delete_reference_data():
    delete_reference_data()
    return "OK!", 200
