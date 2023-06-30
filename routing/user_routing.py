# from flask import Blueprint, jsonify, request
# import controller.user_controller as user_controller
# from controller.user_controller import insert_user_service,get_users, get_user_by_email, login_service, logout_service

# user_route = Blueprint("user", __name__)

# @user_route.route('/user', methods=["GET"])
# def get_user_by_email_service():
#     users = user_controller.get_user_by_email()
#     return jsonify(users)

# @user_route.route("/signup", methods=["POST", "OPTIONS"])  # Ajout de "OPTIONS" ici
# def insert_user():
#     if request.method == "OPTIONS":
#         headers = {
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Methods': 'POST, OPTIONS',
#             'Access-Control-Allow-Headers': 'Content-Type'
#         }
#         return ('', 200, headers)
#     data = request.get_json()
#     return insert_user_service(data)

# @user_route.route("/login", methods=['POST'])
# def login():
#     if request.method == "OPTIONS":
#         headers = {
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Methods': 'POST, OPTIONS',
#             'Access-Control-Allow-Headers': 'Content-Type'
#         }
#         return ('', 200, headers)
#     data = request.get_json()
#     return login_service(data)

# @user_route.route('/logout', methods=['POST'])
# def logout():
#     return logout_service()

# @user_route.route('/users', methods=["GET"])
# def get_users():
#     users = user_controller.get_users()
#     return jsonify(users)
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
import controller.user_controller as user_controller

user_route = Blueprint("user", __name__)

@user_route.route('/user', methods=["GET"])
def get_user_by_email_service():
    users = user_controller.get_user_by_email()
    return jsonify(users)

@user_route.route("/signup", methods=["POST", "OPTIONS"])
@cross_origin()
def insert_user():
    if request.method == "OPTIONS":
        return ('', 200)
    data = request.get_json()
    return user_controller.insert_user_service(data)

@user_route.route("/login", methods=['POST', 'OPTIONS'])
@cross_origin()
def login():
    if request.method == "OPTIONS":
        return ('', 200)
    data = request.get_json()
    return user_controller.login_service(data)

@user_route.route('/logout', methods=['POST'])
def logout():
    return user_controller.logout_service()

@user_route.route('/users', methods=["GET"])
def get_users_route():
    users = user_controller.get_users()
    return jsonify(users)
