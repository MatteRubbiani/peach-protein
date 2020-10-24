from db import db
import time

class WorkoutModel(db.Model):
    __table_name__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    creation_date = db.Column(db.Integer)

    def __int__(self, user_id, name):
        self.id = None
        self.user_id = user_id
        self.name = name
        self.creation_date = int(time.time())

    @classmethod
    def find_by_id(cls, id):
        return WorkoutModel.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return WorkoutModel.query.filter_by()

    @classmethod
    def delete_all(cls):
        for i in WorkoutModel.query:
            i.delete_from_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def change_name(self, name):
        self.name = name