"""

    05b_flask_request_obj.py

"""
from flask import Flask, jsonify, request, Response


app = Flask(__name__)


@app.route('/celebrity/<last_name>', methods=['POST'])
def do_stuff(last_name):
    print(f'remote_addr: {request.remote_addr}')
    print(f'path: {request.path}')
    print(f'path param: {last_name}')
    print(f'form: {request.form}, sample: {request.form.get("first")}')
    print(f'args: {request.args}, sample: {request.args.get("category")}')
    print(f'values: {request.values}, samples: {request.values.get("middle")}, {request.values.get("birthdate")}')
    print(f'headers: {request.headers}, sample: {request.headers.get("User-Agent")}')

    return Response(jsonify({'message': 'Completed.'}).data,
                    status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
