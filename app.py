from flask import Flask, jsonify, request
import controller.test_controller as test_controller
from db import create_tables
from flask_cors import CORS
from routing.routes import test_route
from routing.user_routing import user_route
import secrets

app = Flask(__name__)
secret_key = secrets.token_hex(16)
print(secret_key)
app.config['SECRET_KEY'] = secret_key
app.register_blueprint(test_route)
app.register_blueprint(user_route)
cors = CORS(
    app,
    supports_credentials=True,
    origins="*",
    allow_headers=['Access-Control-Allow-Origin', '*'],
)
# test
@app.route("/test", methods=["POST", "OPTIONS"])  # Ajout de "OPTIONS" ici
def insert_test():
    print('ici')
    if request.method == "OPTIONS":  # Gestion de la méthode OPTIONS
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Methods"] = "POST"
        return response
    else:
        test_details = request.get_json()
        name = test_details["name"]
        price = test_details["price"]
        rate = test_details["rate"]
        result = test_controller.insert_test(name, price, rate)
        return jsonify(result)


@app.route("/test", methods=["PUT"])
def update_test():
    test_details = request.get_json()
    id = test_details["id"]
    name = test_details["name"]
    price = test_details["price"]
    rate = test_details["rate"]
    result = test_controller.update_test(id, name, price, rate)
    return jsonify(result)


@app.route("/test/<id>", methods=["DELETE"])
def delete_test(id):
    result = test_controller.delete_test(id)
    return jsonify(result)


@app.route("/test/<id>", methods=["GET"])
def get_test_by_id(id):
    test = test_controller.get_by_id(id)
    return jsonify(test)

# user

if __name__ == "__main__":
    create_tables()
    app.run()




