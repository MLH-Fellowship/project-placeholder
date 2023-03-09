#!/usr/bin/env bash

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
flask run --host=0.0.0.0
