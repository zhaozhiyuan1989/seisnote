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
from datetime import datetime

# -- Project information -----------------------------------------------------
author = "赵志远"
project = "地震学学习笔记"
copyright = f"2017–{datetime.today().year}, {author}"
github_user = "zhaozhiyuan1989"
github_repo = "seisnote"
github_url = f"https://github.com/{github_user}/{github_repo}"

# The full version, including alpha/beta/rc tags

# -- Contributor information -------------------------------------------------

rst_prolog = """
.. |赵志远| replace:: `赵志远 <https://github.com/zhaozhiyuan1989>`__
"""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx_cjkspace.cjkspace",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_extra_path = []
html_last_updated_fmt = "%Y年%m月%d日"
html_title = project
html_css_files = ["custom.css"]

html_context = {
    "favicon": "favicon.ico",
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo,
    "github_version": "main",
    "conf_py_path": "/source/",
    "theme_vcs_pageview_mode": "blob",
    "menu_links": [
        (
            '<i class="fa fa-github fa-fw"></i> 网站源码',
            github_url,
        ),
         (
            '<i class="fa fa-envelope fa-fw"></i> E-mail',
            "mailto:shetu2008@163.com",
        ),
    ],
}