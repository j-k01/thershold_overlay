from setuptools import setup, find_packages
import subprocess
import sys
import shutil
#import threshold_overlay

setup(
    name = "threshold_overlay",
    version = '1',
    url = 'https://github.com/j-k01/thershold_overlay',
    license = 'MIT',
    author = "John Kincaid",
    author_email = "john.kincaid@ucdenver.com",
    packages = ['threshold_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    description = "Overlay for PYNQ-Z1 implementing simple image thesholding. Enjoy 2x acceleration! Every cycle can count."
)
