''' Author: Sergey Cheh.
    
    add here discription
    version: 00000
'''

import os
from os import path as pt   # to awoid namespace linked_saved? 



sy_SHELL = "default=/bin/bash"

def check_shell(sy_SHELL):
    # checks what $SHELL use users system
    # default = /bin/bash
    sy_SHELL = os.environ['SHELL']
    print(('User start from %s')% sy_SHELL)
    return sy_SHELL;

def search_history_file(sy_SHELL):
    # search *sh history file
    # create list with full dir to *sh users files
    # sample at bash=default to test the bar
    # see os.path to parse the history! at this point bar doesn't work        
    if sy_SHELL == 1:
        sh_history = pt.exists('/home/cheh/')
    else:
        print('no matches found!')

check_shell(sy_SHELL);
search_history_file(sy_SHELL);
