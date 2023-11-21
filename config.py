import secrets


class Config(object):
    def __init__(self, app):
        if not app.config.get("SECRET_KEY"):
            self.SECRET_KEY = secrets.token_urlsafe(64)
