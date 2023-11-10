import os
import uuid


class Config(object):
    ENV = os.getenv("FLASK_ENV", "production")
    SECRET_KEY = os.getenv("SECREET_KEY", uuid.uuid4().hex)
