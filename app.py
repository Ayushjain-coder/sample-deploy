from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    file = open(r'/app.py', 'r').read()
    return exec(file)

if __name__ == '__main__':
   app.run()
