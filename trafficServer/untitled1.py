# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:48:05 2021

@author: Deep
"""

<!-- {%extends "index.html"%}
{%block content%}
<link rel="stylesheet" href={{cdn_css | safe}} type="text/css"/>
<script type="text/javascript" src={{cdn_js | safe}}></script>

{{script1 | safe}}
{{div1 | safe}}
{%endblock%} -->