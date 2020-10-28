from flask_restful import Resource, request
from Models.WorkoutModel import WorkoutModel
from Models.UserModel import UserModel
import errors

class SetWorkout(Resource):
    def post(self): #Create workout if user_id is passed or change an existing one if workout_id is passed
        data = request.get_json()

        name = data["name"]

        try:
            id = data["workout"]
            workout = WorkoutModel.find_by_id(id)
            if workout:
                workout.change_name(name)
                workout.save_to_db()
            else:
                return errors.WORKOUT_DOES_NOT_EXIST
        except:
            try:
                user_id = data["user"]
                if UserModel.find_by_id(user_id):
                    workout = WorkoutModel(user_id, name)
                    workout.save_to_db()
                else:
                    return errors.USER_DOES_NOT_EXIST
            except:
                return errors.SINTAX_ERROR

    def get(self): #Get all workouts of a user
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

    def delete(self):
        data = request.get_json()
        workout_id = data["workout"]
        security_token = data["security_token"]
        workout = WorkoutModel.find_by_id(workout_id)
        user = UserModel.find_by_id(workout.user_id)
        if workout:
            if user.security_token == security_token:
                workout.delete_from_db()
            else:
                return errors.SECURITY_TOKEN_NOT_VALID
        else:
            return errors.WORKOUT_DOES_NOT_EXIST


