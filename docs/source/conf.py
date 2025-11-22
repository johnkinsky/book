
# conf.py for book/guide Sphinx builds.
project = 'Technical Documentation - From Basics to Complex Systems'
copyright = '2025, John M. Kinsky'
author = 'John Kinsky'
version = '1.0'

import os
import sys

# Path to project (docs/source)  
sys.path.insert(0, os.path.abspath('./.'))  

# -- General Settings -------------------
extensions = ['sphinx_book_theme','myst_parser']
templates_path = ['_templates']
exclude_patterns = []

# -- HTML Output ------------------------

html_theme = "sphinx_book_theme"
html_baseurl = "https://johnkinsky.github.io/book/"
html_static_path = ['_static'] # Path to HTML elements
html_logo = '_static/logo.png' # Path to logo file
html_use_index = False # Do not generate the index page
html_theme_options = {
    "repository_url": "https://github.com/johnkinsky/book/",
    "use_repository_button": True
}

# -- Inject GA snippet reference---------
html_js_files = [
    ('https://www.googletagmanager.com/gtag/js?id=id=G-929RXPVCFH', {'async': 'async'}),
    'jmk_gtag.js',
]