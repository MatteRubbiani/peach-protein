from flask_restful import Resource, request
from Models.SheetModel import SheetModel
from Models.ExerciseModel import ExerciseModel
from Models.WeightModel import WeightModel
import errors

class SetWeight(Resource):
    def post(self): #Create weight
        data = request.get_json()
        exercise_id = data["exercise"]
        weight = data["weight"]
        unit = data["unit"]
        if ExerciseModel.find_by_id(exercise_id):
            weight = WeightModel(exercise_id, weight, unit)
            weight.save_to_db()
        else:
            return errors.EXERCISE_DOES_NOT_EXIST

    def get(self): #Get all last weights for a sheet
        data = request.get_json()
        sheet_id = data["sheet"]
        if SheetModel.find_by_id(sheet_id):
            weights = []
            for w in WeightModel.find_lasts_by_sheet_id(sheet_id):
                weights.append({
                    "id": w.id,
                    "exercise_id": w.exercise_id,
                    "weight": w.weight,
                    "unit": w.unit,
                    "date": w.date
                })
            return weights
        else:
            return errors.SHEET_DOES_NOT_EXIST

class GetAllWeightsByWorkout(Resource):
    def get(self):
        data = request.get_json()
        workout_id = data["workout"]
        weights = []
        for w in WeightModel.find_by_workout_id(workout_id):
            weights.append({
                "id": w.id,
                "exercise_id": w.exercise_id,
                "weight": w.weight,
                "unit": w.unit,
                "date": w.date
            })
        return weights
