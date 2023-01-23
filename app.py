
from payload import *
from payload_processor import *
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/')

def index():
    return "hello world"


@app.route('/productionplan', methods=['POST'])
def print_payload():
    content_json = request.get_json()
    # print(content_json["load"])
    # print(content_json)
    payload = PayLoad(content_json)
    # response = generate_response(payload=payload)
    # print(payload
    response = process_payload(payload)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=8888)