import pymongo
import os
import requests
import sys

# Plotly
base_url = 'https://api.plot.ly/v2/jupyter-notebooks/toddbirchard:'
base_account_url = 'https://plot.ly/~toddbirchard/184.embed'
base_external_url = 'https://api.plot.ly/v2/jupyter-notebooks/external?source='
upload_url = "https://api.plot.ly/v2/jupyter-notebooks/upload"

username = 'toddbirchard'
password = "Zoy3YIvNpI7m9eTDluko"
key = 'dG9kZGJpcmNoYXJkOlpveTNZSXZOcEk3bTllVERsdWtv'


# DB Creds
mongo = pymongo.MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin', maxPoolSize=50, connect=False)
db = pymongo.database.Database(mongo, 'jupyter',)
col = pymongo.collection.Collection(db, 'urls')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
