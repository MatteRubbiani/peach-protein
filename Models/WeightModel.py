import operator
from db import db
from Models.SheetModel import SheetModel
from Models.ExerciseModel import ExerciseModel
import time


class WeightModel(db.Model):
    __table_name__ = "weights"

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    unit = db.Column(db.String(10))
    date = db.Column(db.Integer)

    def __init__(self, exercise_id, weight, unit):
        self.id = None
        self.exercise_id = exercise_id
        self.weight = weight
        self.unit = unit
        self.date = int(time.time())

    @classmethod
    def find_by_id(cls, id):
        return WeightModel.query.filter_by(id=id).first()

    @classmethod
    def find_lasts_by_sheet_id(cls, sheet_id):
        exercises = [i for i in ExerciseModel.find_by_sheet_id(sheet_id)]
        weights = []
        for ex in exercises:
            weights += [i for i in WeightModel.find_by_exercise_id(ex.id)]
        weights = reversed(sorted(weights, key=operator.attrgetter("date")))
        exercise_ids_used = []
        lasts = []
        for w in weights:
            if not w.exercise_id in exercise_ids_used:
                lasts.append(w)
                exercise_ids_used.append(w.exercise_id)
        return lasts

    @classmethod
    def find_by_workout_id(cls, workout_id):
        sheets = [i for i in SheetModel.find_by_workout_id(workout_id)]
        exercises = []
        for sheet in sheets:
            exercises+=[i for i in ExerciseModel.find_by_sheet_id(sheet.id)]
        weights = []
        for ex in exercises:
            weights += [i for i in WeightModel.find_by_exercise_id(ex.id)]
        return weights

    @classmethod
    def find_by_exercise_id(cls, exercise_id):
        return WeightModel.query.filter_by(exercise_id=exercise_id)

    @classmethod
    def find_all(cls):
        return WeightModel.query.filter_by()

    @classmethod
    def delete_all(cls):
        for i in WeightModel.query:
            i.delete_from_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()