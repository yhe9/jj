from flask import Flask
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE

bootstrap = Bootstrap()
simple = SimpleMDE()

def create_app():
    app = Flask(__name__)

    # Initializing flask extensions
    bootstrap.init_app(app)
    simple.init_app(app)

    # Registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .tmdbAPI import configure_request
    configure_request()

    return app
