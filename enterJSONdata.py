import json
from pprint import pprint
# Input
flightDate = input("Date of flight (yyyy-mm-dd): ")
flightNumber = input("Flight Number: ")
simulation = input("Simulation (True/False): ")
notes = input("Notes: ")
aircraftID = input("Aircraft ID: ")
aircraftMake = input("Aircraft Make: ")
aircraftModel = input("Aircraft Model: ")
origin = input("Origin: ")
destination = input("Destination: ")
pilot = input("Pilot: ")
passengers = input("Comma Separated list of passengers: ")
# Validation
# TODO

# Create JSON
with open('data.json') as f:
    logs = json.load(f)
    flight_log = {}
    flight_log['date'] = flightDate
    flight_log['flightNumber'] = flightNumber
    flight_log['simulation'] = simulation
    flight_log['notes'] = notes
    aircraft = {}
    aircraft['id'] = aircraftID
    aircraft['make'] = aircraftMake
    aircraft['model'] = aircraftModel
    flight_log['aircraft'] = aircraft
    flight_log['origin'] = origin
    flight_log['destination'] = destination
    flight_log['pilots'] = pilot
    passengers_list = []
    for passenger in passengers.split(','):
        passengers_list.append(passenger)
    flight_log['passengers'] = passengers_list

logs.append(flight_log)
pprint(logs)

with open('data.json', 'w') as outfile:
    json.dump(logs, outfile, indent=4)
