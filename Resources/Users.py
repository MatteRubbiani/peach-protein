from flask_restful import Resource, request
from Models.UserModel import UserModel
import errors

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        user = UserModel(username)
        user.save_to_db()

class GetUsername(Resource):
    def get(self):
        data = request.get_json()
        id = data['user']
        user = UserModel.find_by_id(id)
        if user:
            return user.username
        else:
            return errors.USER_DOES_NOT_EXIST

class ChangeUsername(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        id = data["user"]
        user = UserModel.find_by_id(id)
        if user:
            user.change_username(username)
            user.save_to_db()
        else:
            errors.USER_DOES_NOT_EXIST
