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
  flight_plan, entry_point = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_FPL'][departure])
  position = AIRPORT_SETTINGS[destination]['ARRIVAL_POSITIONS'][entry_point]
  expectedAlt = AIRPORT_SETTINGS[destination]['ARRIVAL_STARS'][rwy][departure]
  route = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][entry_point])

  return '''
@N:{callsign}:0000:1:{position}:32000:0:50:0:0
$FP{callsign}{flight_plan}
$ROUTE:{route}
DELAY:3:7
REQALT:{expectedAlt}
'''.format(
    callsign=callsign,
    position=position,
    flight_plan=flight_plan,
    route=route,
	expectedAlt=expectedAlt
  )
