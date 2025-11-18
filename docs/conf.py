## Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_management_system.settings")
django.setup()

# -- Project information -----------------------------------------------------
project = "Student Management System"
copyright = "2024, Sinesipho Matam"
author = "Sinesipho Matam"
release = "00.00.02"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]