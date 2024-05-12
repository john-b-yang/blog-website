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

posts = [page for page in list(pages) if not page.path.startswith('r/')]
reviews = [page for page in list(pages) if page.path.startswith('r/')]

# Sort review tags by most popular
review_tags = {}
for page in list(reviews):
    for tag in page.meta['tags']:
        if tag not in review_tags:
            review_tags[tag] = 0
        review_tags[tag] += 1
review_tags = dict(sorted(review_tags.items(), key=lambda item: -1 * item[1])[:10])

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
    return render_template('blogs.html', pages=posts, tag="all")

@app.route('/readings/')
def papers():
    return render_template('papers.html', pages=reviews, tags=review_tags, tag="all")

@app.route('/papers/<string:tag>/')
def paper_tag(tag):
    return render_template('papers.html', pages=reviews, tags=review_tags, tag=tag)

@app.route('/projects/')
def projects():
    with open('data/projects.json') as projects_json:
        projects_data = json.load(projects_json)
        return render_template('projects.html', projects=projects_data)

@app.route('/cs88/')
def cs88():
    with open('data/teach/cs88.json') as cs88_json:
        return render_template('classes/cs88.html', info=json.load(cs88_json))

@app.route('/cs61c/')
def cs61c():
    with open('data/teach/cs61c.json') as cs61c_json:
        return render_template('classes/cs61c.html', info=json.load(cs61c_json))

@app.route('/cs186/')
def cs186():
    with open('data/teach/cs186.json') as cs186_json:
        return render_template('classes/cs186.html', info=json.load(cs186_json))

@app.route('/cs169/')
def cs169():
    with open('data/teach/cs169.json') as cs169_json:
        return render_template('classes/cs169.html', info=json.load(cs169_json))

@app.route('/cs161/')
def cs161():
    with open('data/teach/cs161.json') as cs161_json:
        return render_template('classes/cs161.html', info=json.load(cs161_json))

@app.route('/cs1/')
def cs1():
    with open('data/teach/cs1.json') as cs1_json:
        return render_template('classes/cs1.html', info=json.load(cs1_json))

@app.route('/cs2/')
def cs2():
    with open('data/teach/cs2.json') as cs2_json:
        return render_template('classes/cs2.html', info=json.load(cs2_json))

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/subscribe/')
def subscribe():
    return render_template('subscribe.html')

@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path))

@app.route('/review/<path:path>/')
def review(path):
    return render_template('review.html', review=pages.get_or_404(path))

@app.route('/publications/')
def publications():
    with open('data/publications.json') as pubs_json:
        return render_template('publications.html', pubs=json.load(pubs_json))

@app.errorhandler(404)
def page_not_found(path):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5001))
        app.run(host='0.0.0.0', port=port)

# app.jinja_env.globals.update(clever_function=clever_function)
# app.add_template_global(clever_function, name='clever_function')
