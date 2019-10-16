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
        response, db = explore.response_builder()

        print("db:", db)
        explore.write_db(db)
        explore.write_file(response)
        print(response)

    else:
        print("No Content")
