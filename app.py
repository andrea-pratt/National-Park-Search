from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET',"POST"])
def home():
    return render_template("index.html")


@app.route("/display_saved_parks", methods=['GET',"POST"])
def bookmarked():
    return render_template("bookmarked.html")


