# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '简立得®操作手册'
copyright = '哈尔滨工业大学重庆研究院' 

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

language ='zh'

templates_path = ['_templates']

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = "sphinxawesome_theme"
# extensions = ["sphinxawesome_theme"]
# html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_title = "简立得®操作手册"
#html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
# display_version = False

extensions = ['recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# html_additional_pages = {
#   'download': 'my1.html',
#}

# extensions = ["sphinx_design"]
