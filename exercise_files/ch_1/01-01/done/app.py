from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/super_simple")
def super_simple():
    return "Hello World from the Planetary API. boo yah"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
