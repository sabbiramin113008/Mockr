# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import codecs
import json

from jinja2 import Environment, Template

from .Templates import *


class Explore(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.source_file = f"{self.dir_name}\mock.json"
        self.target_file_name = f"{self.dir_name}/server.py"
        self.contents = None

    def read_file(self):
        try:
            with codecs.open(self.source_file, "r", "utf-8") as file_reader:
                contents = json.load(file_reader)
                print("contents:", contents)
                self.contents = contents
                return contents
        except Exception as e:
            print("Error:", e)
            return None

    def write_file(self, response):
        with codecs.open(self.target_file_name, "w", "utf-8") as file_writer:
            file_writer.write(response)

    def response_builder(self):
        env = Environment()

        project_name = self.contents["name"]
        date = self.contents["date"]
        context = {
            "project_name": project_name,
            "date": date
        }
        template = Template(template_about)
        return template.render(context)
        # return env.from_string(template_about).render(context)
