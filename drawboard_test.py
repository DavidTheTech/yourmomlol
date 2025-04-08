import os
import json
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)

socketio = SocketIO(app)

#Socket stuff
@app.route('/')
def serve_board():
    return render_template('drawboard.html')

@socketio.on('join_room')
def handle_join_room(data):
    room = data['room']
    join_room(room)

@socketio.on('draw_event')
def handle_draw_event(data):
    room = data['room']
    if data['type'] == 'text':
        emit('draw_event', data, room=room, include_self=False)
    elif data['type'] == 'draw':
        emit('draw_event', data, room=room, include_self=False)


if __name__ == '__main__':
    socketio.run(app, debug=False)