from db import db
import time


class ExerciseModel(db.Model):
    __table_name__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    sheet_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    description = db.Column(db.String(256))
    repetitions = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    series = db.Column(db.Integer)
    creation_date = db.Column(db.Integer)

    def __init__(self, sheet_id, name, description, repetitions, duration, series):
        self.id = None
        self.sheet_id = sheet_id
        self.name = name
        self.description = description
        if (repetitions or duration) and not(repetitions and duration):
            self.repetitions = repetitions
            self.duration = duration
        else:
            raise SyntaxError
        self.series = series
        self.creation_date = int(time.time())

    @classmethod
    def find_by_id(cls, id):
        return ExerciseModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_sheet_id(cls, sheet_id):
        return ExerciseModel.query.filter_by(sheet_id=sheet_id)

    @classmethod
    def find_all(cls):
        return ExerciseModel.query.filter_by()

    @classmethod
    def delete_all(cls):
        for i in ExerciseModel.query:
            i.delete_from_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def change_name(self, name):
        self.name = name

    def change_description(self, description):
        self.description = description

    def change_repetitions(self, repetitions):
        self.repetitions = repetitions

    def change_duration(self, duration):
        self.duration = duration

    def change_series(self, series):
        self.series = series