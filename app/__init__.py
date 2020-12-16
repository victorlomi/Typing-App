from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
