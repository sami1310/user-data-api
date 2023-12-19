from flask import Blueprint, request, jsonify
from google.cloud import firestore

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

add_user_route = Blueprint("add_users", __name__)

# Initialize Firestore
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()


@add_user_route.route("/add_users", methods=["POST"])
def add_user():
    request_json = request.get_json()
    username = request_json.get("username")
    email = request_json.get("email")

    db = firestore.Client()
    user_ref = db.collection("users").document(username)
    user_ref.set({"username": username, "email": email})

    # Update total user count document
    user_count_ref = db.collection("metadata").document("user_count")

    # Check if metadata collection exists, create if not
    user_count = user_count_ref.get().to_dict()
    if user_count is None:
        user_count = {"count": 1}
        db.collection("metadata").document("user_count").set(user_count)
    else:
        # Increment the user count
        user_count["count"] += 1
        user_count_ref.set(user_count)

    return jsonify(
        {
            "message": f"User {username} added to Firestore!"
            f"User {username} added to Firestore! Total users: {user_count["count"]}"
        }
    )


# Total users: {user_count["count"]}


# Flask route to add a user to Firestore and update total count
# @add_user_route.route("/users", methods=["POST"])
# def add_user():
#     try:
#         data = request.get_json()
#         username = data.get("username")
#         email = data.get("email")

#         # adding users to firestore
#         user_ref = db.collection("users").document(username)
#         user_ref.set({"email": email})

#         # Update total user count
#         update_user_count()

#         return jsonify({"message": "User added successfully"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # Function to update total user count in Firestore
# def update_user_count():
#     try:
#         db.collection("stats").document("user_counts").set({}, merge=True)

#         # Get current total users count
#         stats_ref = db.collection("stats").document("user_counts")
#         stats = stats_ref.get().to_dict()
#         total_added = stats.get("total_added", 0)

#         # Increment total users count
#         total_added += 1

#         # Update Firestore record with the new count
#         stats_ref.set({"total_added": total_added})

#     except Exception as e:
#         print(f"Error updating user count: {str(e)}")
