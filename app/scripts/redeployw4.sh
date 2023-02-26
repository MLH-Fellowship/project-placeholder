#!/bin/bash

# cd into your project folder
cd "~/repos/project-placeholder";

# make sure the git repo inside VPS has lastest changes
git fetch && git reset origin/main --hard;

# Enter the python virtual environment and install python dependencies
source venv/bin/activate && pip install -q -r requirements.txt

# Restart myportfolio service
systemctl daemon-reload
systemctl restart myportfolio
