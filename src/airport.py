#!/usr/bin/env python3
from random import shuffle

from . import AIRPORT_SETTINGS
from .flight import Flight

class Airport():
  def __init__(self, icao, rwy, total_departures=1):
    self.icao = icao
    self.rwy = rwy
    self.total_departures = total_departures

    self.departures = list()

    self._generate_departures()

  def _generate_departures(self):
    callsigns_per_destination = AIRPORT_SETTINGS[self.icao]['DEPARTURE_CALLSIGNS']
    stands = AIRPORT_SETTINGS[self.icao]['STANDS']

    self.departures = list()
    shuffle(stands)

    for destination in callsigns_per_destination:
      for callsign in callsigns_per_destination[destination]:
        departure = Flight(callsign, self.icao, destination)
        if (len(stands) > 0):
          departure.stand = stands.pop()
          self.departures.append(str(departure))

    shuffle(self.departures)
  
  def __str__(self):
    return '\n'.join([
      AIRPORT_SETTINGS[self.icao][self.rwy],
      *AIRPORT_SETTINGS[self.icao]['ALL'],
      '\n',
      *self.departures[:self.total_departures],
    ])