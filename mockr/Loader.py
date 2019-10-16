# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import os
import json
import codecs

Base_Path = os.path.dirname(__file__)

def load_char_maps():
    res_file_path = os.path.join(Base_Path, "res/sample.nim")
    with codecs.open(res_file_path, "r", "utf-8")as file_loader:
        char_maps = json.load(file_loader)
    return char_maps