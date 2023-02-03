import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title="Week 1 - Team Portfolio", url=os.getenv("URL"), users=data["users"], pages=data["pages"])


// TODO: implement /map route

// TODO: implement /aboutme route


@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html", path=path)
