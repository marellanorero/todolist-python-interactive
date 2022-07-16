import json
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label" : "My first task", "done": False},
    {"label" : "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    d = json.loads(request_body)
    todos.append(d)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    json_text = jsonify(todos.pop(position))
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)