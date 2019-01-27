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
    departures = _generate_departures(icao, rwy)
    arrivals = _generate_arrivals(icao, rwy)

    return '\n'.join([
        *AIRPORT_SETTINGS[icao][rwy],
        *AIRPORT_SETTINGS[icao]['ALL'],
        '\n',
        *departures[:total_departures],
        *arrivals[:total_arrivals]
    ])

def _generate_departures(icao, rwy):
    """Generates a random list of departure flights from a list of flights.

    Args:
        icao (str): The scenario ICAO airfield code.
        rwy (str): The runway in use.

    Returns:
        list: A list of str containing the scenario lines to feed to the output file.
    """
    departures = list()
    callsigns_per_destination = AIRPORT_SETTINGS[icao]['DEPARTURE_CALLSIGNS']
    stands = AIRPORT_SETTINGS[icao]['STANDS']

    shuffle(stands)

    for destination in callsigns_per_destination:
        for callsign in callsigns_per_destination[destination]:
            if stands:
                departures.append(flight.make_departure(
                    callsign,
                    icao,
                    destination,
                    stands.pop(),
                    rwy
                ))

    shuffle(departures)

    return departures

def _generate_arrivals(icao, rwy):
    """Generates a random list of arrival flights from a list of flights.

    Args:
        icao (str): The scenario ICAO airfield code.
        rwy (str): The runway in use.

    Returns:
        list: A list of str containing the scenario lines to feed to the output file.
    """
    arrivals = list()
    callsigns_per_departure = AIRPORT_SETTINGS[icao]['ARRIVAL_CALLSIGNS']

    for departure in callsigns_per_departure:
        for callsign in callsigns_per_departure[departure]:
            arrivals.append(flight.make_arrival(
                callsign,
                departure,
                icao,
                rwy
            ))

    shuffle(arrivals)

    return arrivals
