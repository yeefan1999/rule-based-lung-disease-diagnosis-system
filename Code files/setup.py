# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:03:06 2020

@author: yeefan
"""

import cx_Freeze
import sys
import os
import os.path

import re
import clips
import tkinter
if sys.platform =='win32':
    base = 'Win32GUI'
    
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

executables = [cx_Freeze.Executable('es.py')]

cx_Freeze.setup(
    name='Lung Diagnosis',
    version='0.01',
    executables=executables,
    options={"build_exe":{"packages":["tkinter","re","clips"],
                          'include_files':[
                              os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6'),
                              os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')
                              ]}}
    
    )
