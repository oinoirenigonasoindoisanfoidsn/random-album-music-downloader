#!/bin/bash

# Check if the virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    # Activate the virtual environment
    source .venv/bin/activate
fi

# Run the Python script
python main-new.py

# Deactivate the virtual environment
deactivate
