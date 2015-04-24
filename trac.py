# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World, 陈自新"


@app.route("/member/")
def member():
    return "陈自新\n 代平 \n 毛毛"


if __name__ == "__main__":
    app.run()
