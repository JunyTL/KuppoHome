import os

from flask import Flask

from .db import init_app
from .kuppo_home import bp as kuppo_home_bp
from .member import bp as member_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)    # create app

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'kuppo.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_app(app)

    app.register_blueprint(kuppo_home_bp)
    app.register_blueprint(member_bp)

    app.add_url_rule('/', endpoint='home')

    return app

app = create_app()
