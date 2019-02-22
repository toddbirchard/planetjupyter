import os


class Config:

    # General
    TESTING = os.environ["TESTING"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]
    SESSION_TYPE = os.environ["SESSION_TYPE"]
    REDIS_URL = os.environ["REDIS_URI"]

    # Plotly
    base_url = 'https://api.plot.ly/v2/jupyter-notebooks/toddbirchard:'
    base_account_url = 'https://plot.ly/~toddbirchard/184.embed'
    base_external_url = 'https://api.plot.ly/v2/jupyter-notebooks/external?source='
    upload_url = "https://api.plot.ly/v2/jupyter-notebooks/upload"

    # DB Creds
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URI')
