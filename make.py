#!/usr/bin/env python3
import sys
from random import shuffle, choice
import click

from src.airport import Airport

@click.command()
@click.argument('airport')
@click.argument('runway')
@click.option('--departures', default=10, type=int, help='Number of aircraft on the ground to depart.')
@click.option('--arrivals', default=10, type=int, help='Number of arrivals.')
def main(airport, runway, departures, arrivals):
  """Generates a Euroscope's Sweatbox scenario file for an AIRPORT and RUNWAY in use"""
  with open('output.txt', 'w') as file:
    scenario = Airport(
      airport,
      runway,
      total_departures=departures,
      total_arrivals=arrivals)
    file.write(str(scenario))

  file.close()

if __name__ == '__main__':
    main()
