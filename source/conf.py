# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VABS'
copyright = '2025, Wenbin Yu'
author = 'Wenbin Yu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'myst_parser',
    "sphinx.ext.githubpages",
    'sphinx_immaterial',
    'sphinxcontrib.bibtex',
    'sphinx_markdown_builder',
]

templates_path = ['_templates']
exclude_patterns = []

root_doc = 'index'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section'}

bibtex_bibfiles = ['refs.bib']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_theme_options = {
    # 'site_url': 'https://wenbinyugroup.github.io/sgio/',
    # 'repo_url': 'https://github.com/wenbinyugroup/sgio',
    # 'palette': {
    #     'primary': 'red'
    # },
    # # 'logo': {
    # #     'text': 'sgio',
    # # },
    # 'show_nav_level': 2,
    # # "path_to_docs": "doc/source",
    # # 'use_edit_page_button': True,
    # # "use_repository_button": True,
    # # "use_issues_button": True,
    # # 'collapse_navigation': True,
    # 'navigation_depth': 4,
    # "announcement": "Documentation is under construction.",
}

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath"
]
