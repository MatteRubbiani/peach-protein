from db import db
import time


class SheetModel(db.Model):
    __table_name__ = "sheets"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    last_performed = db.Column(db.Integer)
    creation_date = db.Column(db.Integer)

    def __int__(self, workout_id, name, duration):
        self.id = None
        self.workout_id = workout_id
        self.name = name
        self.duration = duration
        self.last_performed = 0
        self.creation_date = int(time.time())

    @classmethod
    def find_by_id(cls, id):
        return SheetModel.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return SheetModel.query.filter_by()

    @classmethod
    def delete_all(cls):
        for i in SheetModel.query:
            i.delete_from_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def change_name(self, name):
        self.name = name

    def change_duration(self, duration):
        self.duration = duration

    def perform(self):
        self.last_performed = int(time.time())