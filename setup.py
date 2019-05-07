from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import threshold_overlay

setup(
    name = "threshold_overlay",
    version = new_overlay.__version__,
    url = 'https://github.com/j-k01/thershold_overlay',
    license = 'MIT',
    author = "John Kincaid",
    author_email = "john.kincaid@ucdenver.com",
    packages = ['treshold_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    description = "Overlay for PYNQ-Z1 implementing simple image thesholding. Enjoy 2x acceleration! Every cycle can count."
)
