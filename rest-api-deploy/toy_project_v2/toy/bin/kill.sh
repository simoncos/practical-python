#!/usr/bin/env bash

# Process Name
PROCESS=toyapi:app

# Kill previous process
for pid in $(ps aux | grep $PROCESS | awk '{print $2}')
do
  if [ "$pid" != "" ]
  then
    echo "killing $pid"
    kill -9 $pid
  fi
done