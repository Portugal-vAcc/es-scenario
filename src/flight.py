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

def departure(callsign, departure, destination, stand, rwy):
  route, level, fp_direction, sidfix = choice(AIRPORT_SETTINGS[departure]['DEPARTURE_FPL'][destination])
  random_altitude = choice(AIRPORT_SETTINGS[departure]['GET_FL'][fp_direction][level])
  flight_plan = ':*A:I:B738:400:'+departure+':0000:0000:'+random_altitude+':'+destination+':00:00:0:0::/v/:'
  sidroute, expected_alt = AIRPORT_SETTINGS[departure]['DEPARTURE_ROUTES'][rwy][sidfix]

  return sidfix, '''
@N:{callsign}:2200:1:{stand}:0:0:0:0:0
$FP{callsign}{flight_plan}{route}
$ROUTE:{sidroute}
REQALT:{sidfix}:{expected_alt}
'''.format(
    callsign=callsign,
    stand=stand,
    flight_plan=flight_plan,
	route=route,
	sidroute=sidroute,
	sidfix=sidfix,
	expected_alt=expected_alt
  )

def arrival(callsign, departure, destination, rwy):
  flight_plan_route, position, level, fp_direction = choice(AIRPORT_SETTINGS[destination]['ARRIVAL_FPL'][departure])
  route, position_coords, expected_alt = AIRPORT_SETTINGS[destination]['ARRIVAL_ROUTES'][rwy][position]
  random_altitude = choice(AIRPORT_SETTINGS[destination]['GET_FL'][fp_direction][level])
  flight_plan = ':*A:I:B738:364:'+departure+':0000:0000:'+random_altitude+':'+destination+':00:00:0:0::/v/:'

  #Preve planos de voo inferiores à altitude de cruzeiro para LOW_LEVEL FP's
  if (random_altitude < expected_alt and level == 'LOW_LEVEL'):
	  expected_alt = random_altitude
  #Prever a mesma situação para HIGH_LEVEL
  if (random_altitude < expected_alt and level == 'HIGH_LEVEL'):
	  random_altitude = max(AIRPORT_SETTINGS[destination]['GET_FL'][fp_direction][level])


  return position_coords, '''
@N:{callsign}:0000:1:{position_coords}:{random_altitude}:0:50:0:0
$FP{callsign}{flight_plan}{flight_plan_route}
$ROUTE:{route}
DELAY:3:7
REQALT:{position}:{expected_alt}
'''.format(
    callsign=callsign,
    position_coords=position_coords,
    flight_plan=flight_plan,
	flight_plan_route=flight_plan_route,
    route=route,
    position=route.split()[0],
    expected_alt=expected_alt,
	random_altitude=random_altitude
  )
