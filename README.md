# Euroscope Sweatbox Scenario file generator [![Build Status](https://travis-ci.org/pedro2555/scenarios-es.svg?branch=master)](https://travis-ci.org/pedro2555/scenarios-es)

Generates a random Euroscope's Sweatbox scenario file for an AIRPORT and RUNWAY in use.

# Installation

Install the python runtime, if not installed already, https://www.python.org/downloads/.

Use pip to download and install the program from source:

    $ pip install git+https://github.com/Portugal-vAcc/es-scenario.git

# Usage

    $ esmake [OPTIONS] AIRPORT RUNWAY

## Options:

**--departures** `INTEGER`  Number of aircraft on the ground to depart.  
**--arrivals** `INTEGER`    Number of arrivals.

## Usage Examples

    $ esmake LPPT 03 --arrivals=0 --departure=50

50 departures, with no arrival aircraft