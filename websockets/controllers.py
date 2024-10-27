import base64
from __main__ import socketio

from flask_socketio import emit, rooms, join_room


# WebSocket endpoint for joining a room
@socketio.on("join_room")
def handle_join_room(data):
    room_id = data["room_id"]
    join_room(room_id)
    emit("room_joined", {"message": f"You have joined room {room_id}"})


# WebSocket endpoint for receiving and broadcasting the answer in a room
@socketio.on("send_answer")
def handle_send_answer(data):
    print(data)
    room_id = data.get("room_id")
    answer = data.get("answer")

    # Adding current device in room
    join_room(room_id)

    if room_id and answer:
        # Send the answer to everyone in the room, including the sender
        emit(
            "receive_answer",
            {"answer": answer},
            room=room_id,
        )
    else:
        emit("error", {"message": "Room ID or answer not provided."})


@socketio.on("connection_successfully")
def connection_successful(data):
    room_id = data["room_id"]
    print(room_id)
    emit("connected_with_peer", room=room_id, include_self=False)
