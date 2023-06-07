#!/bin/bash

# Activate the virtual environment
source env/bin/activate

# Run the FastAPI app using Uvicorn
uvicorn api:app --reload
