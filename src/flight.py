#!/usr/bin/env python3
from random import choice
import random

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
  expected_alt = AIRPORT_SETTINGS[destination]['ARRIVAL_STARS'][rwy][departure]
  route = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][rwy][entry_point])
  start_delay = random.randint(0,30)

  return '''
@N:{callsign}:0000:1:{position}:32000:0:50:0:0
$FP{callsign}{flight_plan}
$ROUTE:{route}
START:{start_delay}
DELAY:2:5
REQALT:{expected_alt}
'''.format(
    callsign=callsign,
    position=position,
    flight_plan=flight_plan,
    route=route,
    expected_alt=expected_alt,
	start_delay=start_delay
  )
