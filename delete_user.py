from flask import Blueprint, request, jsonify
from google.cloud import firestore

delete_user_route = Blueprint("delete_users", __name__)


@delete_user_route.route("/delete_users", methods=["POST"])
def delete_user():
    request_json = request.get_json()
    username = request_json.get("username")

    db = firestore.Client()
    user_ref = db.collection("users").document(username)

    # Check if the user exists before deletion
    if user_ref.get().exists:
        user_ref.delete()

        # Update total deleted user count document
        deleted_count_ref = db.collection("metadata").document("deleted_count")
        deleted_count = deleted_count_ref.get().to_dict()

        if deleted_count is None:
            deleted_count = {"count": 1}
            db.collection("metadata").document("deleted_count").set(deleted_count)
        else:
            # Increment the deleted user count
            deleted_count["count"] += 1
            deleted_count_ref.set(deleted_count)

        return jsonify(
            {
                "message": f'User {username} deleted from Firestore! Total deleted users: {deleted_count["count"]}'
            }
        )
    else:
        return jsonify(
            {"message": f"User {username} not found in Firestore. No user deleted."}
        )
