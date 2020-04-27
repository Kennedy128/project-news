from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from .requests import configure_requests

bootstap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])
    configure_requests(app)

    #Initializing flask extensions
    bootstap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app