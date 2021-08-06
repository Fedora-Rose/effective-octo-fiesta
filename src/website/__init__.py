from flask import Flask
from .views import views
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "MEUHFAIFHAUHFIAUHUahfshdffhaushfiauFEufhui3heigerg89wehui"
    app.register_blueprint(views)
    return app

