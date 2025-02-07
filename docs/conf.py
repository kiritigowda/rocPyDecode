# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re

with open('../CMakeLists.txt', encoding='utf-8') as f:
    match = re.search(r'.*\bset\(VERSION\s+\"?([0-9.]+)[^0-9.]+', f.read())
    if not match:
        raise ValueError("VERSION not found!")
    version_number = match[1]
left_nav_title = f"rocPyDecode {version_number} Documentation"

extensions = ["rocm_docs"]
external_toc_path = "./sphinx/_toc.yml"
external_projects_current_project = "rocpydecode"
external_projects_remote_repository = ""

html_theme = "rocm_docs_theme"
html_theme_options = {"flavor": "rocm"}
html_title = left_nav_title

version = version_number
release = version_number
html_title = left_nav_title
project = "rocPyDecode"
author = "Advanced Micro Devices, Inc."
copyright = (
    "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."
)
