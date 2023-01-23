
from payload import *
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')

def index():
    return "hello world"


@app.route('/productionplan', methods=['POST'])
def print_payload():
    content_json = request.json
    print(content_json["powerplants"])
    # print(content_json)
    # payload = PayLoad(content_json)
    # print(payload)



if __name__ == "__main__":
    app.run(debug=True, port=8888)