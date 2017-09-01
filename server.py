#!/usr/bin/python3
#-*- coding: utf-8 -*-
""" minimal web interface """

# Standard library imports
from __future__ import print_function
from datetime import datetime
from functools import wraps
from json import decoder, dumps, loads
from os import getenv, path

# Third party library imports
from flask import Flask, render_template, request, Response, redirect, url_for, send_from_directory
from urllib3 import disable_warnings
from requests import get, post
from requests.exceptions import ConnectionError
from werkzeug import secure_filename

APP = Flask(__name__)
APP.config.from_pyfile('settings.txt')

@APP.route('/')
def index():
    """ Display home page """
    return render_template('homepage.html')

@APP.route('/page1/')
def first_page():
    """ Display page 1 """
    name = APP.config['STATIC_VAR']
    return render_template('page1.html', username=name)

@APP.errorhandler(404)
def page_not_found(_):
    """ Display error page """
    return render_template('404.html'), 404

if __name__ == '__main__':
    PORT = int(getenv('PORT', 5000))
    APP.run(debug=True, host='0.0.0.0', port=PORT)
