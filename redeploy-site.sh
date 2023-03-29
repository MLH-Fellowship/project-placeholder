#!/bin/bash


# Docker Container Deployment:

# cd into your project folder
cd "~/project-placeholder";

# make sure the git repo inside VPS has the latest changes from main
git fetch && git reset origin/main --hard

# Run docker spin containers down to prevent out of memory issues on our VPS instances when building in the next step
docker compose -f docker-compose.prod.yml down

# Run
docker compose -f docker-compose.prod.yml up -d --build


# tmux kill-server;

# cd into your project folder
# cd "~/repos/project-placeholder";

# make sure the git repo inside VPS has the latest changes from main
# git fetch && git reset origin/main --hard

# Enter the python virtual environment and install python dependencies
# "git stash && git switch main && git fetch --all && git reset --hard origin/main && source python3-virtualenv/bin/activate && pip install -r requirements.txt && systemctl daemon-reload && systemctl restart myportfolio && flask run --host=0.0.0.0"


# Start a new detached Tmux session that goes to the project directory, enters the python virtual environment and starts the Flask server.


# tmux new-session -d -s process "cd ~/repos/project-placeholder && source venv/bin/activate && pip install -q -r requirements.txt && flask run --host=0.0.0.0";


# creating new session:
# tmux new

# python -m ven python3-virutalenv

# source python3-virtualenv/bin/activate

# pip install -r requirements.txt

# flask run --host=0.0.0.0

# cmd-B + D

#!/bin/bash

# tmux kill-server;

# Enter the python virtual environment and install python dependencies
# "git stash && git switch main && git fetch --all && git reset --hard origin/main && source python3"


# Start a new detached Tmux session that goes to the project directory, enters the python virtual e>


# tmux new-session -d -s process "cd ~/repos/project-placeholder && source venv/bin/activate && pip>


# creating new session:
# tmux new

# python -m ven python3-virutalenv

