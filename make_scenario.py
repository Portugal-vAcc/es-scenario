#!/usr/bin/env python3
from random import shuffle, choice

from src.airport import Airport

# program options
AIRPORT = 'LPPR'
RUNWAY = '35'
TOTAL_DEPARTURES = 7

# program
with open('output.txt', 'w') as file:
  scenario = Airport(AIRPORT, RUNWAY, total_departures=5)
  file.write(str(scenario))

file.close()
