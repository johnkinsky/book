# Configuration file for the Sphinx documentation builder.
#
project = 'Technical Writing - From Basics to a Complex Systems Approach'
copyright = '2025, John M. Kinsky'
author = 'John Kinsky'
version = '1.0'

import os
import sys
sys.path.insert(0, os.path.abspath('./.'))  # Path to project root (docs/source)  

# -- General configuration ---------------------------------------------------
extensions = [
       'sphinx_book_theme',
       'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://sphinx-themes.org/#themes

html_theme = "sphinx_book_theme"
html_baseurl = "https://johnkinsky.github.io/book/"
html_static_path = ['_static'] # Path to HTML elements
html_logo = '_static/logo.png' # Path to logo file
html_use_index = False # Do not generate the index page

# Inject GA snippet via js script
html_js_files = [
    ('https://www.googletagmanager.com/gtag/js?id=id=G-929RXPVCFH', {'async': 'async'}),
    'jmk_gtag.js',
]