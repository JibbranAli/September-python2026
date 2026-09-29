from flask import Flask

app=Flask(__name__)

@app.route("/home")
def home():
    return "HELLO I AM HOME PAGE"

@app.route("/index")
def index():
    return "I am index page"

@app.route("/search")
def search():
    return "I am Search PAGE"

app.run(debug=True)