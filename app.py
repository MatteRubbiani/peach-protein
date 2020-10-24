import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
from Resources.Users import *
from Resources.Workout import *



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
api.add_resource(Register, "/user/register")
api.add_resource(GetUsername, "/user")
api.add_resource(ChangeUsername, "/user/change-username")

api.add_resource(CreateWorkout, "/workout")

# ============ ### ============= #

if __name__ == "__main__":
    from db import db


    @app.before_first_request
    def create_table():
        db.create_all()


    db.init_app(app)
    app.run(port=60000, debug=True)
