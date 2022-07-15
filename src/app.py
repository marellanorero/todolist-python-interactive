import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    print("Incoming request with the following body", decoded_object)
    return jsonify(..., decoded_object)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)