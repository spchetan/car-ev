#!/bin/bash

# Train the model if it doesn't exist
if [ ! -f "ev_range_model.pkl" ]; then
    echo "Training model..."
    python train_model.py
fi

# Start the application with gunicorn
gunicorn --bind 0.0.0.0:$PORT --timeout 600 --workers 2 app:app
