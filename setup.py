#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
name = "robotframework-robotmk",
version = "1.0.2",
author = "Simon Meggle",
author_email = "simon.meggle@elabit.de",
py_modules = ["robotmk"],
long_description = README,
long_description_content_type = "text/markdown",
url = "https://github.com/simonmeggle/robotframework-robotmk",
license = "GPLv3",
)
