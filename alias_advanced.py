''' Author: Sergey Cheh.
    
    add here discription
    version: 00000
'''



import os
from os import path as pt



ROOT_DIR = "/"
ROOT_USER_DIR = "root"
HOME_DIR = "home/"
LOGGED_USER = os.getlogin()
sy_SHELL = "default=/bin/bash"



def check_shell(sy_SHELL):
    # checks what $SHELL use
    # default = /bin/bash 
    sy_SHELL = os.environ['SHELL']
    print(('User start from %s\n')% sy_SHELL)
    return sy_SHELL

def search_history_file(sy_SHELL):
    # search *sh history file's directory       
    if (LOGGED_USER != ROOT_USER_DIR):
        sh_history_dir = '%s%s%s' % (ROOT_DIR, HOME_DIR, LOGGED_USER)
        os.chdir(pt.abspath(sh_history_dir))
    else:
        sh_history_dir = '%s%s' % (ROOT_DIR, ROOT_USER_DIR)
        os.chdir(pt.abspath(sh_history_dir))
        print("You've running like root!")
    
    print("Curent working path is %s" % pt.abspath(sh_history_dir))
    return sh_history_dir


# Block of Debug code
sy_SHELL = check_shell(sy_SHELL)
search_history_file(sy_SHELL);
