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
import os
import sys
sys.setrecursionlimit(1500)

# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LBM_Saclay'
copyright = '2025, LBM_Saclay Workforce'
author = 'LBM_Saclay Workforce'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx_design',
    'sphinx_pdf_generate',
    'sphinxcontrib.bibtex'
]
bibtex_default_style = 'plain'
bibtex_bibfiles = ['./src_doc/BIBLIO/Biblio.bib','./src_doc/BIBLIO/LBM_CEA.bib']

htmlhelp_basename = 'LBM_Saclay Documentation'

# To show or not private members 
autodoc_default_options = {     "members": True,     "undoc-members": True,     "private-members": False  }
# generate autosummary even if no references
numpydoc_show_class_members = False
autosummary_generate = False
autosummary_imported_members = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'press'
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'bizstyle'
#html_theme = "sphinx_rtd_theme"
#html_theme = 'pyramid'
#html_theme = 'agogo'
#html_theme = 'traditional'
#html_theme = 'classic'
#html_theme = 'nature'
#html_theme = 'scrolls'
#html_theme = 'haiku'
#html_theme = 'default'
#html_theme = 'sphinx_material'
#html_theme = 'pydata_sphinx_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']
#pygments_style = 'manni','inkpot','vim','emacs','monokai','sphinx'
pygments_style = 'perldoc'

# Enable numref
numfig = True
show_authors = True

# inside conf.py
latex_engine = 'xelatex'
latex_elements = {
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'sphinxsetup': 'TitleColor=DarkGoldenrod',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'
