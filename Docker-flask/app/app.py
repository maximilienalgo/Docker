import sys, os
from flask import Flask

app = Flask(__name__)

#route for home page
@app.route("/")
def index():
    return "hello BG"

@app.route("/name/<name>")
def name(name):
    return "Hello %s" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)


