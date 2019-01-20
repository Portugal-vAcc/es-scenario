#!/usr/bin/env python3

_LPPR_SETTINGS = {
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
    'LPPT': [':*A:I:B738:0:LPPR:0000:0000:0:LPPT:00:00:0:0::/v/:MANIK DCT XAMAX',],
    'LPFR': [':*A:I:B738:0:LPPR:0000:0000:0:LPFR:00:00:0:0::/v/:MANIK A5 ODEMI',],
  }
}

AIRPORT_SETTINGS = {
  'LPPR': _LPPR_SETTINGS,
}