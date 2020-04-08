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
    return render_template('about.html')

@app.route('/blogs/')
def blogs():
    return render_template('blogs.html', pages=pages)

# @app.route('/about/')
# def about():
#     return render_template('about.html')

@app.route('/projects/')
def projects():
    with open('data/projects.json') as projects_json:
        projects_data = json.load(projects_json)
        return render_template('projects.html', projects=projects_data)

@app.route('/cs88/')
def cs88():
    with open('data/cs88.json') as cs88_json:
        cs88_data = json.load(cs88_json)
        return render_template('classes/cs88.html', info=cs88_data)

@app.route('/cs61c/')
def cs61c():
    with open('data/cs61c.json') as cs61c_json:
        cs61c_data = json.load(cs61c_json)
        return render_template('classes/cs61c.html', info=cs61c_data)

@app.route('/csw186/')
def csw186():
    with open('data/csw186.json') as csw186_json:
        csw186_data = json.load(csw186_json)
        return render_template('classes/csw186.html', info=csw186_data)

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
