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
@app.route('/docs')
@app.route('/index')
def index():
    return """{{html}}"""
    
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

tem_prism_css = '''
/* PrismJS 1.17.1
https://prismjs.com/download.html#themes=prism-okaidia&languages=json+python */
/**
 * okaidia theme for JavaScript, CSS and HTML
 * Loosely based on Monokai textmate theme by http://www.monokai.nl/
 * @author ocodia
 */

code[class*="language-"],
pre[class*="language-"] {
	color: #f8f8f2;
	background: none;
	text-shadow: 0 1px rgba(0, 0, 0, 0.3);
	font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
	font-size: 1em;
	text-align: left;
	white-space: pre;
	word-spacing: normal;
	word-break: normal;
	word-wrap: normal;
	line-height: 1.5;

	-moz-tab-size: 4;
	-o-tab-size: 4;
	tab-size: 4;

	-webkit-hyphens: none;
	-moz-hyphens: none;
	-ms-hyphens: none;
	hyphens: none;
}

/* Code blocks */
pre[class*="language-"] {
	padding: 1em;
	margin: .5em 0;
	overflow: auto;
	border-radius: 0.3em;
}

:not(pre) > code[class*="language-"],
pre[class*="language-"] {
	background: #272822;
}

/* Inline code */
:not(pre) > code[class*="language-"] {
	padding: .1em;
	border-radius: .3em;
	white-space: normal;
}

.token.comment,
.token.prolog,
.token.doctype,
.token.cdata {
	color: slategray;
}

.token.punctuation {
	color: #f8f8f2;
}

.namespace {
	opacity: .7;
}

.token.property,
.token.tag,
.token.constant,
.token.symbol,
.token.deleted {
	color: #f92672;
}

.token.boolean,
.token.number {
	color: #ae81ff;
}

.token.selector,
.token.attr-name,
.token.string,
.token.char,
.token.builtin,
.token.inserted {
	color: #a6e22e;
}

.token.operator,
.token.entity,
.token.url,
.language-css .token.string,
.style .token.string,
.token.variable {
	color: #f8f8f2;
}

.token.atrule,
.token.attr-value,
.token.function,
.token.class-name {
	color: #e6db74;
}

.token.keyword {
	color: #66d9ef;
}

.token.regex,
.token.important {
	color: #fd971f;
}

.token.important,
.token.bold {
	font-weight: bold;
}
.token.italic {
	font-style: italic;
}

.token.entity {
	cursor: help;
}


'''

