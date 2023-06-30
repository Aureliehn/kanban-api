from flask import Blueprint, jsonify
import controller.test_controller as test_controller

test_route = Blueprint("test", __name__)

@test_route.route('/tests', methods=["GET"])
def get_test():
    test = test_controller.get_test()
    return jsonify(test)

