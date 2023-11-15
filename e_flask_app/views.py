from logging import getLevelName
from datetime import datetime
from flask import Blueprint, current_app, render_template

bp = Blueprint("views", __name__)


@bp.route("/")
def index():
    greeting="Hello, World!"
    current_app.logger.info(f'{greeting=}')
    return render_template("index.html", greeting=greeting)


@bp.route("/logging", methods=["GET"])
def write_test_data_to_log():
    now = datetime.utcnow()
    current_app.logger.critical(f"#\nnow: {now}")
    current_app.logger.critical(
        f"log level: {getLevelName(current_app.logger.level)} {current_app.logger.level}\n#"
    )
    current_app.logger.debug("LOG TEST: DEBUG 10")
    current_app.logger.info("LOG TEST: INFO 20")
    current_app.logger.warning("LOG TEST: WARNING 30")
    current_app.logger.error("LOG TEST: ERROR 40")
    current_app.logger.critical("LOG TEST: CRITICAL 50")
    return {
        "now": now,
        "log level": f"{getLevelName(current_app.logger.level)} {current_app.logger.level}",
    }, 200
