# conf.py for book/guide Sphinx builds.
import os
import sys
from datetime import datetime

# Get current year
current_year = datetime.now().year
# Project path (docs/source)
sys.path.insert(0, os.path.abspath('./.'))

# Set project details
project = 'Technical Documentation - From Basics to Complex Systems'
copyright = f"{current_year}, John M. Kinsky"
author = 'John M. Kinsky'
version = '0.9'

# General settings
extensions = ['sphinx_book_theme','myst_parser']
templates_path = ['_templates']
exclude_patterns = []

# HTML output settings
html_theme = "sphinx_book_theme"
html_baseurl = "https://johnkinsky.github.io/book/"
html_static_path = ['_static'] # Path to HTML elements
html_logo = '_static/logo.png' # Path to logo file
html_use_index = False # Do not generate the index page
html_theme_options = {
    "repository_url": "https://github.com/johnkinsky/book/",
    "use_repository_button": True
}

# Inject GA4 and other libraries as needed
html_js_files = [
    ('https://www.googletagmanager.com/gtag/js?id=id=G-929RXPVCFH', {'async': 'async'}),
    'jmk_gtag.js',
]
