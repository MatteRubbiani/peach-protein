from flask_restful import Resource, request
from Models.UserModel import UserModel
from Models.WorkoutModel import WorkoutModel
from Models.SheetModel import SheetModel
import errors

class SetSheet(Resource):
    def post(self): #Create sheet if workout_id is passed or change an existing one if sheet_id is passed
        data = request.get_json()

        name = data["name"]
        duration = data["duration"]

        try:
            id = data["sheet"]
            sheet = SheetModel.find_by_id(id)
            if sheet:
                sheet.change_name(name)
                sheet.change_duration(duration)
                sheet.save_to_db()
            else:
                return errors.SHEET_DOES_NOT_EXIST
        except:
            try:
                workout_id = data["workout"]
                if WorkoutModel.find_by_id(workout_id):
                    sheet = SheetModel(workout_id, name, duration)
                    sheet.save_to_db()
                else:
                    return errors.WORKOUT_DOES_NOT_EXIST
            except:
                return errors.SINTAX_ERROR

    def get(self): #Get all sheets of a workout
        data = request.get_json()
        workout_id = data["workout"]
        if WorkoutModel.find_by_id(workout_id):
            sheets = []
            for s in SheetModel.find_by_workout_id(workout_id):
                sheets.append({
                    "id": s.id,
                    "name": s.name,
                    "duration": s.duration,
                    "last_performed": s.last_performed,
                    "creation_date": s.creation_date
                })
            return sheets
        else:
            return errors.WORKOUT_DOES_NOT_EXIST

    def put(self): #Perform sheet (update last_performed date)
        data = request.get_json()
        id = data["sheet"]
        sheet = SheetModel.find_by_id(id)
        if sheet:
            sheet.perform()
            sheet.save_to_db()
        else:
            return errors.SHEET_DOES_NOT_EXIST

    def delete(self):
        data = request.get_json()
        sheet_id = data["sheet"]
        security_token = data["security_token"]
        sheet = SheetModel.find_by_id(sheet_id)
        workout = WorkoutModel.find_by_id(sheet.workout_id)
        user = UserModel.find_by_id(workout.user_id)
        if sheet:
            if user.security_token == security_token:
                sheet.delete_from_db()
            else:
                return errors.SECURITY_TOKEN_NOT_VALID
        else:
            return errors.SHEET_DOES_NOT_EXIST

