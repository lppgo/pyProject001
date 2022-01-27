#!/usr/bin/env python
# coding: utf-8

import flask

App = flask.Flask(__name__)


@App.route("/")
def index():
    return "Hello world !"


# 调用index函数
if __name__ == "__main__":
    App.run(debug=True)
