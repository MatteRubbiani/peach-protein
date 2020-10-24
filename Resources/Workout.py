from flask_restful import Resource, request
from Models.WorkoutModel import WorkoutModel
from Models.UserModel import UserModel
import errors

class CreateWorkout(Resource):
    def post(self):
        data = request.get_json()
        user_id = data["user"]
        name = data["name"]
        if UserModel.find_by_id(user_id):
            workout = WorkoutModel(user_id, name)
            workout.save_to_db()
        else:
            return errors.USER_DOES_NOT_EXIST

    def get(self):
        data = request.get_json()
        user_id = data["user"]
        workouts = []
        if UserModel.find_by_id(user_id):
            for w in WorkoutModel.find_by_user_id(user_id):
                workouts.append({
                    "id": w.id,
                    "name": w.name,
                    "creation_date": w.creation_date
                })
            return workouts
        else:
            return errors.USER_DOES_NOT_EXIST