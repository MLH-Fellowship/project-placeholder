#!/bin/bash

cd ~/repos/project-placeholder;

# make sure the git repo inside VPS has lastest changes
git stash && git switch main && git fetch --all && git reset --hard origin/main;

# (Let's first spin containers down to prevent out of memory issues on our VPS instances when building in the next step)
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build --detach