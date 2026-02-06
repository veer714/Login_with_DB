#!/bin/bash
# Activate virtual environment
source venv/bin/activate

# Run database setup to be safe
python3 setup_db.py

# Run the application
python3 app.py
