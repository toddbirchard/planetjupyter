from flask import Flask, url_for, render_template, Markup, request, Response, redirect, flash
from config import key, col, db, base_url, base_external_url, base_account_url, username, password, ROOT_DIR
import requests
from form import JupyterForm
# from flask_assets import Bundle, Environment
from flask_static_compress import FlaskStaticCompress
import logging
import sys
from currenttime import yourtime, prettytime
# from flask_cors import CORS, cross_origin
# from nbconvert import HTMLExporter
import json


app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
# CORS(app)
compress = FlaskStaticCompress(app)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'sdist'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
app.static_folder = 'static'

# html_exporter = HTMLExporter()
# html_exporter.template_file = 'basic'


headers = {
    'Content-Type': 'application/json',
    'Vary': 'Accept',
    'Plotly-Client-Platform': 'Python 3 0.3.2'
}


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    recent_searches = list(col.find().limit(10).sort("time", -1))
    print('recent_searches = ', recent_searches)
    sys.stdout.flush()
    return render_template('/index.html', form=JupyterForm(), recents=recent_searches, template="home-template")


@app.route("/notebook", methods=['POST', 'GET', 'OPTIONS'])
def notebook():
    """Return internal notebook."""
    app.static_folder = 'static'
    if request.method == 'POST':
        if ".ipynb" not in request.form['PlotlyURL']:
            error = Markup('<p class="error">Invalid URL: Please submit a Jupyter Notebook URL ending in .ipynb</p>')
            return render_template('/index.html', error=error, form=JupyterForm(), recents='', template="home-template")
        else:
            url = request.form['PlotlyURL']
            githubsource = url.replace("https://raw.githubusercontent.com/", "https://github.com/")
            firstslash = githubsource.find('/', 20)
            secondslash = githubsource.find('/', firstslash)
            repo_url = githubsource[0:secondslash]
            print('secondslash = ', secondslash)
            print('repo_url = ', repo_url)
            sys.stdout.flush()
            r = requests.get(base_external_url + url, headers=headers, auth=(username, password))
            response = r.json()['html']
            extract = Markup(response).strip()
            document = {'url': request.form['PlotlyURL'],
                        'time': yourtime,
                        'displaytime': prettytime,
                        'githuburl': repo_url
                        }
            result = col.replace_one({'url': document['url']}, document, upsert=True)
            return render_template('/notebook.html', content=extract, template="notebook-template")