tem_prism_js = '''
/* PrismJS 1.17.1
https://prismjs.com/download.html#themes=prism-okaidia&languages=json+python */
var _self="undefined"!=typeof window?window:"undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?self:{},Prism=function(c){var g=/\blang(?:uage)?-([\w-]+)\b/i,a=0;var _={manual:c.Prism&&c.Prism.manual,disableWorkerMessageHandler:c.Prism&&c.Prism.disableWorkerMessageHandler,util:{encode:function(e){return e instanceof L?new L(e.type,_.util.encode(e.content),e.alias):Array.isArray(e)?e.map(_.util.encode):e.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/\u00a0/g," ")},type:function(e){return Object.prototype.toString.call(e).slice(8,-1)},objId:function(e){return e.__id||Object.defineProperty(e,"__id",{value:++a}),e.__id},clone:function n(e,r){var t,a,i=_.util.type(e);switch(r=r||{},i){case"Object":if(a=_.util.objId(e),r[a])return r[a];for(var o in t={},r[a]=t,e)e.hasOwnProperty(o)&&(t[o]=n(e[o],r));return t;case"Array":return a=_.util.objId(e),r[a]?r[a]:(t=[],r[a]=t,e.forEach(function(e,a){t[a]=n(e,r)}),t);default:return e}}},languages:{extend:function(e,a){var n=_.util.clone(_.languages[e]);for(var r in a)n[r]=a[r];return n},insertBefore:function(n,e,a,r){var t=(r=r||_.languages)[n],i={};for(var o in t)if(t.hasOwnProperty(o)){if(o==e)for(var l in a)a.hasOwnProperty(l)&&(i[l]=a[l]);a.hasOwnProperty(o)||(i[o]=t[o])}var s=r[n];return r[n]=i,_.languages.DFS(_.languages,function(e,a){a===s&&e!=n&&(this[e]=i)}),i},DFS:function e(a,n,r,t){t=t||{};var i=_.util.objId;for(var o in a)if(a.hasOwnProperty(o)){n.call(a,o,a[o],r||o);var l=a[o],s=_.util.type(l);"Object"!==s||t[i(l)]?"Array"!==s||t[i(l)]||(t[i(l)]=!0,e(l,n,o,t)):(t[i(l)]=!0,e(l,n,null,t))}}},plugins:{},highlightAll:function(e,a){_.highlightAllUnder(document,e,a)},highlightAllUnder:function(e,a,n){var r={callback:n,selector:'code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'};_.hooks.run("before-highlightall",r);for(var t,i=e.querySelectorAll(r.selector),o=0;t=i[o++];)_.highlightElement(t,!0===a,r.callback)},highlightElement:function(e,a,n){var r=function(e){for(;e&&!g.test(e.className);)e=e.parentNode;return e?(e.className.match(g)||[,"none"])[1].toLowerCase():"none"}(e),t=_.languages[r];e.className=e.className.replace(g,"").replace(/\s+/g," ")+" language-"+r;var i=e.parentNode;i&&"pre"===i.nodeName.toLowerCase()&&(i.className=i.className.replace(g,"").replace(/\s+/g," ")+" language-"+r);var o={element:e,language:r,grammar:t,code:e.textContent};function l(e){o.highlightedCode=e,_.hooks.run("before-insert",o),o.element.innerHTML=o.highlightedCode,_.hooks.run("after-highlight",o),_.hooks.run("complete",o),n&&n.call(o.element)}if(_.hooks.run("before-sanity-check",o),!o.code)return _.hooks.run("complete",o),void(n&&n.call(o.element));if(_.hooks.run("before-highlight",o),o.grammar)if(a&&c.Worker){var s=new Worker(_.filename);s.onmessage=function(e){l(e.data)},s.postMessage(JSON.stringify({language:o.language,code:o.code,immediateClose:!0}))}else l(_.highlight(o.code,o.grammar,o.language));else l(_.util.encode(o.code))},highlight:function(e,a,n){var r={code:e,grammar:a,language:n};return _.hooks.run("before-tokenize",r),r.tokens=_.tokenize(r.code,r.grammar),_.hooks.run("after-tokenize",r),L.stringify(_.util.encode(r.tokens),r.language)},matchGrammar:function(e,a,n,r,t,i,o){for(var l in n)if(n.hasOwnProperty(l)&&n[l]){var s=n[l];s=Array.isArray(s)?s:[s];for(var c=0;c<s.length;++c){if(o&&o==l+","+c)return;var g=s[c],u=g.inside,h=!!g.lookbehind,f=!!g.greedy,d=0,m=g.alias;if(f&&!g.pattern.global){var p=g.pattern.toString().match(/[imsuy]*$/)[0];g.pattern=RegExp(g.pattern.source,p+"g")}g=g.pattern||g;for(var y=r,v=t;y<a.length;v+=a[y].length,++y){var k=a[y];if(a.length>e.length)return;if(!(k instanceof L)){if(f&&y!=a.length-1){if(g.lastIndex=v,!(x=g.exec(e)))break;for(var b=x.index+(h&&x[1]?x[1].length:0),w=x.index+x[0].length,A=y,P=v,O=a.length;A<O&&(P<w||!a[A].type&&!a[A-1].greedy);++A)(P+=a[A].length)<=b&&(++y,v=P);if(a[y]instanceof L)continue;j=A-y,k=e.slice(v,P),x.index-=v}else{g.lastIndex=0;var x=g.exec(k),j=1}if(x){h&&(d=x[1]?x[1].length:0);w=(b=x.index+d)+(x=x[0].slice(d)).length;var N=k.slice(0,b),S=k.slice(w),C=[y,j];N&&(++y,v+=N.length,C.push(N));var E=new L(l,u?_.tokenize(x,u):x,m,x,f);if(C.push(E),S&&C.push(S),Array.prototype.splice.apply(a,C),1!=j&&_.matchGrammar(e,a,n,y,v,!0,l+","+c),i)break}else if(i)break}}}}},tokenize:function(e,a){var n=[e],r=a.rest;if(r){for(var t in r)a[t]=r[t];delete a.rest}return _.matchGrammar(e,n,a,0,0,!1),n},hooks:{all:{},add:function(e,a){var n=_.hooks.all;n[e]=n[e]||[],n[e].push(a)},run:function(e,a){var n=_.hooks.all[e];if(n&&n.length)for(var r,t=0;r=n[t++];)r(a)}},Token:L};function L(e,a,n,r,t){this.type=e,this.content=a,this.alias=n,this.length=0|(r||"").length,this.greedy=!!t}if(c.Prism=_,L.stringify=function(e,a){if("string"==typeof e)return e;if(Array.isArray(e))return e.map(function(e){return L.stringify(e,a)}).join("");var n={type:e.type,content:L.stringify(e.content,a),tag:"span",classes:["token",e.type],attributes:{},language:a};if(e.alias){var r=Array.isArray(e.alias)?e.alias:[e.alias];Array.prototype.push.apply(n.classes,r)}_.hooks.run("wrap",n);var t=Object.keys(n.attributes).map(function(e){return e+'="'+(n.attributes[e]||"").replace(/"/g,"&quot;")+'"'}).join(" ");return"<"+n.tag+' class="'+n.classes.join(" ")+'"'+(t?" "+t:"")+">"+n.content+"</"+n.tag+">"},!c.document)return c.addEventListener&&(_.disableWorkerMessageHandler||c.addEventListener("message",function(e){var a=JSON.parse(e.data),n=a.language,r=a.code,t=a.immediateClose;c.postMessage(_.highlight(r,_.languages[n],n)),t&&c.close()},!1)),_;var e=document.currentScript||[].slice.call(document.getElementsByTagName("script")).pop();return e&&(_.filename=e.src,_.manual||e.hasAttribute("data-manual")||("loading"!==document.readyState?window.requestAnimationFrame?window.requestAnimationFrame(_.highlightAll):window.setTimeout(_.highlightAll,16):document.addEventListener("DOMContentLoaded",_.highlightAll))),_}(_self);"undefined"!=typeof module&&module.exports&&(module.exports=Prism),"undefined"!=typeof global&&(global.Prism=Prism);
Prism.languages.json={property:{pattern:/"(?:\\.|[^\\"\r\n])*"(?=\s*:)/,greedy:!0},string:{pattern:/"(?:\\.|[^\\"\r\n])*"(?!\s*:)/,greedy:!0},comment:/\/\/.*|\/\*[\s\S]*?(?:\*\/|$)/,number:/-?\d+\.?\d*(e[+-]?\d+)?/i,punctuation:/[{}[\],]/,operator:/:/,boolean:/\b(?:true|false)\b/,null:{pattern:/\bnull\b/,alias:"keyword"}};
'''

