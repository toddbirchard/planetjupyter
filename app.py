from flask import Flask, url_for, render_template, Markup, request, Response
from config import key, col, db, base_url, base_external_url, base_account_url
import requests
from form import JupyterForm
from flask_assets import Bundle, Environment
from flask_static_compress import FlaskStaticCompress
import logging
import sys
from currenttime import yourtime, prettytime

app = Flask(__name__)
compress = FlaskStaticCompress(app)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static'
app.config['COMPRESSOR_OUTPUT_DIR'] = '/sdist'
app.static_folder = 'static'

headers = {
  'Access-Control-Allow-Origin': '*',
  'Plotly-Client-Platform': 'Python 3 0.3.2',
  'Authorization': key,
  'Content-Type': 'application/json'
}


@app.route('/', methods=['GET', 'POST'])
def home():
    """Landing page."""
    recent_searches = list(col.find().limit(5).sort("time", -1))
    print('recent_searches = ', recent_searches)
    sys.stdout.flush()
    return render_template('/index.html', form=JupyterForm(), recents=recent_searches, template="home-template")


@app.route("/notebook")
def notebook():
    """Return internal notebook."""
    #r = requests.get(base_account_url + notebookID, auth=(username, password), headers=headers)
    r2 = requests.get(base_account_url, auth=(username, password), headers={'Content-Type': 'text/html'})
    return render_template('/notebook.html', content=Markup(r2.text), template="notebook-template")


@app.route("/notebookResult", methods=['POST'])
def notebookResult():
    """Return internal notebook."""
    app.static_folder = 'static'
    url = request.form['PlotlyURL']
    githubsource = url.replace("https://raw.githubusercontent.com/", "https://github.com/")
    repo_url = githubsource.rsplit('/', 2)[0]
    if request.method == 'POST':
        url = request.form['PlotlyURL']
        r = requests.get(base_external_url + url, headers={'Content-Type': 'application/json'})
        extract = Markup(r.json()['html'].strip())
        document = {'url': request.form['PlotlyURL'],
                    'time': yourtime,
                    'displaytime': prettytime,
                    'githuburl': repo_url
                    }
        result = col.replace_one({'url': document['url']}, document, upsert=True)
        return render_template('/notebook.html', content=extract, headers=headers, template="notebook-template")
    else:
        return render_template('/index.html')


@app.route("/example")
def example():
    """Return external notebook."""
    app.static_folder = 'static'
    r = requests.get(base_external_url + 'https://raw.githubusercontent.com/mattalhonte/sfi-challenge/master/ComplexityChallengeWriteup.ipynb', headers={'Content-Type': 'application/json', 'Plotly-Client-Platform': 'Lisp'})
    extract = Markup(r.json()['html'].strip())
    return render_template('/notebook.html', content=extract, template="notebook-template")
