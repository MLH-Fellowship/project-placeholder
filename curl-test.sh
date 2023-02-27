#!/bin/bash

# make a random post
RANDOM_POST="name=Anshaal&email=anshaalhussain@gmail.com&content=Just Added Database to my portfolio site!"

# send POST request
curl -X POST "http://localhost:5000/api/timeline_post" -d $RANDOM_POST

# test GET response
curl "http://localhost:5000/api/timeline_post"