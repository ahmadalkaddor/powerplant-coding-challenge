
from payload import *
from flask import Flask
from flask import request


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
    print(payload.fuels)
    # print(payload)
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=8888)