from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import new_overlay

setup(
    name = "new_overlay",
    version = new_overlay.__version__,
    url = 'https://github.com/your_github/new_overlay',
    license = 'All rights reserved.',
    author = "Your Name",
    author_email = "your@email.com",
    packages = ['new_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    description = "New custom overlay for PYNQ-Z1"
)