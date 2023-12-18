from flask import Blueprint

# app = Flask(__name__)

welcome_route = Blueprint("welcome", __name__)


@welcome_route.route("/welcome")
def home():
    return "HI, from first flask app"


# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
