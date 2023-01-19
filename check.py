import datetime
import os
import cv2
from flask import redirect, session, url_for

camera=cv2.VideoCapture(0)

def gen_frames():
    global capture
    global img
    
    print('[DEBUG] gen_frames: start')

    while True:
        success, img = camera.read()
        
        if not success:
            break
        
        if capture:
            capture = False

            now = datetime.datetime.now()
            filename = "shot_{}.png".format(str(now).replace(":",''))
            path = os.path.sep.join(['shots', filename])

            print('[DEBUG] capture:', path)

            cv2.imwrite(path, img)

        frame = cv2.imencode('.jpg', img)[1].tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
