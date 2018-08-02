#!/usr/bin/env bash

cd ../
export FLASK_APP=toy/__init__.py
export FLASK_DEBUG=TRUE
flask run --port=5000 --host=0.0.0.0