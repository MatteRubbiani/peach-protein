import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
from Resources.Users import *
from Resources.Workout import *
from Resources.Sheet import *
from Resources.Exercise import *
from Resources.Weight import *




# ============ app configs ============= #

app = Flask(__name__)

load_dotenv(".env", verbose=True)
# app.config.from_object("default_config")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = "super"
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['CORS_HEADERS'] = '*'

jwt = JWTManager(app)
cors = CORS(app)
api = Api(app)

# ============ resources ============= #
api.add_resource(SetUser, "/user")

api.add_resource(SetWorkout, "/workout")

api.add_resource(SetSheet, "/sheet")

api.add_resource(SetExercise, "/exercise")

api.add_resource(SetWeight, "/weight")
api.add_resource(GetAllWeightsByWorkout, "/weight/workout")

# ============ ### ============= #

if __name__ == "__main__":
    from db import db


    @app.before_first_request
    def create_table():
        db.create_all()


    db.init_app(app)
    app.run(port=60000, debug=True)
