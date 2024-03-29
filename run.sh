#!/bin/bash

# Find and run Python files starting with "odds"
for file in odds*.py; do
    python3 "$file"
done

# Run the remaining four scripts in order
python3 MATCHFINDER.py
python3 betfinder.py
python3 multiplierfinder.py
python3 BESTBETS.py
