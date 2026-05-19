# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "my_dataproc"
copyright = "2026, Edwin"
author = "Edwin"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # automatically generate API doc
    "autoapi.extension",
    # Allows mermaid diagrams to be used in the documentation
    "sphinxcontrib.mermaid",
]

autoapi_dirs = ["../../src"]

templates_path = ["_templates"]
exclude_patterns = []

language = "ko"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"  #'alabaster'
html_static_path = ["_static"]
