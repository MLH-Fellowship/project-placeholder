#!/bin/bash

# Reset environment and update project.
tmux kill-server
cd "~/project-placeholder"
git fetch && git reset origin/main --hard

# Boot process.
tmux new-session -d -s process "cd ~/project-placeholder && source venv/bin/activate && pip install -q -r requirements.txt && flask run --host=0.0.0.0";