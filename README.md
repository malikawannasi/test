# RPN Calculator API

## Endpoints

### List All Operations

- **GET** `/rpn/op`

Returns a list of supported operations (`+`, `-`, `*`, `/`).

### Create a New Stack

- **POST** `/rpn/stack`

Creates a new stack and returns its ID.

### List Available Stacks

- **GET** `/rpn/stack`

Returns a list of all stack IDs.

### Delete a Stack

- **DELETE** `/rpn/stack/<stack_id>`

Deletes the stack with the given ID.

### Push a Value to a Stack

- **POST** `/rpn/stack/<stack_id>`

Pushes a new value to the stack with the given ID. The value should be provided in the request body as JSON (`{"value": <number>}`).

### Get a Stack

- **GET** `/rpn/stack/<stack_id>`

Returns the current contents of the stack with the given ID.

### Apply an Operation to a Stack

- **POST** `/rpn/op/<op>/stack/<stack_id>`

Applies the operation `<op>` to the stack with the given ID. The operation must be one of `+`, `-`, `*`, or `/`. Returns the updated stack.

## Running the API

1. Install dependencies:
pip install -r requirements.txt

2. Run the Flask application:
python app.py

3. Access the API at `http://localhost:5000`.