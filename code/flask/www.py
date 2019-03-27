# export FLASK_APP=www.py
#
#   flask --help
#   flask run --help
#
# The WEB server listens to the port 5000, on the local interface only:
#
#   - python -m flask run
#
# The WEB server listens to the port 80, on all available network interfaces:
#
#   - python -m flask run --host="0.0.0.0" --port=80
#
# Testing:
#
#   - wget http://localhost:5000

from flask import Flask, request
import pickle
import datetime
from uuid import uuid4
import hashlib

app = Flask(__name__)

def get_uid() -> str:
    return hashlib.sha256(uuid4().bytes).hexdigest()[0:6]

def request_to_str() -> str:
    text = [f"Method: {request.method}\n", "Header:\n"]
    # noinspection PyUnusedLocal
    name: str
    # noinspection PyUnusedLocal
    value: str
    for name, value in request.headers.items():
        text.append(f"\t - {name}: {value}")
    text.append("\nBody:\n")
    text.append(request.data.decode())
    return "\n".join(text)

@app.route('/', methods=['POST', 'GET'])
def index():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    uid = get_uid()
    with open(f'request.{timestamp}-{uid}.info', 'w') as fd:
        fd.write(request_to_str())
    with open(f'request.{timestamp}-{uid}.bin', 'wb') as fd:
        pickle.dump(request, fd)
    return 'Hello, World!'

