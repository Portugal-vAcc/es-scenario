#!/usr/bin/env python3
from random import choice

from . import AIRPORT_SETTINGS

class Flight():
  def __init__(self, callsign, departure, destination):
    self.callsign = callsign
    self.flight_plan = choice(AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination])
    self.stand = '41.237411:-8.675570'

  def __str__(self):
    return '@N:{callsign}:2200:1:{stand}:0:0:0:0:0\n$FP{callsign}{flight_plan}\n'.format(
      callsign=self.callsign,
      stand=self.stand,
      flight_plan=self.flight_plan
    )
