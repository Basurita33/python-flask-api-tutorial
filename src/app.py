from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/myroute', methods=['GET'])
def hello_world():
  return 'Hello World!'

# GET /todos
@app.route('/todos', methods=['GET'])
def todos():
	json_text = jsonify(todos)
	return json_text

# POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.get_json(force=True)
  print("Add new task:", request_body)
  todos.append(request_body)
  return todos

#DELETE /todos
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
     print("This is the position to delete:", position)
     if 0 <= position < len(todos):
          todos.pop(position)
     return jsonify(todos)

#global variable
todos = [
	{ "label": "Clean bathroom", "done": False },
	{ "label": "Cook dinner", "done": False }
]

#this lines should be at the end of the file
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3245, debug=True)