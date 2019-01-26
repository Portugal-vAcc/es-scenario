#!/usr/bin/env python3
from random import choice

from . import AIRPORT_SETTINGS

def departure(callsign, departure, destination, stand):
  route, level, fp_direction = AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination]
  random_altitude = choice(AIRPORT_SETTINGS[departure]['GET_FL'][fp_direction][level])
  flight_plan = ':*A:I:B738:400:'+departure+':0000:0000:'+random_altitude+':'+destination+':00:00:0:0::/v/:'

  return '''\
@N:{callsign}:2200:1:{stand}:0:0:0:0:0
$FP{callsign}{flight_plan}
'''.format(
    callsign=callsign,
    stand=stand,
    flight_plan=flight_plan+route
  )

def arrival(callsign, departure, destination, rwy):
  flight_plan, position = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_FPL'][departure])
  route, position_coords, expected_alt = AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][rwy][position]

  return position_coords, '''
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
