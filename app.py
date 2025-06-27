from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "name": "Sparsh", "email": "sparsh@example.com"},
    {"id": 2, "name": "Riya", "email": "riya@example.com"}
]

# Home Route
@app.route('/')
def home():
    return "Flask API is running. Use /users endpoint."

# Define GET Route (All Users)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Define GET by ID Route
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# Define POST Route (Add User)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

#Define PUT Route (Update User)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        data = request.get_json()
        user['name'] = data.get('name', user['name'])
        user['email'] = data.get('email', user['email'])
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# Define DELETE Route
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'})

# Error Handling for 404
if __name__ == '__main__':
    app.run(debug=True)
