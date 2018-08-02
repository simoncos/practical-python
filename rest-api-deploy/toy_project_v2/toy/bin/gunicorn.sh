#!/usr/bin/env bash

# Kill previous process
bash kill.sh

# Start Process
cd ../
gunicorn -c conf/gunicorn_conf.py toy:syntacticapp # toy/__init__.py | app = Flask(__name__)