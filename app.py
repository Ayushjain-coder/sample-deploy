from flask import Flask, render_template, Response, request
import cv2
import os, sys

#instatiate flask app  
app = Flask(__name__, template_folder='./templates')

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run()
    
camera.release()
cv2.destroyAllWindows()     
