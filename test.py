import os
import json
from flask import Flask, render_template, send_from_directory, send_file, current_app
from flask_socketio import SocketIO, emit

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static')

socketio = SocketIO(app)

#Socket stuff
@app.route('/drawboard')
def serve_board():
    return render_template('drawboard.html')

@socketio.on('draw_event')
def handle_draw_event(data):
    emit('draw_event', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=False)
