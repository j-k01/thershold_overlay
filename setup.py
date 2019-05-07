#import threshold_overlay

from setuptools import setup, find_packages
from distutils.dir_util import copy_tree
import os
import shutil



# global variables

#board = os.environ['BOARD']
repo_board_folder = f'threshold_overlay'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']


# copy overlays to python package

def copy_overlays():
    src_ol_dir = repo_board_folder
    dst_ol_dir = os.path.join(os.environ['HOME'], 'pynq','overlays','threshold_overlay')
    if not os.path.exists(dst_nd_dir):
        os.mkdir(dst_ol_dir)
    copy_tree(src_ol_dir, dst_ol_dir)
    #hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])

# copy notebooks to jupyter home

def copy_notebooks():
    src_nb_dir = f'notebook'
    dst_nb_dir = os.path.join(board_notebooks_dir, 'threshold_overlay')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)

copy_overlays()
copy_notebooks()


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
