#!/bin/bash

# Activate the virtual environment
python3 -m env venv
source env/bin/activate
pip install -r requirements.txt

# Run the FastAPI app using Uvicorn
uvicorn main:app --reload --host  "0.0.0.0"   --port "8000"
