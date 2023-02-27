#!/bin/bash

tmux kill-server;

# cd into your project folder
cd "~/repos/project-placeholder";

# make sure the git repo inside VPS has the latest changes from main
git stash && git switch main && git fetch --all && git reset --hard origin/main;

# Enter the python virtual environment and install python dependencies
# Start a new detached Tmux session that goes to the project directory, enters the python virtual environment and starts the Flask server.

tmux new-session -d -s process "cd ~/repos/project-placeholder && source venv/bin/activate && pip install -q -r requirements.txt && flask run --host=0.0.0.0";