#!/usr/bin/env python3
from random import choice

from . import AIRPORT_SETTINGS

def departure(callsign, departure, destination, stand):
  flight_plan = choice(AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination])

  return '@N:{callsign}:2200:1:{stand}:0:0:0:0:0\n$FP{callsign}{flight_plan}\n'.format(
    callsign=callsign,
    stand=stand,
    flight_plan=flight_plan
  )