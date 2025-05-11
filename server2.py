from flask import Flask, request, jsonify, send_file
import socket
import os
import ctypes
from mss import mss

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
capturebox = {"left":0, "top":0, "width":screensize[0], "height":screensize[1]}

app = Flask(__name__)
    
@app.route("/Screenshot", methods=["POST"])
def post():
    print("Received POST request")
    with mss() as sct:
        filename = sct.shot(mon=-1, output='c:/WINDOWS/Temp/screenshot.png')
    return send_file(filename, mimetype="image/png")

if __name__ == "__main__":
    app.run()