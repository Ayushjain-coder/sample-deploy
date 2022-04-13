from flask import Flask, render_template
import cv2
import os, sys

#instatiate flask app  
app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
    camera = cv2.VideoCapture(0)
    return render_template('index1.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
    
camera.release()
cv2.destroyAllWindows()     
