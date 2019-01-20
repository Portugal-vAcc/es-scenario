#!/usr/bin/env python3
from random import shuffle, choice

# program options
AIRPORT = 'LPPR'
RUNWAY = '35'
TOTAL_DEPARTURES = 7

# program defaults
LPPR_SETTINGS = {
  '35': 'ILS35:N041.13.59,934:W008.40.38,582:352',
  '17': None,
  'ALL': [
    'AIRPORT_ALT:0'
  ],
  'DEPARTURE_CALLSIGNS': {
    'LPPT': ['SWT230P', 'RYR2093', 'RYR2095', 'RYR2695', 'TAP1921', 'TAP1923', 'TAP1925',],
    'LPFR': ['RYR5486',],
  },
  'DEPARTURE_FPL': {
    # all lines start with $FP{callsign}
    'LPPT': [':*A:I:B738:210:LPPR:0000:0000:0:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX', ':*A:I:B738:230:LPPR:0000:0000:0:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX'],
    'LPFR': [':*A:I:B738:210:LPPR:0000:0000:0:LPFR:00:00:0:0::/v/:MANIK A5 ODEMI',],
  }
}
AIRPORT_SETTINGS = {
  'LPPR': LPPR_SETTINGS,
}
def make_settings():
  return '\n'.join([
    AIRPORT_SETTINGS[AIRPORT][RUNWAY],
    *AIRPORT_SETTINGS[AIRPORT]['ALL'],
    '\n'
  ])

def make_departures():
  departures = list()
  for dest in AIRPORT_SETTINGS[AIRPORT]['DEPARTURE_CALLSIGNS']:
    for callsign in AIRPORT_SETTINGS[AIRPORT]['DEPARTURE_CALLSIGNS'][dest]:
      departures.append(''.join([
        '@N:', callsign, ':2200:1:41.237411:-8.675570:0:0:0:0:0'
        '\n',
        '$FP', callsign, choice(AIRPORT_SETTINGS[AIRPORT]['DEPARTURE_FPL'][dest]),
        '\n'
      ]))

  shuffle(departures)
  return '\n'.join(departures[:TOTAL_DEPARTURES])

# program
with open('output.txt', 'w') as file:
  file.write(make_settings())
  file.write(make_departures())

file.close()