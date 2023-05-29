from flask import Flask
from main.__init__ import init_apis

def create_app():
    app = Flask(__name__)
    init_apis()
    return app
