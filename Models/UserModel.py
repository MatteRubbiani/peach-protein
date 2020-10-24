from db import db
import time


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    creation_date = db.Column(db.Integer)

    def __init__(self, username):
        self.id = None
        self.username = username
        self.creation_date = int(time.time())

    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    @classmethod
    def find_all(self):
        return UserModel.query.filter_by()

    # def send_confirmation_email(self):
    #     link = "aaaaa"
    #     subject = "Registration Confirmation"
    #     text = "please confirm you mail"
    #     html = None
    #     return None
    #     return Mailgun.send_email(self.mail, subject, text, html)

    @classmethod
    def delete_all(cls):
        for i in UserModel.query:
            i.delete_from_db()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_username(self, username):
        self.username = username
