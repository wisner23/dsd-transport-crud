from flask import Blueprint, request, abort, jsonify
from app import db
from .transport_model import Transport
from .transport_validator import validate_transport


mod_transport = Blueprint("mod_transport", __name__, url_prefix="/transport")


@mod_transport.route("/", methods=["POST"])
def create_new_transport():

    data = request.json

    if not data:
        abort(400)

    if not validate_transport(data):
        raise Exception("Invalid parameters")

    transport = Transport(name=data["name"])

    try:
        db.session.add(transport)
        db.session.commit()

    except Exception as e:
        raise Exception("A Database exception occurred while we are trying to insert data")

    return jsonify({"status": "created"}), 200


@mod_transport.route("/<int:transport_id>", methods=["PUT"])
def update_transport(transport_id):

    data = request.json

    if not data:
        abort(400)

    if not validate_transport(data):
        raise Exception("Invalid parameters")

    transport = Transport.query.get(transport_id)

    if not transport:
        abort(404)

    try:
        transport.name = data["name"]
        db.session.commit()
    except Exception as e:
        raise Exception("A Database exception occurred while we are trying to update data")

    return jsonify({"status": "updated"}), 200


@mod_transport.route("/<int:transport_id>", methods=["DELETE"])
def remove_transport(transport_id):

    transport = Transport.query.get(transport_id)

    if not transport:
        abort(404)

    try:

        db.session.delete(transport)
        db.session.commit()
    except:
        raise Exception("A Database exception occurred while we are trying to delete data")

    return jsonify({"status": "removed"}), 200


@mod_transport.route("/", methods=["GET"])
def read_transport():
    transports = Transport.query.all()

    schema_transport = [{"id": x.id, "name": x.name} for x in transports]

    return jsonify(transports=schema_transport)


@mod_transport.route("/<transport_id>", methods=["GET"])
def read_transport_by_id(transport_id):
    transport = Transport.query.get(transport_id)

    data = {"id": transport.id, "name": transport.name}

    return jsonify(data)