tem_api_content = '''
<div class="resource">
                    <h3 class="resource-heading">{{route_name}}</h3>
                    <p>{{route_name}}</p>
                    <div class="action get">
                        <h4 class="action-heading">
                            <div class="name">{{route_name}}</div>
                            <a href="#" class="method {{method_lower}}">{{method_upper}}</a>
                            <code class="uri">{{path}}</code>
                        </h4>
                        <h4>Example URL</h4>
                        <div class="definition">
                            <span class="method {{method_lower}}">{{method_upper}}</span>&nbsp;<span class="uri">
                            <span class="hostname">http://localhost:3000</span>
                            {{path}}</span>
                        </div>
                        <div class="title"><strong>Response&nbsp;&nbsp;<code>{{status}}</code></strong>
                            <div class="inner">
                            <pre><code class="language-json">{{res_body}}</code></pre>
                            </div>
                        </div>
                    </div>
                </div>



'''

tem_html_header = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mock API</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <!--<link href="https://myCDN.com/prism@v1.x/themes/prism.css" rel="stylesheet"/>-->
    <!--<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.17.1/themes/prism.min.css">-->

    <style>@import url('https://fonts.googleapis.com/css?family=Roboto:400,700|Inconsolata|Raleway:200');

    /*Prism CSS Code Init*/

    /* PrismJS 1.17.1
https://prismjs.com/download.html#themes=prism-okaidia&languages=json+python */
    /**
     * okaidia theme for JavaScript, CSS and HTML
     * Loosely based on Monokai textmate theme by http://www.monokai.nl/
     * @author ocodia
     */

    code[class*="language-"],
    pre[class*="language-"] {
        color: #f8f8f2;
        background: none;
        text-shadow: 0 1px rgba(0, 0, 0, 0.3);
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        font-size: 1em;
        text-align: left;
        white-space: pre;
        word-spacing: normal;
        word-break: normal;
        word-wrap: normal;
        line-height: 1.5;

        -moz-tab-size: 4;
        -o-tab-size: 4;
        tab-size: 4;

        -webkit-hyphens: none;
        -moz-hyphens: none;
        -ms-hyphens: none;
        hyphens: none;
    }

    /* Code blocks */
    pre[class*="language-"] {
        padding: 1em;
        margin: .5em 0;
        overflow: auto;
        border-radius: 0.3em;
    }

    :not(pre) > code[class*="language-"],
    pre[class*="language-"] {
        background: #272822;
    }

    /* Inline code */
    :not(pre) > code[class*="language-"] {
        padding: .1em;
        border-radius: .3em;
        white-space: normal;
    }

    .token.comment,
    .token.prolog,
    .token.doctype,
    .token.cdata {
        color: slategray;
    }

    .token.punctuation {
        color: #f8f8f2;
    }

    .namespace {
        opacity: .7;
    }

    .token.property,
    .token.tag,
    .token.constant,
    .token.symbol,
    .token.deleted {
        color: #f92672;
    }

    .token.boolean,
    .token.number {
        color: #ae81ff;
    }

    .token.selector,
    .token.attr-name,
    .token.string,
    .token.char,
    .token.builtin,
    .token.inserted {
        color: #a6e22e;
    }

    .token.operator,
    .token.entity,
    .token.url,
    .language-css .token.string,
    .style .token.string,
    .token.variable {
        color: #f8f8f2;
    }

    .token.atrule,
    .token.attr-value,
    .token.function,
    .token.class-name {
        color: #e6db74;
    }

    .token.keyword {
        color: #66d9ef;
    }

    .token.regex,
    .token.important {
        color: #fd971f;
    }

    .token.important,
    .token.bold {
        font-weight: bold;
    }

    .token.italic {
        font-style: italic;
    }

    .token.entity {
        cursor: help;
    }

    /*Prism CSS Code Done*/

    .hljs-comment, .hljs-title {
        color: #8e908c
    }

    .hljs-variable, .hljs-attribute, .hljs-tag, .hljs-regexp, .ruby .hljs-constant, .xml .hljs-tag .hljs-title, .xml .hljs-pi, .xml .hljs-doctype, .html .hljs-doctype, .css .hljs-id, .css .hljs-class, .css .hljs-pseudo {
        color: #c82829
    }

    .hljs-number, .hljs-preprocessor, .hljs-pragma, .hljs-built_in, .hljs-literal, .hljs-params, .hljs-constant {
        color: #f5871f
    }

    .ruby .hljs-class .hljs-title, .css .hljs-rules .hljs-attribute {
        color: #eab700
    }

    .hljs-string, .hljs-value, .hljs-inheritance, .hljs-header, .ruby .hljs-symbol, .xml .hljs-cdata {
        color: #718c00
    }

    .css .hljs-hexcolor {
        color: #3e999f
    }

    .hljs-function, .python .hljs-decorator, .python .hljs-title, .ruby .hljs-function .hljs-title, .ruby .hljs-title .hljs-keyword, .perl .hljs-sub, .javascript .hljs-title, .coffeescript .hljs-title {
        color: #4271ae
    }

    .hljs-keyword, .javascript .hljs-function {
        color: #8959a8
    }

    .hljs {
        display: block;
        background: white;
        color: #4d4d4c;
        padding: .5em
    }

    .coffeescript .javascript, .javascript .xml, .tex .hljs-formula, .xml .javascript, .xml .vbscript, .xml .css, .xml .hljs-cdata {
        opacity: .5
    }

    .right .hljs-comment {
        color: #969896
    }

    .right .css .hljs-class, .right .css .hljs-id, .right .css .hljs-pseudo, .right .hljs-attribute, .right .hljs-regexp, .right .hljs-tag, .right .hljs-variable, .right .html .hljs-doctype, .right .ruby .hljs-constant, .right .xml .hljs-doctype, .right .xml .hljs-pi, .right .xml .hljs-tag .hljs-title {
        color: #c66
    }

    .right .hljs-built_in, .right .hljs-constant, .right .hljs-literal, .right .hljs-number, .right .hljs-params, .right .hljs-pragma, .right .hljs-preprocessor {
        color: #de935f
    }

    .right .css .hljs-rule .hljs-attribute, .right .ruby .hljs-class .hljs-title {
        color: #f0c674
    }

    .right .hljs-header, .right .hljs-inheritance, .right .hljs-name, .right .hljs-string, .right .hljs-value, .right .ruby .hljs-symbol, .right .xml .hljs-cdata {
        color: #b5bd68
    }

    .right .css .hljs-hexcolor, .right .hljs-title {
        color: #8abeb7
    }

    .right .coffeescript .hljs-title, .right .hljs-function, .right .javascript .hljs-title, .right .perl .hljs-sub, .right .python .hljs-decorator, .right .python .hljs-title, .right .ruby .hljs-function .hljs-title, .right .ruby .hljs-title .hljs-keyword {
        color: #81a2be
    }

    .right .hljs-keyword, .right .javascript .hljs-function {
        color: #b294bb
    }

    .right .hljs {
        display: block;
        overflow-x: auto;
        background: #1d1f21;
        color: #c5c8c6;
        padding: .5em;
        -webkit-text-size-adjust: none
    }

    .right .coffeescript .javascript, .right .javascript .xml, .right .tex .hljs-formula, .right .xml .css, .right .xml .hljs-cdata, .right .xml .javascript, .right .xml .vbscript {
        opacity: .5
    }

    body {
        color: black;
        background: white;
        font: 400 14px / 1.42 'Roboto', Helvetica, sans-serif
    }

    header {
        border-bottom: 1px solid #f2f2f2;
        margin-bottom: 12px
    }

    h1, h2, h3, h4, h5 {
        color: black;
        margin: 12px 0
    }

    h1 .permalink, h2 .permalink, h3 .permalink, h4 .permalink, h5 .permalink {
        margin-left: 0;
        opacity: 0;
        transition: opacity .25s ease
    }

    h1:hover .permalink, h2:hover .permalink, h3:hover .permalink, h4:hover .permalink, h5:hover .permalink {
        opacity: 1
    }

    .triple h1 .permalink, .triple h2 .permalink, .triple h3 .permalink, .triple h4 .permalink, .triple h5 .permalink {
        opacity: .15
    }

    .triple h1:hover .permalink, .triple h2:hover .permalink, .triple h3:hover .permalink, .triple h4:hover .permalink, .triple h5:hover .permalink {
        opacity: .15
    }

    h1 {
        font: 200 36px 'Raleway', Helvetica, sans-serif;
        font-size: 36px
    }

    h2 {
        font: 200 36px 'Raleway', Helvetica, sans-serif;
        font-size: 30px
    }

    h3 {
        font-size: 100%;
        text-transform: uppercase
    }

    h5 {
        font-size: 100%;
        font-weight: normal
    }

    p {
        margin: 0 0 10px
    }

    p.choices {
        line-height: 1.6
    }

    a {
        color: #428bca;
        text-decoration: none
    }

    li p {
        margin: 0
    }

    hr.split {
        border: 0;
        height: 1px;
        width: 100%;
        padding-left: 6px;
        margin: 12px auto;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0) 20%, rgba(0, 0, 0, 0.2) 51.4%, rgba(255, 255, 255, 0.2) 51.4%, rgba(255, 255, 255, 0) 80%)
    }

    dl dt {
        float: left;
        width: 130px;
        clear: left;
        text-align: right;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        font-weight: 700
    }

    dl dd {
        margin-left: 150px
    }

    blockquote {
        color: rgba(0, 0, 0, 0.5);
        font-size: 15.5px;
        padding: 10px 20px;
        margin: 12px 0;
        border-left: 5px solid #e8e8e8
    }

    blockquote p:last-child {
        margin-bottom: 0
    }

    pre {
        background-color: #f5f5f5;
        padding: 12px;
        border: 1px solid #cfcfcf;
        border-radius: 6px;
        overflow: auto
    }

    pre code {
        color: black;
        background-color: transparent;
        padding: 0;
        border: none
    }

    code {
        color: #444;
        background-color: #f5f5f5;
        font: 'Inconsolata', monospace;
        padding: 1px 4px;
        border: 1px solid #cfcfcf;
        border-radius: 3px
    }

    ul, ol {
        padding-left: 2em
    }

    table {
        border-collapse: collapse;
        border-spacing: 0;
        margin-bottom: 12px
    }

    table tr:nth-child(2n) {
        background-color: #fafafa
    }

    table th, table td {
        padding: 6px 12px;
        border: 1px solid #e6e6e6
    }

    .text-muted {
        opacity: .5
    }

    .note, .warning {
        padding: .3em 1em;
        margin: 1em 0;
        border-radius: 2px;
        font-size: 90%
    }

    .note h1, .warning h1, .note h2, .warning h2, .note h3, .warning h3, .note h4, .warning h4, .note h5, .warning h5, .note h6, .warning h6 {
        font-family: 200 36px 'Raleway', Helvetica, sans-serif;
        font-size: 135%;
        font-weight: 500
    }

    .note p, .warning p {
        margin: .5em 0
    }

    .note {
        color: black;
        background-color: #f0f6fb;
        border-left: 4px solid #428bca
    }

    .note h1, .note h2, .note h3, .note h4, .note h5, .note h6 {
        color: #428bca
    }

    .warning {
        color: black;
        background-color: #fbf1f0;
        border-left: 4px solid #c9302c
    }

    .warning h1, .warning h2, .warning h3, .warning h4, .warning h5, .warning h6 {
        color: #c9302c
    }

    header {
        margin-top: 24px
    }

    nav {
        position: fixed;
        top: 24px;
        bottom: 0;
        overflow-y: auto
    }

    nav .resource-group {
        padding: 0
    }

    nav .resource-group .heading {
        position: relative
    }

    nav .resource-group .heading .chevron {
        position: absolute;
        top: 12px;
        right: 12px;
        opacity: .5
    }

    nav .resource-group .heading a {
        display: block;
        color: black;
        opacity: .7;
        border-left: 2px solid transparent;
        margin: 0
    }

    nav .resource-group .heading a:hover {
        text-decoration: none;
        background-color: bad-color;
        border-left: 2px solid black
    }

    nav ul {
        list-style-type: none;
        padding-left: 0
    }

    nav ul a {
        display: block;
        font-size: 13px;
        color: rgba(0, 0, 0, 0.7);
        padding: 8px 12px;
        border-top: 1px solid #d9d9d9;
        border-left: 2px solid transparent;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap
    }

    nav ul a:hover {
        text-decoration: none;
        background-color: bad-color;
        border-left: 2px solid black
    }

    nav ul > li {
        margin: 0
    }

    nav ul > li:first-child {
        margin-top: -12px
    }

    nav ul > li:last-child {
        margin-bottom: -12px
    }

    nav ul ul a {
        padding-left: 24px
    }

    nav ul ul li {
        margin: 0
    }

    nav ul ul li:first-child {
        margin-top: 0
    }

    nav ul ul li:last-child {
        margin-bottom: 0
    }

    nav > div > div > ul > li:first-child > a {
        border-top: none
    }

    .preload * {
        transition: none !important
    }

    .pull-left {
        float: left
    }

    .pull-right {
        float: right
    }

    .badge {
        display: inline-block;
        float: right;
        min-width: 10px;
        min-height: 14px;
        padding: 3px 7px;
        font-size: 12px;
        color: #000;
        background-color: #f2f2f2;
        border-radius: 10px;
        margin: -2px 0
    }

    .badge.get {
        color: #70bbe1;
        background-color: #d9edf7
    }

    .badge.head {
        color: #70bbe1;
        background-color: #d9edf7
    }

    .badge.options {
        color: #70bbe1;
        background-color: #d9edf7
    }

    .badge.put {
        color: #f0db70;
        background-color: #fcf8e3
    }

    .badge.patch {
        color: #f0db70;
        background-color: #fcf8e3
    }

    .badge.post {
        color: #93cd7c;
        background-color: #dff0d8
    }

    .badge.delete {
        color: #ce8383;
        background-color: #f2dede
    }

    .collapse-button {
        float: right
    }

    .collapse-button .close {
        display: none;
        color: #428bca;
        cursor: pointer
    }

    .collapse-button .open {
        color: #428bca;
        cursor: pointer
    }

    .collapse-button.show .close {
        display: inline
    }

    .collapse-button.show .open {
        display: none
    }

    .collapse-content {
        max-height: 0;
        overflow: hidden;
        transition: max-height .3s ease-in-out
    }

    nav {
        width: 220px
    }

    .container {
        max-width: 940px;
        margin-left: auto;
        margin-right: auto
    }

    .container .row .content {
        margin-left: 244px;
        width: 696px
    }

    .container .row:after {
        content: '';
        display: block;
        clear: both
    }

    .container-fluid nav {
        width: 22%
    }

    .container-fluid .row .content {
        margin-left: 24%
    }

    .container-fluid.triple nav {
        width: 16.5%;
        padding-right: 1px
    }

    .container-fluid.triple .row .content {
        position: relative;
        margin-left: 16.5%;
        padding-left: 24px
    }

    .middle:before, .middle:after {
        content: '';
        display: table
    }

    .middle:after {
        clear: both
    }

    .middle {
        box-sizing: border-box;
        width: 51.5%;
        padding-right: 12px
    }

    .right {
        box-sizing: border-box;
        float: right;
        width: 48.5%;
        padding-left: 12px
    }

    .right a {
        color: #428bca
    }

    .right h1, .right h2, .right h3, .right h4, .right h5, .right p, .right div {
        color: white
    }

    .right pre {
        background-color: #1d1f21;
        border: 1px solid #1d1f21
    }

    .right pre code {
        color: #c5c8c6
    }

    .right .description {
        margin-top: 12px
    }

    .triple .resource-heading {
        font-size: 125%
    }

    .definition {
        margin-top: 12px;
        margin-bottom: 12px
    }

    .definition .method {
        font-weight: bold
    }

    .definition .method.get {
        color: #2e8ab8
    }

    .definition .method.head {
        color: #2e8ab8
    }

    .definition .method.options {
        color: #2e8ab8
    }

    .definition .method.post {
        color: #56b82e
    }

    .definition .method.put {
        color: #b8a22e
    }

    .definition .method.patch {
        color: #b8a22e
    }

    .definition .method.delete {
        color: #b82e2e
    }

    .definition .uri {
        word-break: break-all;
        word-wrap: break-word
    }

    .definition .hostname {
        opacity: .5
    }

    .example-names {
        background-color: #eee;
        padding: 12px;
        border-radius: 6px
    }

    .example-names .tab-button {
        cursor: pointer;
        color: black;
        border: 1px solid #ddd;
        padding: 6px;
        margin-left: 12px
    }

    .example-names .tab-button.active {
        background-color: #d5d5d5
    }

    .right .example-names {
        background-color: #444
    }

    .right .example-names .tab-button {
        color: white;
        border: 1px solid #666;
        border-radius: 6px
    }

    .right .example-names .tab-button.active {
        background-color: #5e5e5e
    }

    #nav-background {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: 16.5%;
        padding-right: 14.4px;
        background-color: #fbfbfb;
        border-right: 1px solid #f0f0f0;
        z-index: -1
    }

    #right-panel-background {
        position: absolute;
        right: -12px;
        top: -12px;
        bottom: -12px;
        width: 48.6%;
        background-color: #333;
        z-index: -1
    }

    @media (max-width: 1200px) {
        nav {
            width: 198px
        }

        .container {
            max-width: 840px
        }

        .container .row .content {
            margin-left: 224px;
            width: 606px
        }
    }

    @media (max-width: 992px) {
        nav {
            width: 169.4px
        }

        .container {
            max-width: 720px
        }

        .container .row .content {
            margin-left: 194px;
            width: 526px
        }
    }

    @media (max-width: 768px) {
        nav {
            display: none
        }

        .container {
            width: 95%;
            max-width: none
        }

        .container .row .content, .container-fluid .row .content, .container-fluid.triple .row .content {
            margin-left: auto;
            margin-right: auto;
            width: 95%
        }

        #nav-background {
            display: none
        }

        #right-panel-background {
            width: 48.6%
        }
    }

    .back-to-top {
        position: fixed;
        z-index: 1;
        bottom: 0;
        right: 24px;
        padding: 4px 8px;
        color: rgba(0, 0, 0, 0.5);
        background-color: #f2f2f2;
        text-decoration: none !important;
        border-top: 1px solid #d9d9d9;
        border-left: 1px solid #d9d9d9;
        border-right: 1px solid #d9d9d9;
        border-top-left-radius: 3px;
        border-top-right-radius: 3px
    }

    .resource-group {
        padding: 12px;
        margin-bottom: 12px;
        background-color: white;
        border: 1px solid #d9d9d9;
        border-radius: 6px
    }

    .resource-group h2.group-heading, .resource-group .heading a {
        padding: 12px;
        margin: -12px -12px 12px -12px;
        background-color: #f2f2f2;
        border-bottom: 1px solid #d9d9d9;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden
    }

    .triple .content .resource-group {
        padding: 0;
        border: none
    }

    .triple .content .resource-group h2.group-heading, .triple .content .resource-group .heading a {
        margin: 0 0 12px 0;
        border: 1px solid #d9d9d9
    }

    nav .resource-group .heading a {
        padding: 12px;
        margin-bottom: 0
    }

    nav .resource-group .collapse-content {
        padding: 0
    }

    .action {
        margin-bottom: 12px;
        padding: 12px 12px 0 12px;
        overflow: hidden;
        border: 1px solid transparent;
        border-radius: 6px
    }

    .action h4.action-heading {
        padding: 6px 12px;
        margin: -12px -12px 12px -12px;
        border-bottom: 1px solid transparent;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        overflow: hidden
    }

    .action h4.action-heading .name {
        float: right;
        font-weight: normal;
        padding: 6px 0
    }

    .action h4.action-heading .method {
        padding: 6px 12px;
        margin-right: 12px;
        border-radius: 3px;
        display: inline-block
    }

    .action h4.action-heading .method.get {
        color: #000;
        background-color: #337ab7
    }

    .action h4.action-heading .method.head {
        color: #000;
        background-color: #337ab7
    }

    .action h4.action-heading .method.options {
        color: #000;
        background-color: #337ab7
    }

    .action h4.action-heading .method.put {
        color: #000;
        background-color: #ed9c28
    }

    .action h4.action-heading .method.patch {
        color: #000;
        background-color: #ed9c28
    }

    .action h4.action-heading .method.post {
        color: #000;
        background-color: #5cb85c
    }

    .action h4.action-heading .method.delete {
        color: #000;
        background-color: #d9534f
    }

    .action h4.action-heading code {
        color: #444;
        background-color: #f5f5f5;
        border-color: #cfcfcf;
        font-weight: normal;
        word-break: break-all;
        display: inline-block;
        margin-top: 2px
    }

    .action dl.inner {
        padding-bottom: 2px
    }

    .action .title {
        border-bottom: 1px solid white;
        margin: 0 -12px -1px -12px;
        padding: 12px
    }

    .action.get {
        border-color: #bce8f1
    }

    .action.get h4.action-heading {
        color: #337ab7;
        background: #d9edf7;
        border-bottom-color: #bce8f1
    }

    .action.head {
        border-color: #bce8f1
    }

    .action.head h4.action-heading {
        color: #337ab7;
        background: #d9edf7;
        border-bottom-color: #bce8f1
    }

    .action.options {
        border-color: #bce8f1
    }

    .action.options h4.action-heading {
        color: #337ab7;
        background: #d9edf7;
        border-bottom-color: #bce8f1
    }

    .action.post {
        border-color: #d6e9c6
    }

    .action.post h4.action-heading {
        color: #5cb85c;
        background: #dff0d8;
        border-bottom-color: #d6e9c6
    }

    .action.put {
        border-color: #faebcc
    }

    .action.put h4.action-heading {
        color: #ed9c28;
        background: #fcf8e3;
        border-bottom-color: #faebcc
    }

    .action.patch {
        border-color: #faebcc
    }

    .action.patch h4.action-heading {
        color: #ed9c28;
        background: #fcf8e3;
        border-bottom-color: #faebcc
    }

    .action.delete {
        border-color: #ebccd1
    }

    .action.delete h4.action-heading {
        color: #d9534f;
        background: #f2dede;
        border-bottom-color: #ebccd1
    }</style>
