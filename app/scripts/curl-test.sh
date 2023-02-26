#!bin/bash

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'name=test&email=test&content=test' http://localhost:5000/api/create_timeline_post
curl -X GET http://localhost:5000/api/get_timeline_post | jq '.timeline_posts[0]'