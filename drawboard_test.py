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
    points = data['points']
    pen_size = data['penSize']
    color = data['color']

    emit('draw_event', { 'points': points, 'penSize': pen_size, 'color': color }, room=room, include_self=False)


if __name__ == '__main__':
    socketio.run(app, debug=False)