</head>
<body class="preload"><a href="#top" class="text-muted back-to-top">
    <i class="fa fa-toggle-up"></i>&nbsp;Back to top</a>
<div class="container">
    <div class="row">
        <div class="content">
            <header><h2>Mock Test API</h2></header>
            <section class="resource-group">

'''
tem_html_footer = '''
</section>
        </div>
    </div>

</div>
<script>
    
   /* PrismJS 1.17.1
     https://prismjs.com/download.html#themes=prism-okaidia&languages=json+python */
    var _self = "undefined" != typeof window ? window : "undefined" != typeof WorkerGlobalScope && self instanceof WorkerGlobalScope ? self : {},
        Prism = function (c) {
            var g = /\\blang(?:uage)?-([\w-]+)\\b/i, a = 0;
            var _ = {
                manual: c.Prism && c.Prism.manual,
                disableWorkerMessageHandler: c.Prism && c.Prism.disableWorkerMessageHandler,
                util: {
                    encode: function (e) {
                        return e instanceof L ? new L(e.type, _.util.encode(e.content), e.alias) : Array.isArray(e) ? e.map(_.util.encode) : e.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/\\u00a0/g, " ")
                    }, type: function (e) {
                        return Object.prototype.toString.call(e).slice(8, -1)
                    }, objId: function (e) {
                        return e.__id || Object.defineProperty(e, "__id", {value: ++a}), e.__id
                    }, clone: function n(e, r) {
                        var t, a, i = _.util.type(e);
                        switch (r = r || {}, i) {
                            case"Object":
                                if (a = _.util.objId(e), r[a])return r[a];
                                for (var o in t = {}, r[a] = t, e)e.hasOwnProperty(o) && (t[o] = n(e[o], r));
                                return t;
                            case"Array":
                                return a = _.util.objId(e), r[a] ? r[a] : (t = [], r[a] = t, e.forEach(function (e, a) {
                                    t[a] = n(e, r)
                                }), t);
                            default:
                                return e
                        }
                    }
                },
                languages: {
                    extend: function (e, a) {
                        var n = _.util.clone(_.languages[e]);
                        for (var r in a)n[r] = a[r];
                        return n
                    }, insertBefore: function (n, e, a, r) {
                        var t = (r = r || _.languages)[n], i = {};
                        for (var o in t)if (t.hasOwnProperty(o)) {
                            if (o == e)for (var l in a)a.hasOwnProperty(l) && (i[l] = a[l]);
                            a.hasOwnProperty(o) || (i[o] = t[o])
                        }
                        var s = r[n];
                        return r[n] = i, _.languages.DFS(_.languages, function (e, a) {
                            a === s && e != n && (this[e] = i)
                        }), i
                    }, DFS: function e(a, n, r, t) {
                        t = t || {};
                        var i = _.util.objId;
                        for (var o in a)if (a.hasOwnProperty(o)) {
                            n.call(a, o, a[o], r || o);
                            var l = a[o], s = _.util.type(l);
                            "Object" !== s || t[i(l)] ? "Array" !== s || t[i(l)] || (t[i(l)] = !0, e(l, n, o, t)) : (t[i(l)] = !0, e(l, n, null, t))
                        }
                    }
                },
                plugins: {},
                highlightAll: function (e, a) {
                    _.highlightAllUnder(document, e, a)
                },
                highlightAllUnder: function (e, a, n) {
                    var r = {
                        callback: n,
                        selector: 'code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'
                    };
                    _.hooks.run("before-highlightall", r);
                    for (var t, i = e.querySelectorAll(r.selector),
                             o = 0; t = i[o++];)_.highlightElement(t, !0 === a, r.callback)
                },
                highlightElement: function (e, a, n) {
                    var r = function (e) {
                        for (; e && !g.test(e.className);)e = e.parentNode;
                        return e ? (e.className.match(g) || [, "none"])[1].toLowerCase() : "none"
                    }(e), t = _.languages[r];
                    e.className = e.className.replace(g, "").replace(/\s+/g, " ") + " language-" + r;
                    var i = e.parentNode;
                    i && "pre" === i.nodeName.toLowerCase() && (i.className = i.className.replace(g, "").replace(/\s+/g, " ") + " language-" + r);
                    var o = {element: e, language: r, grammar: t, code: e.textContent};

                    function l(e) {
                        o.highlightedCode = e, _.hooks.run("before-insert", o), o.element.innerHTML = o.highlightedCode, _.hooks.run("after-highlight", o), _.hooks.run("complete", o), n && n.call(o.element)
                    }

                    if (_.hooks.run("before-sanity-check", o), !o.code)return _.hooks.run("complete", o), void(n && n.call(o.element));
                    if (_.hooks.run("before-highlight", o), o.grammar)if (a && c.Worker) {
                        var s = new Worker(_.filename);
                        s.onmessage = function (e) {
                            l(e.data)
                        }, s.postMessage(JSON.stringify({language: o.language, code: o.code, immediateClose: !0}))
                    } else l(_.highlight(o.code, o.grammar, o.language)); else l(_.util.encode(o.code))
                },
                highlight: function (e, a, n) {
                    var r = {code: e, grammar: a, language: n};
                    return _.hooks.run("before-tokenize", r), r.tokens = _.tokenize(r.code, r.grammar), _.hooks.run("after-tokenize", r), L.stringify(_.util.encode(r.tokens), r.language)
                },
                matchGrammar: function (e, a, n, r, t, i, o) {
                    for (var l in n)if (n.hasOwnProperty(l) && n[l]) {
                        var s = n[l];
                        s = Array.isArray(s) ? s : [s];
                        for (var c = 0; c < s.length; ++c) {
                            if (o && o == l + "," + c)return;
                            var g = s[c], u = g.inside, h = !!g.lookbehind, f = !!g.greedy, d = 0, m = g.alias;
                            if (f && !g.pattern.global) {
                                var p = g.pattern.toString().match(/[imsuy]*$/)[0];
                                g.pattern = RegExp(g.pattern.source, p + "g")
                            }
                            g = g.pattern || g;
                            for (var y = r, v = t; y < a.length; v += a[y].length, ++y) {
                                var k = a[y];
                                if (a.length > e.length)return;
                                if (!(k instanceof L)) {
                                    if (f && y != a.length - 1) {
                                        if (g.lastIndex = v, !(x = g.exec(e)))break;
                                        for (var b = x.index + (h && x[1] ? x[1].length : 0), w = x.index + x[0].length,
                                                 A = y, P = v,
                                                 O = a.length; A < O && (P < w || !a[A].type && !a[A - 1].greedy); ++A)(P += a[A].length) <= b && (++y, v = P);
                                        if (a[y] instanceof L)continue;
                                        j = A - y, k = e.slice(v, P), x.index -= v
                                    } else {
                                        g.lastIndex = 0;
                                        var x = g.exec(k), j = 1
                                    }
                                    if (x) {
                                        h && (d = x[1] ? x[1].length : 0);
                                        w = (b = x.index + d) + (x = x[0].slice(d)).length;
                                        var N = k.slice(0, b), S = k.slice(w), C = [y, j];
                                        N && (++y, v += N.length, C.push(N));
                                        var E = new L(l, u ? _.tokenize(x, u) : x, m, x, f);
                                        if (C.push(E), S && C.push(S), Array.prototype.splice.apply(a, C), 1 != j && _.matchGrammar(e, a, n, y, v, !0, l + "," + c), i)break
                                    } else if (i)break
                                }
                            }
                        }
                    }
                },
                tokenize: function (e, a) {
                    var n = [e], r = a.rest;
                    if (r) {
                        for (var t in r)a[t] = r[t];
                        delete a.rest
                    }
                    return _.matchGrammar(e, n, a, 0, 0, !1), n
                },
                hooks: {
                    all: {}, add: function (e, a) {
                        var n = _.hooks.all;
                        n[e] = n[e] || [], n[e].push(a)
                    }, run: function (e, a) {
                        var n = _.hooks.all[e];
                        if (n && n.length)for (var r, t = 0; r = n[t++];)r(a)
                    }
                },
                Token: L
            };

            function L(e, a, n, r, t) {
                this.type = e, this.content = a, this.alias = n, this.length = 0 | (r || "").length, this.greedy = !!t
            }

            if (c.Prism = _, L.stringify = function (e, a) {
                    if ("string" == typeof e)return e;
                    if (Array.isArray(e))return e.map(function (e) {
                        return L.stringify(e, a)
                    }).join("");
                    var n = {
                        type: e.type,
                        content: L.stringify(e.content, a),
                        tag: "span",
                        classes: ["token", e.type],
                        attributes: {},
                        language: a
                    };
                    if (e.alias) {
                        var r = Array.isArray(e.alias) ? e.alias : [e.alias];
                        Array.prototype.push.apply(n.classes, r)
                    }
                    _.hooks.run("wrap", n);
                    var t = Object.keys(n.attributes).map(function (e) {
                        return e + '="' + (n.attributes[e] || "").replace(/"/g, "&quot;") + '"'
                    }).join(" ");
                    return "<" + n.tag + ' class="' + n.classes.join(" ") + '"' + (t ? " " + t : "") + ">" + n.content + "</" + n.tag + ">"
                }, !c.document)return c.addEventListener && (_.disableWorkerMessageHandler || c.addEventListener("message", function (e) {
                var a = JSON.parse(e.data), n = a.language, r = a.code, t = a.immediateClose;
                c.postMessage(_.highlight(r, _.languages[n], n)), t && c.close()
            }, !1)), _;
            var e = document.currentScript || [].slice.call(document.getElementsByTagName("script")).pop();
            return e && (_.filename = e.src, _.manual || e.hasAttribute("data-manual") || ("loading" !== document.readyState ? window.requestAnimationFrame ? window.requestAnimationFrame(_.highlightAll) : window.setTimeout(_.highlightAll, 16) : document.addEventListener("DOMContentLoaded", _.highlightAll))), _
        }(_self);
    "undefined" != typeof module && module.exports && (module.exports = Prism), "undefined" != typeof global && (global.Prism = Prism);
    Prism.languages.json = {
        property: {pattern: /"(?:\\\.|[^\\"\\r\\n])*"(?=\s*:)/, greedy: !0},
        string: {pattern: /"(?:\\.|[^\\"\\r\\n])*"(?!\s*:)/, greedy: !0},
        comment: /\/\/.*|\/\*[\s\S]*?(?:\*\/|$)/,
        number: /-?\d+\.?\d*(e[+-]?\d+)?/i,
        punctuation: /[{}[\],]/,
        operator: /:/,
        boolean: /\\b(?:true|false)\\b/,
        null: {pattern: /\\bnull\\b/, alias: "keyword"}
    };
</script>
</body>
</html>
'''
tem_html = '''
{{html_header}}
{{html_contents}}
{{html_footer}}
'''
