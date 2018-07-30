from flask import Flask, url_for, render_template, Markup, request, Response, redirect
from config import key, col, db, base_url, base_external_url, base_account_url, username, password, ROOT_DIR
import requests
from form import JupyterForm
from flask_assets import Bundle, Environment
from flask_static_compress import FlaskStaticCompress
import logging
import sys
from currenttime import yourtime, prettytime
from flask_cors import CORS, cross_origin
from nbconvert import HTMLExporter
from traitlets.config import Config
from nbconvert import HTMLExporter
import nbformat
import json


app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
CORS(app)
compress = FlaskStaticCompress(app)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'sdist'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
app.static_folder = 'static'

html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'


headers = {
    'Content-Type': 'application/json',
    'Vary': 'Accept',
    'Plotly-Client-Platform': 'Python 3 0.3.2'
}


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    recent_searches = list(col.find().limit(5).sort("time", -1))
    print('recent_searches = ', recent_searches)
    sys.stdout.flush()
    return render_template('/index.html', form=JupyterForm(), recents=recent_searches, template="home-template")


@app.route("/notebookUpload")
def notebookUpload():
    """Return internal notebook."""
    app.static_folder = ROOT_DIR + '/static'
    if request.method == 'POST':
        headers = {
          'Access-Control-Allow-Origin': '*',
          'Plotly-Client-Platform': 'Python 3 0.3.2',
          'Content-Type': 'application/json',
          'Vary': 'Accept'
        }
        #url = request.form['PlotlyURL']
        githubsource = url.replace("https://raw.githubusercontent.com/", "https://github.com/")
        repo_url = githubsource.rsplit('/', 2)[0]
        #r = requests.get('https://api.plot.ly/v2/jupyter-notebooks/upload', auth=(username, password), headers=headers)
        plotlyurl = r.json()['web_url']
    #r = requests.get(base_account_url + notebookID, auth=(username, password), headers=headers)
    return redirect(plotlyurl, code=302)


@app.route("/notebook", methods=['POST', 'GET', 'OPTIONS'])
def notebook():
    """Return internal notebook."""
    app.static_folder = 'static'
    if request.method == 'POST':
        url = request.form['PlotlyURL']
        githubsource = url.replace("https://raw.githubusercontent.com/", "https://github.com/")
        repo_url = githubsource.rsplit('/', 2)[0]
        r = requests.get(base_external_url + url, headers=headers, auth=(username, password))
        response = r.json()['html']
        # Testing this
        #notebook = nbformat.read(url, as_version=4)
        #(body, resources) = html_exporter.from_notebook_node(notebook)
        #print(body[:400] + '...')
        # --------
        #print("r.json() = ", response)
        #print("response = ", response)
        #sys.stdout.flush()
        extract = Markup(response).strip()
        document = {'url': request.form['PlotlyURL'],
                    'time': yourtime,
                    'displaytime': prettytime,
                    'githuburl': repo_url
                    }
        result = col.replace_one({'url': document['url']}, document, upsert=True)
        return render_template('/notebook.html', content=extract, template="notebook-template")


@app.route("/example")
def example():
    """Return external notebook."""
    app.static_folder = 'static'
    r = requests.get(base_external_url + 'https://raw.githubusercontent.com/mattalhonte/sfi-challenge/master/ComplexityChallengeWriteup.ipynb', headers={'Content-Type': 'application/json', 'Plotly-Client-Platform': 'Lisp'})
    extract = Markup(r.json()['html'].strip())
    return render_template('/notebook.html', content=extract, template="notebook-template")
