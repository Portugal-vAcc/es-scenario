#!/usr/bin/env python3
"""
Euroscope Sweatbox Scenario Maker

Copyright (C) 2019  Pedro Rodrigues <prodrigues1990@gmail.com>
                    Tiago Vicente <tmavicente@gmail.com>

This file is part of Euroscope Sweatbox Scenario Maker.

Euroscope Sweatbox Scenario Maker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Euroscope Sweatbox Scenario Maker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Euroscope Sweatbox Scenario Maker. If not, see <http://www.gnu.org/licenses/>.
"""
from random import shuffle
from collections import defaultdict

from . import AIRPORT_SETTINGS
from . import flight

def make_scenario(icao, rwy, total_departures, total_arrivals):
    """Generates a Euroscope Sweatbox scenario for the given icao and active rwy, with random
    arrivals and departures.

    Args:
        icao (str): The scenario ICAO airfield code.
        rwy (str): Runway in use.
        total_departures (int, optional): Total departing aircraft.
        total_arrivals (int, optional): The scenario ICAO airfield code.

    Returns:
        list: A list of str containing the scenario lines to feed to the output file.
    """
    departures = _generate_departures(icao)
    arrivals = _generate_arrivals(icao, rwy)

    return '\n'.join([
        *AIRPORT_SETTINGS[icao][rwy],
        *AIRPORT_SETTINGS[icao]['ALL'],
        '\n',
        *departures[:total_departures],
        *arrivals[:total_arrivals]
    ])

def _generate_departures(icao):
    """Generates a random list of departure flights from a list of flights.

    Args:
        icao (str): The scenario ICAO airfield code.

    Returns:
        list: A list of str containing the scenario lines to feed to the output file.
    """
    departures = list()
    callsigns_per_destination = AIRPORT_SETTINGS[icao]['DEPARTURE_CALLSIGNS']
    stands = AIRPORT_SETTINGS[icao]['STANDS']

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
