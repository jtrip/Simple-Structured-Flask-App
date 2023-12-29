from logging import getLevelName
from datetime import datetime, timezone
from flask import current_app, session, flash, redirect, url_for, request
from app.main import bp


@bp.route("/clear-session", methods=["GET"])
def clear_session():
    session.clear()
    flash("Session Cleared", "success")
    return redirect(url_for("main.index_view"))


@bp.route("/json/client_ip", methods=["GET"])
def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    current_app.logger.info(f"{client_ip=}")
    return {"client_ip": client_ip}, 200


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
