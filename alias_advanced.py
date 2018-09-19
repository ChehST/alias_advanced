''' Author: Sergey Cheh.
    
    add here discription
    version: 00000
'''


import os
from os import path as pt   # to awoid namespace linked_saved? 



ROOT_DIR = "/"
HOME_DIR = "home/"
LOGGED_USER = os.getlogin()
sy_SHELL = "default=/bin/bash"




def check_shell(sy_SHELL):
    # checks what $SHELL use users system
    # default = /bin/bash
    new_sy_SHELL = os.environ['SHELL']
    print(('User start from %s')% sy_SHELL)
    sy_SHELL = str(new_sy_SHELL)

def search_history_file(sy_SHELL):
    # search *sh history file
    # create list with full dir to *sh users files
    # sample at bash=default to test the bar
    # see os.path to parse the history! at this point bar doesn't work        
    sh_history_dir = '%s%s%s' % (ROOT_DIR, HOME_DIR, LOGGED_USER)
    print(sh_history_dir)



new_sy_SHELL = check_shell(sy_SHELL)
search_history_file(new_sy_SHELL);
