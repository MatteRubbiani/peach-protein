from flask_restful import Resource, request
from Models.UserModel import UserModel
import errors

class SetUser(Resource):
    def post(self): #Create user if user_id is not passed or change an existing one if user_id is passed
        data = request.get_json()
        username = data["username"]
        try:
            id = data["user"]
            user = UserModel.find_by_id(id)
            if user:
                user.change_username(username)
                user.save_to_db()
            else:
                return errors.USER_DOES_NOT_EXIST
        except:
            user = UserModel(username)
            user.save_to_db()
        return user.security_token

    def get(self): #Get username
        data = request.get_json()
        id = data['user']
        user = UserModel.find_by_id(id)
        if user:
            return user.username
        else:
            return errors.USER_DOES_NOT_EXIST