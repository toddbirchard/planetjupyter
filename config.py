from os import environ


class Config:
    """Configuration class for all FLask settings."""

    # General
    TESTING = environ.get("TESTING")
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SESSION_TYPE = environ.get("SESSION_TYPE")
    REDIS_URI = environ.get("REDIS_URI")

    # Plotly
    base_url = 'https://api.plot.ly/v2/jupyter-notebooks/toddbirchard:'
    base_account_url = 'https://plot.ly/~toddbirchard/184.embed'
    base_external_url = 'https://api.plot.ly/v2/jupyter-notebooks/external?source='
    upload_url = "https://api.plot.ly/v2/jupyter-notebooks/upload"

    # DB Creds
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
