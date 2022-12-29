# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '简立得'
copyright = '哈尔滨工业大学重庆研究院' 

language ='zh'

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []

html_theme = 'sphinx_book_theme'

html_title = ""
html_logo = "_static/1.png"
html_favicon = "_static/logo.png"


extensions = ['recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

#extensions = ['sphinx_toolbox.collapse'] 


