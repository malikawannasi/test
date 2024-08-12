
from flask import Flask, request, jsonify, abort, send_from_directory, Response
import uuid
import os

app = Flask(__name__)

# Stockage des piles par ID
stacks = {}

# Liste des opérations disponibles
OPERATIONS = ['+', '-', '*', '/']

@app.route('/rpn/op', methods=['GET'])
def list_operations():
    return jsonify(OPERATIONS)

@app.route('/rpn/stack', methods=['POST'])
def create_stack():
    stack_id = str(uuid.uuid4())
    stacks[stack_id] = []
    return jsonify({'stack_id': stack_id}), 201

@app.route('/rpn/stack', methods=['GET'])
def list_stacks():
    return jsonify({'stacks': list(stacks.keys())})

@app.route('/rpn/stack/<stack_id>', methods=['DELETE'])
def delete_stack(stack_id):
    if stack_id in stacks:
        del stacks[stack_id]
        return '', 204
    else:
        abort(404, description="Stack not found")

@app.route('/rpn/stack/<stack_id>', methods=['POST'])
def push_value(stack_id):
    if stack_id not in stacks:
        abort(404, description="Stack not found")

    data = request.json
    if 'value' not in data:
        abort(400, description="Value required")

    stacks[stack_id].append(data['value'])
    return jsonify(stacks[stack_id])

@app.route('/rpn/stack/<stack_id>', methods=['GET'])
def get_stack(stack_id):
    if stack_id not in stacks:
        abort(404, description="Stack not found")

    return jsonify(stacks[stack_id])

@app.route('/rpn/op/<op>/stack/<stack_id>', methods=['POST'])
def apply_operation(op, stack_id):
    if stack_id not in stacks:
        abort(404, description="Stack not found")
    
    if op not in OPERATIONS:
        abort(400, description="Invalid operation")
    
    if len(stacks[stack_id]) < 2:
        abort(400, description="Not enough elements in stack")

    b = stacks[stack_id].pop()
    a = stacks[stack_id].pop()

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            abort(400, description="Division by zero")
        result = a / b

    stacks[stack_id].append(result)
    return jsonify(stacks[stack_id])

# Chemin vers le répertoire des fichiers statiques
STATIC_FOLDER = 'static'

@app.route('/', methods=['GET'])
def home():
    try:
        # Lire le contenu du fichier openapi.yaml
        file_path = os.path.join(STATIC_FOLDER, 'openapi.yaml')
        with open(file_path, 'r') as file:
            content = file.read()
        # Retourner le contenu du fichier comme réponse
        return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        abort(404, description="File not found")

if __name__ == '__main__':
    app.run(debug=True)
