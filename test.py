from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "This is a test API!"


if __name__ == '__main__':
    app.run(debug=True, port=12347)