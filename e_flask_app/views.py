from flask import Blueprint, current_app, render_template

bp = Blueprint("views", __name__)


@bp.route("/")
def index():
    greeting="Hello, World!"
    current_app.logger.info(f'{greeting=}')
    return render_template("index.html", greeting=greeting)
