from flask import Flask
import eel

app = Flask(__name__)

@app.route('/')
def run_script():
    eel.init(r'\web', allowed_extensions=['.js', '.html'])
    try:
        eel.start('index.html', mode='chrome',
                                host='localhost',
                                port=27005,
                                block=False,
                                size=(350, 480),
                                position=(10,100),
                                disable_cache=True,
                                close_callback=ChatBot.close_callback)
        ChatBot.started = True
        while ChatBot.started:
            try:
                eel.sleep(10.0)
            except:
                #main thread exited
                break

    except:
        pass

if __name__ == "__main__":
    app.run(debug=True)
