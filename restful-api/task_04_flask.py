#!/usr/bin/python3
"""Module for Flask"""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Return welcome message"""
    return "Welcome to the Flask API"

@app.route("/data")
def data():
    """Returns a JSON response using jsonify"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Returns the status of the server"""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Get specified user data"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(users[username])

@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.get_json()
    if new_user is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = new_user.get("username")
    if username is None:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = {
        "username": username,
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
