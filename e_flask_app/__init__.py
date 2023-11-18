import logging
import tomllib
from pathlib import Path
from flask import Flask
from config import Config
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)
    app.config.from_file(
        Path(app.instance_path) / Path("config.toml"),
        load=tomllib.load,
        text=False,
    )
    config = Config(app)
    app.config.from_object(config)
    print(app.config)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    # configure logging to accoimdate for gunicorn in production, else DEBUG
    if app.config['ENV'] == 'production':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    else:
        app.logger.setLevel('DEBUG')

    from . import views

    app.register_blueprint(views.bp)

    return app
