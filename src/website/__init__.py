from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "MEUHFAIFHAUHFIAUHUahfshdffhaushfiauFEufhui3heigerg89wehui"

    return app

