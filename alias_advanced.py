''' Author: Sergey Cheh.
    
    add here discription
    version: 00000
'''

import os
from os import path as pt   # to awoid namespace linked_saved? 



def check_shell():
    sy_SHELL = "default=/bin/bash"
    # checks what $SHELL use users system
    # default = /bin/bash
    sy_SHELL = os.environ['SHELL']
    print(('User start from %s')% sy_SHELL)
    return sy_SHELL;

def search_history_file():
    # search *sh history file
    pass

check_shell();
