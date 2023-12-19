from flask import Blueprint, jsonify
from google.cloud import firestore

deleted_user_count_route = Blueprint("deleted_user_count", __name__)


@deleted_user_count_route.route("/deleted_users", methods=["GET"])
def get_deleted_user_count():
    db = firestore.Client()
    deleted_count_ref = db.collection("metadata").document("deleted_count")

    deleted_count = deleted_count_ref.get().to_dict()

    if deleted_count is not None:
        return jsonify({"deleted_user_count": deleted_count.get("count")})
    else:
        return jsonify({"deleted_user_count": 0})
