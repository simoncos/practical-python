#!/usr/bin/env bash

# Kill previous process
bash kill.sh

# Start Process
cd ../
gunicorn -c conf/gunicorn.conf toy:app # toy/__init__.py | app = Flask(__name__)