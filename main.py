from flask import Flask

# from welcome import welcome_route
from add_user import add_user_route
from delete_user import delete_user_route

app = Flask(__name__)

# Register routes
# app.register_blueprint(welcome_route)
app.register_blueprint(add_user_route)
app.register_blueprint(delete_user_route)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
