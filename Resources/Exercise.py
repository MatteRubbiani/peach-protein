from flask_restful import Resource, request
from Models.SheetModel import SheetModel
from Models.ExerciseModel import ExerciseModel
import errors

class SetExercise(Resource):
    def post(self): #Create exercise if sheet_id is passed or change an existing one if exercise_id is passed
        data = request.get_json()

        name = data["name"]
        description = data["description"]

        try:
            repetitions = data["repetitions"]
        except:
            try:
                duration = data["duration"]
            except:
                return errors.SINTAX_ERROR

        series = data["series"]
        try:
            id = data["exercise"]
            exercise = ExerciseModel.find_by_id(id)
            if exercise:
                exercise.change_name(name)
                exercise.change_description(description)
                try:
                    exercise.change_duration(duration)
                except:
                    exercise.change_repetitions(repetitions)
                exercise.change_series(series)
                exercise.save_to_db()
            else:
                return errors.EXERCISE_DOES_NOT_EXIST
        except:
            try:
                sheet_id = data["sheet"]
                if SheetModel.find_by_id(sheet_id):
                    try:
                        exercise = ExerciseModel(sheet_id, name, description, repetitions, None, series)
                    except:
                        exercise = ExerciseModel(sheet_id, name, description, None, duration, series)
                    exercise.save_to_db()
                else:
                    return errors.SHEET_DOES_NOT_EXIST
            except:
                return errors.SINTAX_ERROR


    def get(self): #Get all exercises of a sheet
        data = request.get_json()
        sheet_id = data["sheet"]

        if SheetModel.find_by_id(sheet_id):
            exercises = []
            for e in ExerciseModel.find_by_sheet_id(sheet_id):
                exercises.append({
                    "id": e.id,
                    "name": e.name,
                    "description": e.description,
                    "repetitions": e.repetitions,
                    "duration": e.duration,
                    "series": e.series,
                    "creation_data": e.creation_date
                })
            return exercises
        else:
            return errors.SHEET_DOES_NOT_EXIST