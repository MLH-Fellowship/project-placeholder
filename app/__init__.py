import os
import json
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)
CORS(app)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv(
    "MYSQL_USER"), password="", host=os.getenv("MYSQL_HOST"), port=3306)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


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


@app.route('/timeline')
def timeline():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), users=data["users"])


@app.route('/api/timeline_post', methods=['POST'])
@cross_origin()
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(
        name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
@cross_origin()
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html", path=path)
