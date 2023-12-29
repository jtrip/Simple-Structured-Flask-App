from logging import getLevelName
from datetime import datetime, timezone
from flask import current_app, render_template
from app.main import bp


@bp.route("/")
def index():
    greeting = "Hello, World!"
    current_app.logger.info(f"{greeting=}")
    return render_template("index.html", greeting=greeting)


@bp.route("/logging", methods=["GET"])
def log_log_data():
    now_utc = datetime.now(timezone.utc)
    current_log_level_msg = f"log level:\t{getLevelName(current_app.logger.level)} {current_app.logger.level}"
    current_app.logger.critical(
        f"\n# now:\t\t{now_utc.isoformat()}\n# {current_log_level_msg}"
    )
    current_app.logger.debug("\t\tLOG TEST: DEBUG\t\t10")
    current_app.logger.info("\t\tLOG TEST: INFO\t\t20")
    current_app.logger.warning("\tLOG TEST: WARNING\t30")
    current_app.logger.error("\t\tLOG TEST: ERROR\t\t40")
    current_app.logger.critical("\tLOG TEST: CRITICAL\t50")
    return {
        "now": now_utc.isoformat(),
        "log level": f"{getLevelName(current_app.logger.level)} {current_app.logger.level}",
    }, 200
