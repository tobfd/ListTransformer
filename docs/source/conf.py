import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath("../"))

project = "ListTransformer"
copyright = f"{date.today().year}, tobfd"
author = "tobfd"
release = "0.2.0"


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

simplify_optional_unions = True

autodoc_member_order = "bysource"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]

html_title = f"<h3 align='center'>{release}</h3>"
html_logo = "_static/listtransformer_logo.png"
html_favicon = "_static/icologo.ico"
