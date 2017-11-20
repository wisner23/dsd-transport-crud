from flask import Blueprint, request, abort, jsonify
from app import db
from .transport_line_model import TransportLine


mod_transport_line = Blueprint("mod_transport_line", __name__, url_prefix="/transport-line")


@mod_transport_line.route("/", methods=["POST"])
def create_new_transport_line():

    data = request.json

    if not data:
        abort(400)

    transport_line = TransportLine(name=data["name"], hour=data["hour"],
                                   passed=data["passed"], transport_id=data["transport_id"])

    try:
        db.session.add(transport_line)
        db.session.commit()

    except Exception as e:
        raise Exception("A Database exception occurred while we are trying to insert data")

    return jsonify({"status": "created"}), 200


@mod_transport_line.route("/<int:transport_line_id>", methods=["PUT"])
def update_transport_line(transport_line_id):

    data = request.json

    if not data:
        abort(400)

    transport_line = TransportLine.query.get(transport_line_id)

    if not transport_line:
        abort(404)

    try:
        transport_line.name = data["name"]
        db.session.commit()
    except Exception as e:
        raise Exception("A Database exception occurred while we are trying to update data")

    return jsonify({"status": "updated"}), 200


@mod_transport_line.route("/<int:transport_line_id>", methods=["DELETE"])
def remove_transport_line(transport_line_id):
    transport_line = TransportLine.query.get(transport_line_id)

    if not transport_line:
        abort(404)

    try:

        db.session.delete(transport_line)
        db.session.commit()
    except:
        raise Exception("A Database exception occurred while we are trying to delete data")

    return jsonify({"status": "removed"}), 200


@mod_transport_line.route("/", methods=["GET"])
def read_transport_line():
    transport_lines = TransportLine.query.all()
    schema_transport = [{"id": x.id, "name": x.name, "transport_id": x.transport_id} for x in transport_lines]

    return jsonify(transport_lines=schema_transport)


@mod_transport_line.route("/transport/<int:transport_id>", methods=["GET"])
def read_transport_line_by_transport_id(transport_id):
    transport_lines = TransportLine.query.filter_by(transport_id=transport_id).all()
    schema_transport = [{"id": x.id, "name": x.name, "hour": x.hour, "passed": x.passed,
                         "transport_id": x.transport_id} for x in transport_lines]

    return jsonify(transport_lines=schema_transport)


@mod_transport_line.route("/<int:transport_line_id>", methods=["GET"])
def read_transport_line_by_id(transport_line_id):
    transport_line = TransportLine.query.get(transport_line_id)

    data = {"id": transport_line.id, "name": transport_line.name, "transport_id": transport_line.transport_id}

    return jsonify(data)
