# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os
sys.path.insert(0, os.path.abspath('../'))
#sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "fogo")))
#sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))
#print (sys.path)
#sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))


sys.path.append('/Samsung Lab/PycharmProjects/IlhaProibida/fogo')

project = 'Ilha Proibida fogo'
copyright = '2023, fernanda, finn, vanessa e anderson'
author = 'fernanda, finn, vanessa e anderson'
release = '23.12'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt-Br'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
