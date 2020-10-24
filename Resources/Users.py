from flask_restful import Resource, request
from Models.UserModel import UserModel

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        user = UserModel(username)
        user.save_to_db()
