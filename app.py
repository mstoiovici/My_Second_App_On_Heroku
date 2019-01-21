# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:41:45 2019

@author: maria
"""

from flask import Flask,render_template,request
app=Flask("MyApp")

@app.route("/")
def hello():
    return "Hello world!!!!!"

app.run(debug=True)