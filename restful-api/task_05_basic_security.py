#!/usr/bin/python3
"""Module for Basic Security with APIs"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-secret-key"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@jwt.unauthorized_loader
def handle_unauthorized_loader(err):
    """Handler for missing or invalid tokens"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handler for invalid tokens"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handler for expired tokens"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handler for revoked tokens"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handler for when fresh token is required"""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route with basic protection"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=['POST'])
def login():
    """Login method that accepts JSON payload with username and password
    returns a JWT token on success"""
    login_info = request.get_json()

    if login_info is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = login_info.get("username")
    password = login_info.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route with JWT authentication"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route only for admins checked by JWT"""
    username = get_jwt_identity()
    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
