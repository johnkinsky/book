# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Technical Writing - From Basics to a Complex Systems Approach'
copyright = '2025, John M. Kinsky'
author = 'John Kinsky'
version = '1.0'

import os
import sys
# sys.path.append(os.path.abspath("./_ext")) # Working for extensions; commented out for now.
sys.path.insert(0, os.path.abspath('../..'))  # Path to project root (docs/source)  


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
      'sphinxcontrib.mermaid',
      'myst_parser',
      'sphinx_design'
]
      #'external_links'
#https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/index.html
myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://sphinx-themes.org/#themes

html_theme = 'sphinx_book_theme'
html_static_path = ['_static'] # Path to HTML elements
html_logo = '_static/logo.png' # Path to logo file
html_use_index = False # Do not generate the index page


# -- Mermaid configuration ---------------------------------------------------
# Optional: Set Mermaid CLI or JS options
#mermaid_version = "10.9.0"  # Pin a specific Mermaid.js version
mermaid_output_format = "svg"  # Options: 'raw', 'png', 'svg'
mermaid_params = [
    "--theme", "default",  # Mermaid theme: default, dark, forest, neutral
]