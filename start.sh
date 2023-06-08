#!/bin/bash

# Activate the virtual environment
source env/bin/activate

# Run the FastAPI app using Uvicorn
uvicorn main:app --reload --host  "0.0.0.0"   --port "8000"
