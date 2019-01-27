#!/usr/bin/env python3
"""
Euroscope Sweatbox Scenario Maker

Copyright (C) 2019  Pedro Rodrigues <prodrigues1990@gmail.com>
                    Tiago Vicente <tmavicente@gmail.com>

This file is part of Euroscope Sweatbox Scenario Maker.

Euroscope Sweatbox Scenario Maker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Euroscope Sweatbox Scenario Maker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Euroscope Sweatbox Scenario Maker. If not, see <http://www.gnu.org/licenses/>.
"""
import click

from src.airport import make_scenario

@click.command()
@click.argument('airport')
@click.argument('runway')
@click.option(
    '--departures',
    default=10,
    type=int,
    help='Number of aircraft on the ground to depart.')
@click.option('--arrivals', default=10, type=int, help='Number of arrivals.')
def main(airport, runway, departures, arrivals):
    """Generates a Euroscope's Sweatbox scenario file for an AIRPORT and RUNWAY in use"""
    with open('output.txt', 'w') as file:
        scenario = make_scenario(
            airport,
            runway,
            total_departures=departures,
            total_arrivals=arrivals)

        file.write(str(scenario))
        file.close()

if __name__ == '__main__':
    main() # pylint: disable=E1120
