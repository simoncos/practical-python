#!/usr/bin/env bash

echo "Checking dependencies with pip..."
pip install -r ../deploy/docker/requirements.txt

bash gunicorn.sh
