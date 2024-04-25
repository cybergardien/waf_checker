#!/bin/bash

# Navigate to the project directory (replace with your actual project path)
cd "$(dirname "$0")"

# Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Python script with the path to the CSV as an argument
python -m src.waf_checker data/urls.csv

# Deactivate the virtual environment
deactivate
