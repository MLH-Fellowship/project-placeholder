#!/bin/bash

# cd into your project folder
cd "~/repos/project-placeholder";

# make sure the git repo inside VPS has lastest changes
git fetch && git reset origin/main --hard;

# (Let's first spin containers down to prevent out of memory issues on our VPS instances when building in the next step)
docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build
