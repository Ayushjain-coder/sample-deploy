from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)

ui = FlaskUI(app, host='localhost', port=27005, width=350, height=480, maximized=True, fullscreen=True)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    ui.run(debug=True)
