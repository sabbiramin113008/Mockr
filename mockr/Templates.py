# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

tem_about = '''# -*- coding: utf-8 -*-
"""

author: S.M. Sabbir Amin
project_name: {{project_name}}
date: {{date}}

"""
'''

tem_for_loop = '''


{% for i in range(10)%}
print ("Ola")
{% endfor %}


'''
template_file = '''

{{response}}

'''

tem_header = '''
import json
import codecs
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = 'YourDummySecretKeyIsHere'
with codecs.open("db.json","r","utf-8") as f:
    db = json.load(f)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World</h1>'
    
'''

tem_route = '''
@app.route('{{path}}',methods=['{{method}}'])
def {{route_name}}():
    if request.method == '{{method}}':
    {% if h %}
        {{headers_check}}
        response = db["{{rid}}"]["response"]
        return jsonify(response),{{status}}
    {% else %}
        response = db["{{rid}}"]["response"]
        return jsonify(response),{{status}}
    {% endif %}
'''

tem_routes = '''

{{routes}}

'''

tem_headers_check = '''
        try:
            key = "{{key_val}}"
            key = request.headers["{{key_name}}"]
        except KeyError:
            return jsonify({"flag":"KEY_MISSING"})
'''
















tem_footer = '''app.run(
    port=8000,
    host="localhost",
    debug=True
    )
'''

tem_final = '''
{{tem_about}}

{{tem_header}}

{{tem_routes}}

{{tem_footer}}

'''
