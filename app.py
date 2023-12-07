# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory storage for simplicity)
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description for Task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description for Task 2',
        'done': False
    }
]

# API routes

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json.get('title', ''),
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})

# Introduced Bugs
# Bug 1: Index out of range
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) + 1):
    print(numbers[i])

# Bug 2: Division by zero
numerator = 10
denominator = 0
result = numerator / denominator
print("Result:", result)

# Bug 3: NullPointerExcpetion equivalent (TypeError)
text = None
print(len(text))

@app.route('/deserialize', methods=['POST'])
def deserialize():
    serialized_data = request.form.get('data')
    
    # Intentional vulnerability: Unsafe deserialization of user input
    user_data = pickle.loads(serialized_data)
    
    return f"Deserialized data: {user_data}"
    
# Run the application if executed directly
if __name__ == '__main__':
    app.run(debug=True)
