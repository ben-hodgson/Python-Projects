#!/bin/bash

while true; do
    python air-mon.py
    exit_code=$?
    if [ $exit_code -eq 0 ]; then
        echo "Program exited successfully."
        break
    else
        echo "Program exited with error code $exit_code. Restarting..."
        sleep 1
    fi
done