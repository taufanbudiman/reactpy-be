from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app.users import bp


@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    additional_claims = {}
    access_token = create_access_token(username,
                                       additional_claims=additional_claims)
    return jsonify(access_token=access_token)
