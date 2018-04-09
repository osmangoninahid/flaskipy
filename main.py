#!/usr/bin/python
# coding=utf-8
from routes import app

if __name__ == '__main__':
    # run application server
    app.run("0.0.0.0", 8000)
