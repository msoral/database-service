from flask import Blueprint, current_app
bp_temp = Blueprint("template", __name__, url_prefix="/template")


@bp_temp.route("/")
def index():
    return
