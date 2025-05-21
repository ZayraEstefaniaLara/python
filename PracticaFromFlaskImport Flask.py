from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hola mundo"

if __name__ == '__main__':
    app.run(host = '10.2.81.175', port=5000)