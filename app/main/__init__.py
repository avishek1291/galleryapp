from api import main_api
from flask import Flask
from blueprints.healthcheck.namespace.health_check_namespace import namespace as health_check_ns
from blueprints.blueprint import root_blue_print


def init_apis(app: Flask):
    main_api.add_namespace(health_check_ns)
    app.register_blueprint(root_blue_print)
