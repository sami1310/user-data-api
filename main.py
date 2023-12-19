from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

# from welcome import welcome_route
from add_user import add_user_route
from delete_user import delete_user_route
from get_user_count import user_count_route
from deleted_user_count import deleted_user_count_route

app = Flask(__name__)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "User data API"}
)

# Register routes
# app.register_blueprint(welcome_route)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(add_user_route)
app.register_blueprint(delete_user_route)
app.register_blueprint(user_count_route)
app.register_blueprint(deleted_user_count_route)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
