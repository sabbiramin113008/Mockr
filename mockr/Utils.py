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
        self.db_file_name = f"{self.dir_name}/db.json"
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

    def write_db(self, response):
        with codecs.open(self.db_file_name, "w", "utf-8") as file_writer:
            json.dump(response, file_writer, indent=2, ensure_ascii=False)

    def pre_response_builder(self):
        env = Environment()

        project_name = self.contents["name"]
        date = self.contents["date"]
        context = {
            "project_name": project_name,
            "date": date
        }
        # template = Template(tem_about)
        template = Template(tem_for_loop)
        t_for_loop = Template(tem_for_loop).render()
        # return template.render(context)
        response = template.render()
        template_final = Template(template_file)
        f_response = template_final.render(response=response)
        return f_response
        # return env.from_string(tem_about).render(context)

    def response_builder(self):
        db = {}
        for index, route in enumerate(self.contents["routes"]):
            try:
                req_body = route["request"]["body"]
            except:
                req_body = {}
            try:
                res_body = route["response"]["body"]
            except:
                res_body = {}

            db[str(index)] = {"request": req_body, "response": res_body}

        tem_about_context = {
            "project_name": self.contents["name"],
            "date": self.contents["date"]
        }
        tem_about_response = Template(tem_about).render(tem_about_context)

        tem_footer_response = Template(tem_footer).render()

        routes = ''''''
        headers_check = ''''''
        html_contents = ''''''
        for index, route in enumerate(self.contents["routes"]):
            path = route["path"]
            method = str(route["method"]).upper()
            route_name = str(route["route_name"]).rstrip().lstrip().replace(" ", "_").lower()
            status = route["response"]["status"]
            try:
                header_dict = route["request"]["header"]
                for k, v in header_dict.items():
                    key_name = str(k)
                    key_val = str(v)
                    print("Value:", key_val)

                    headers_check_response = Template(tem_headers_check).render(
                        key_name=key_name,
                        key_val=key_val
                    )
                    headers_check = headers_check + headers_check_response

                h = 1
            except:
                header_dict = {}
                h = 0

            r_response = Template(tem_route).render(
                path=path,
                method=method,
                h=h,
                headers_check=headers_check,
                route_name=route_name,
                rid=str(index),
                status=status
            )
            routes = routes + r_response

            r_html_content_response = Template(tem_api_content).render(
                route_name=route_name,
                method_lower=str(method).lower(),
                method_upper=str(method).upper(),
                path=path,
                res_body=str(route["response"]["body"]).replace("'","\""),
                status=status
            )
            html_contents = html_contents + r_html_content_response

            print("routes: ", routes)
        print("Final Routes:", routes)
        print("Final Headers Check:", headers_check)

        html_content_response = Template(tem_html).render(
            html_header=tem_html_header,
            html_contents=html_contents,
            html_footer=tem_html_footer

        )
        print("Final HTML Chech:", html_content_response)

        tem_header_response = Template(tem_header).render(
            html=html_content_response
        )

        tem_final_response = Template(tem_final).render(
            tem_about=tem_about_response,
            tem_header=tem_header_response,
            tem_routes=routes,
            tem_footer=tem_footer_response
        )
        return tem_final_response, db
