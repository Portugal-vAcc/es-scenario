#!/usr/bin/env python3
"""
Euroscope Sweatbox Scenario Maker

Copyright (C) 2019    Pedro Rodrigues <prodrigues1990@gmail.com>
                                        Tiago Vicente <tmavicente@gmail.com>

This file is part of Euroscope Sweatbox Scenario Maker.

Euroscope Sweatbox Scenario Maker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Euroscope Sweatbox Scenario Maker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Euroscope Sweatbox Scenario Maker. If not, see <http://www.gnu.org/licenses/>.
"""
from random import choice

from . import AIRPORT_SETTINGS

def make_departure(callsign, departure, destination, stand):
    """Generates a random departure flight from a list of flights.

    Args:
        callsign (str): The aircraft callsign.
        departure (str): The ICAO code for the departing airfield
            (ie. the airport we're simulating).
        destination (str): The ICAO code for the flight destination airfield.
        stand (str): The available stand where the flight should be placed.

    Returns:
        str: The flight string to be feed into the scenario file.
    """
    flight_plan = choice(AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination])

    return '''\
@N:{callsign}:2200:1:{stand}:0:0:0:0:0
$FP{callsign}{flight_plan}
'''.format(
        callsign=callsign,
        stand=stand,
        flight_plan=flight_plan
    )

def make_arrival(callsign, departure, destination, rwy):
    """Generates a random arrival flight from a list of flights.

    Args:
        callsign (str): The aircraft callsign.
        departure (str): The ICAO code for the departing airfield.
        destination (str): The ICAO code for the flight destination airfield
            (ie. the airport we're simulating).
        rwy (str): The runway in use.

    Returns:
        str: The flight string to be feed into the scenario file.
    """
    flight_plan, position = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_FPL'][departure])
    route_data = AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][rwy][position]
    route, position_coords, expected_alt = route_data

    return '''
@N:{callsign}:0000:1:{position_coords}:32000:0:50:0:0
$FP{callsign}{flight_plan}
$ROUTE:{route}
DELAY:3:7
REQALT:{position}:{expected_alt}
'''.format(
        callsign=callsign,
        position_coords=position_coords,
        flight_plan=flight_plan,
        route=route,
        position=route.split()[0],
        expected_alt=expected_alt
    )
