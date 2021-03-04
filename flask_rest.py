import json
import bson
import datetime
from bson.objectid import ObjectId
import base64

from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

class JSONEncoder(json.JSONEncoder):
    """ extend json-encoder class"""

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

def set_json_encoder(app):
    app.json_encoder = JSONEncoder
    return None

def set_cors_headers(app):
    app.config.CORS_HEADERS = 'Content-Type'
    return None

def set_strict_slashes(app):
    app.url_map.strict_slashes = False
    return None

set_json_encoder(app)
set_cors_headers(app)
set_strict_slashes(app)


@app.route('/post', methods=['Post'])
def webhook():
    # obj = request.get_json()
    file = request.files['file']
    rv = base64.b64encode(str.encode(file))  # bytes
    rv = rv.decode('ascii')  # str
    return rv

    # json_request = request.get_json()
    # return json.dumps(json_request), 200, {'Content-Type': 'application/json'}


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Hello, User. Server is working successfully!'


if __name__ == '__main__':
    app.run(port=5000,
    host="127.0.0.1",
    debug=True,
    use_reloader=True)


    # exp://192.168.1.151:19000



