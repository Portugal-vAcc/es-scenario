#!/usr/bin/env python3
import json

with open('data/airports.json', 'r') as file:
    AIRPORT_SETTINGS = json.loads(file.read())
