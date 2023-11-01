# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Photonics with MEEP python'
copyright = '2023, Álvaro H. Bedoya, Leandro Uribe'
author = 'Álvaro H. Bedoya, Leandro Uribe'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#import nbsphinx
#import myst-nb
#import myst-parser

extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.mathjax',
               'sphinx.ext.autosectionlabel', 'sphinx_tabs.tabs' ]

myst_enable_extensions = ["amsmath", "dollarmath"]

source_suffix = ['.rst', '.md', '.ipynb']

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_rtd_theme
html_theme = "sphinxawesome_theme"

# these extensions only work for the sphinxawesome_theme
extensions += [
    "sphinxawesome_theme",
    "sphinxawesome_theme.highlighting",
    "sphinxawesome_theme.docsearch"
    # To help you with the upgrade to version 5:
    # "sphinxawesome.deprecated",
]

html_theme_options = {
    # ...
    "show_relbar_top": False,      # hides permalink heading on top
    "show_relbar_bottom": False,   # hides permalink heading on bottom
    "navigation_with_keys": True,  # enables navigation with n and p keyboard keys
    "show_prev_next": True         # adds navigation buttons
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

