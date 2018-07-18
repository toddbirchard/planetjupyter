import requests
from flask import url_for, render_template, Markup
from config import base_url, notebookID, username, password, key
import json

headers = {
  'Access-Control-Allow-Origin': '*',
  'Plotly-Client-Platform': 'Python 3 0.3.2',
  'Authorization': key,
  'Content-Type': 'application/json'
}


'''@app.route("/notebook")
def hello():
    r = requests.get(base_url + notebookID, auth=(username, password), headers=headers)
    result = r.json()
    embed_url = result['embed_url']
    r2 = requests.get(embed_url, auth=(username, password), headers={'Content-Type': 'text/html'})
    return render_template('index.html', content=Markup(r2.text))'''
