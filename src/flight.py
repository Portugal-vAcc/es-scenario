#!/usr/bin/env python3
from random import choice

from . import AIRPORT_SETTINGS

def departure(callsign, departure, destination, stand):
  flight_plan = choice(AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination])

  return '''\
@N:{callsign}:2200:1:{stand}:0:0:0:0:0
$FP{callsign}{flight_plan}
'''.format(
    callsign=callsign,
    stand=stand,
    flight_plan=flight_plan
  )

def arrival(callsign, departure, destination, rwy):
  flight_plan, position = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_FPL'][departure])
  route, position_coords, expected_alt = AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][rwy][position]

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
    position=position,
	  expected_alt=expected_alt
  )
