#!/bin/bash

tmux kill-server;

# cd into your project folder
cd "~/repos/project-placeholder";

# make sure the git repo inside VPS has the latest changes from main
git stash && git switch main && git fetch --all && git reset --hard origin/main;

# Enter the python virtual environment and install python dependencies
# Start a new detached Tmux session that goes to the project directory, enters the python virtual environment and starts the Flask server.

tmux new-session -d -s process "cd ~/repos/project-placeholder && source venv/bin/activate && pip install -q -r requirements.txt && flask run --host=0.0.0.0";

# root@146.190.240.33

# tmux new

# python -m ven python3-virutalenv

# source python3-virtualenv/bin/activate

# pip install -r requirements.txt

# flask run --host=0.0.0.0

# cmd-B + D