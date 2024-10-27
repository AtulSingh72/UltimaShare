import importlib

from flask import Flask
from flask_socketio import SocketIO

from rest_endpoints.controllers import rest_endpoints
from share_page.controllers import share_page

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

importlib.import_module("websockets.controllers")

app.register_blueprint(share_page)
app.register_blueprint(rest_endpoints)


if __name__ == "__main__":
    socketio.run(app, debug=True)
