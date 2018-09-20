''' Author: Sergey Cheh.
    
    add here discription
    version: 00000
'''


import os
from os import path as pt   # to awoid namespace linked_saved? 



ROOT_DIR = "/"
ROOT_USER_DIR = "root"
HOME_DIR = "home/"
LOGGED_USER = os.getlogin()
sy_SHELL = "default=/bin/bash"




def check_shell(sy_SHELL):
    # checks what $SHELL use users system
    # default = /bin/bash
    new_sy_SHELL = os.environ['SHELL']
    print(('User start from %s')% new_sy_SHELL)
    sy_SHELL = str(new_sy_SHELL)
    return sy_SHELL

def search_history_file(sy_SHELL):
    # search *sh history file
    # create list with full dir to *sh users files
    # sample at bash=default to test the bar
    # see os.path to parse the history! at this point bar doen't work        
    print(sy_SHELL, LOGGED_USER, ROOT_USER_DIR)
    if (LOGGED_USER != ROOT_USER_DIR):
        sh_history_dir = '%s%s%s/' % (ROOT_DIR, HOME_DIR, LOGGED_USER)
        print(sh_history_dir)
        pt.split(sh_history_dir[1])
        history_path = pt.exists(sh_history_dir)
        print(history_path) # debug is var returnd to path compabitiy whith os.path
        '''here we gonna use pt.curdir debug manupulations'''
        os.chdir(pt.abspath(sh_history_dir))
    else:
        sh_history_dir = '%s%s/' % (ROOT_DIR, ROOT_USER_DIR)
        os.chdir(pt.abspath(sh_history_dir))

        print("You'r root! Why this ELSE run?!")
    print("abs path is %s" % pt.abspath(pt.curdir))


new_sy_SHELL = check_shell(sy_SHELL)
search_history_file(new_sy_SHELL);
