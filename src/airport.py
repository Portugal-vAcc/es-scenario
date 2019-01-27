#!/usr/bin/env python3
from random import shuffle
from collections import defaultdict

from . import AIRPORT_SETTINGS
from . import flight

class Airport():
  def __init__(self, icao, rwy, total_departures=1, total_arrivals=0):
    self.icao = icao
    self.rwy = rwy
    self.total_departures = total_departures
    self.total_arrivals = total_arrivals

    self.departures = list()
    self.arrivals = list()

    self._generate_departures()
    self._generate_arrivals()

  def _generate_departures(self):
    callsigns_per_destination = AIRPORT_SETTINGS[self.icao]['DEPARTURE_CALLSIGNS']
    stands = AIRPORT_SETTINGS[self.icao]['STANDS']

    self.departures = list()
    shuffle(stands)

    for destination in callsigns_per_destination:
      for callsign in callsigns_per_destination[destination]:
        if (len(stands) > 0):
          self.departures.append(flight.departure(
            callsign,
            self.icao,
            destination,
            stands.pop(),
			self.rwy
          ))

    shuffle(self.departures)
	
    def get_0():
      return 0
    counter = defaultdict(get_0)
    d = []
    for spawn, departure in self.departures:
      d.append(departure + 'START:%s' % (counter[spawn] * 1))
      counter[spawn] = counter[spawn] + 1
    self.departures = d
	
  def _generate_arrivals(self):
    callsigns_per_departure = AIRPORT_SETTINGS[self.icao]['ARRIVAL_CALLSIGNS']

    for departure in callsigns_per_departure:
      for callsign in callsigns_per_departure[departure]:
        self.arrivals.append(flight.arrival(
          callsign,
          departure,
          self.icao,
          self.rwy
        ))
    
    shuffle(self.arrivals)

    def get_0():
      return 0
    counter = defaultdict(get_0)
    a = []
    for spawn, arrival in self.arrivals:
      a.append(arrival + 'START:%s' % (counter[spawn] * 4))
      counter[spawn] = counter[spawn] + 1
    self.arrivals = a



  def __str__(self):
    return '\n'.join([
      *AIRPORT_SETTINGS[self.icao][self.rwy],
	  '\n',
      *AIRPORT_SETTINGS[self.icao]['ALL'],
	  '\n',
	  *AIRPORT_SETTINGS[self.icao]['HOLDS'][self.rwy],
      '\n',
      *self.departures[:self.total_departures],
      *self.arrivals[:self.total_arrivals]
    ])
