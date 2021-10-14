import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "This username has been taken."}, 400
        user = UserModel(data['username'], generate_password_hash(data['password']))
        user.save_to_db()

        return {"message": "User created successfully."}, 201
