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

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv(
        "MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_HOST"), port=3306)

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
mydb.close()


@app.before_first_request
def _db_connect():
    mydb.connect()


@app.teardown_request
def _db_close(exc):
    if not mydb.is_closed():
        mydb.close()


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
    # Try and retrieve the 'name' field from the request form
    try:
        name = request.form['name']
    # If it doesn't exist, KeyError will be raised and we'll return an error
    except KeyError:
        return 'Invalid name', 400

    try:
        content = request.form['content']
        if content == "" or content == None:
            return 'Invalid content', 400
    except:
        return 'Invalid content', 400

    try:
        email = request.form['email']
        if "@" not in email and "." not in email or email == "" or email == None or len(email) < 3:
            return 'Invalid email', 400
    except:
        return 'Invalid email', 400

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
