import random
import string


class Config(object):
    def __init__(self, app):
        if not app.config.get("SECRET_KEY"):
            self.SECRET_KEY = "".join(
                random.sample(string.ascii_lowercase + string.digits, 32)
            )
