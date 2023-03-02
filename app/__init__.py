from peewee import Model, MySQLDatabase, SqliteDatabase, CharField, TextField, DateTimeField

import os
import json
import datetime
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
from app.utils.validators import is_valid_email
from app.utils.exceptions import InvalidEmailException


load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == 'true':
    print("running in testing mode...")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    print("running in production mode...")
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )


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
    return render_template('timeline.html', title='Timeline')


@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html", path=path)


# Create Save and Retrieval Endpoints

# Create POST /api/timeline_post
@app.route('/api/create_timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']

        assert len(name) > 0
        assert len(email) > 0
        assert len(content) > 0

        if not is_valid_email(email):
            raise InvalidEmailException(email)
    except KeyError as e:
        return f"expecting {e.args[0]} parameter in body", 400
    except AssertionError:
        return f"arguments cannot be empty strings", 400
    except InvalidEmailException as e:
        return f"malformed email: {e.args[0]}", 400

    TimelinePost.create(name=name, email=email, content=content)

    return redirect("/timeline")

# Create GET /api/timeline_post


@app.route('/api/get_timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route('/api/delete_timeline_posts', methods=['DELETE'])
def delete_time_line_posts():
    TimelinePost.delete().execute()
    # expect to return empty
    return redirect('/api/get_timeline_post')
