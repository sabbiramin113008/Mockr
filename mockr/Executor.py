# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from .Utils import *


def generate():
    dir_name = input("Enter The Mock Dir Name: ")
    explore = Explore(dir_name=dir_name)
    content = explore.read_file()
    if content:
        msg = '''
        Enter: 
            1 -> Generate 'server.py' With API Documentation
            2 -> Generate API Documentation
        
        '''
        choice = input(msg)
        if str(choice) == '1':
            response, db = explore.build_py_and_doc()

            print("db:", db)
            explore.write_db(db)
            explore.write_file(response)
            print(response)
        if str(choice) == '2':
            response = explore.build_doc()
            explore.write_file(response,target_file_type="api_doc")
    else:
        print("No Content")
