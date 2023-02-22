import os
import json

from flask import Flask, render_template, request
from peewee import MySQLDatabase

from app.database.lib import Database
from app.database.models.post import Post


app = Flask(__name__)
database = Database.get_instance()

database.connect()
database.create_tables([Post])
print(database.get_tables())

@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title="Week 1 - Team Portfolio", url=os.getenv("URL"), users=data["users"])


@app.route('/map')
def map_view():
    return render_template('map.html')


@app.route('/aboutme')
def aboutme():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('aboutme.html', title="Week 1 - Team Portfolio", url=os.getenv("URL"), users=data["users"])


@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html", path=path)
