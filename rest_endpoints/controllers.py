import uuid

from flask import Blueprint

rest_endpoints = Blueprint("rest_endpoints", __name__, url_prefix="/rest_endpoints")


@rest_endpoints.route("/create_room", methods=["GET"])
def create_room():
    room_id = str(uuid.uuid4())

    # TODO: Check if already room_id exists

    return {"room_id": room_id}, 200
