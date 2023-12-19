from flask import Blueprint, jsonify
from google.cloud import firestore

user_count_route = Blueprint("get_user_count", __name__)


@user_count_route.route("/users", methods=["GET"])
def get_user_count():
    db = firestore.Client()
    user_count_ref = db.collection("metadata").document("user_count")

    user_count = user_count_ref.get().to_dict()

    if user_count is not None:
        return jsonify({"user_count": user_count.get("count")})
    else:
        return jsonify({"user_count": 0})
