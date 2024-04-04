#!/bin/bash

cd /home/surya/evcharger

# Set the path to your virtual environment
VENV_PATH="/home/surya/evcharger/env"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

export DISPLAY=:0.0

# Run your Python script
python /home/surya/evcharger/main.py

# Deactivate the virtual environment
deactivate