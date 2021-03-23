from flask import Blueprint, jsonify
bp_temp = Blueprint("template", __name__)


@bp_temp.route("/test")
def index():
    output = {"msg": "Test output of index"}
    return jsonify(output), 200
