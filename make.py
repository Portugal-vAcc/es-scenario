#!/usr/bin/env python3
import sys
from random import shuffle, choice

from src.airport import Airport

def main():
  AIRPORT = sys.argv[1]
  RUNWAY = sys.argv[2]
  TOTAL_DEPARTURES = int(sys.argv[3])

  with open('output.txt', 'w') as file:
    scenario = Airport(AIRPORT, RUNWAY, total_departures=TOTAL_DEPARTURES)
    file.write(str(scenario))

  file.close()

if __name__ == '__main__':
  if len(sys.argv) < 4:
    print('Usage: ´$ ./make.py AIRPORT RUNWAY TOTAL_DEPARTURES´')
  else:
    main()
