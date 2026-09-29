from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello I am Home "
@app.route("/index")
def index():
    return "I am index page"
@app.route("/search")
def search():
    return "I am Searchpage" 


app.run()