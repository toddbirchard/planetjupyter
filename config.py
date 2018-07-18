import pymongo
import os
import requests
import sys

# Plotly
base_url = 'https://api.plot.ly/v2/jupyter-notebooks/toddbirchard:'
base_account_url = 'https://plot.ly/~toddbirchard/184.embed'
base_external_url = 'https://api.plot.ly/v2/jupyter-notebooks/external?source='
username = 'toddbirchard'
password = "OISDy4S6Om1voqdOYzWJ"
key = 'dG9kZGJpcmNoYXJkOk9JU0R5NFM2T20xdm9xZE9ZeldK'

# DB Creds
mongo = pymongo.MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin', maxPoolSize=50, connect=False)
db = pymongo.database.Database(mongo, 'jupyter',)
col = pymongo.collection.Collection(db, 'urls')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
