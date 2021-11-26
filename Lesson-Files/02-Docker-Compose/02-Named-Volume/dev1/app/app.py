# flask_web/app.py

from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"data": {"container" : os.getenv('HOSTNAME') , "device" : os.getenv('DEVICE'), "temp" : random.randrange(-10, 20, 1)}})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')