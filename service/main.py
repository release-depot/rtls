#!/usr/bin/env python
""" Main runner for the service """

from flask import Flask
from flask_restful import Api

from resources.rtls import Rtls


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Rtls, '/rtls/',
                     '/rtls/<string:package>/<string:change_id>',
                     resource_class_kwargs={'logger': app.logger})

    return app


def run():
    from logging import INFO
    app = create_app()
    app.logger.setLevel(INFO)
    app.run(port=8080)


def run_debug():
    from logging import DEBUG
    app = create_app()
    app.logger.setLevel(DEBUG)
    app.run(port=8080)


if __name__ == '__main__':
    run_debug()
