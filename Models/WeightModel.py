from db import db
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