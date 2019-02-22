from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

r = FlaskRedis()
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder="templates",
                static_folder="static"
                )
    app.config.from_object('config.Config')

    with app.app_context():
        # Set Global Session Variables
        r.init_app(app, charset="utf-8", decode_responses=True)
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])


        # Initialize Global DB
        db.init_app(app)

        # Import Blueprints
        from . import currenttime
        from . import form
        from . import routes

        return app
