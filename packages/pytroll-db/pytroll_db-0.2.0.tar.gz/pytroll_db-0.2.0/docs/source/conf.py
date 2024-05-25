# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os

from sphinx.ext import apidoc

from trolldb.version import __version__

autodoc_mock_imports = ["motor", "pydantic", "fastapi", "uvicorn", "loguru", "pyyaml"]

# -- Project information -----------------------------------------------------

project = "Pytroll-db"
copyright = "2024, Pytroll"
author = "Pouria Khalaj"

# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*tests/*"]
include_patterns = ["**"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "private-members": True,
    "special-members": True,
    "undoc-members": True,
}

root_doc = "index"

output_dir = os.path.join(".")
module_dir = os.path.abspath("../../trolldb")
apidoc.main(["-e", "-M", "-q", "-f", "-o", output_dir, module_dir, *include_patterns])
