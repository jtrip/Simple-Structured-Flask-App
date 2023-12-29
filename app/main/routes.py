from flask import current_app, render_template
from app.main import bp


@bp.route("/")
def index_view():
    greeting = "Hello, World!"
    current_app.logger.info(f"{greeting=}")
    return render_template("index.html", greeting=greeting)
