import sys, os
import json

# Imports
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flaskext.markdown import Markdown

# Configuration
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)

# Functionalities
# @app.context_processor
# def clever_function(u):
#     return 'hello'

# Routes
@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/projects/')
def projects():
    with open('data/projects.json') as projects_json:
        projects_data = json.load(projects_json)
        return render_template('projects.html', projects=projects_data)

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.errorhandler(404)
def page_not_found(path):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)

# app.jinja_env.globals.update(clever_function=clever_function)
# app.add_template_global(clever_function, name='clever_function')
