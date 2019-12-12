import json
from pprint import pprint

with open('flight_log.json') as f:
    logs = json.load(f)

# aircraft list
aircraftIDs = []
aircraftIDs.append('Simulation')
aircraftIDs.append('N908JE')
aircraftIDs.append('N909JE')
aircraftIDs.append('N908GM')
aircraftIDs.append('N739SP')
aircraftIDs.append('N474AW')
# looked like pg12 had a 1589 flight with N909JG
aircraftIDs.append('N909JG')
aircraftIDs.append('N407BP')
aircraftIDs.append('N491GM')
# pg18 has some that appear to be maintenance that I can't make out
aircraftIDs.append('N5279X')
aircraftIDs.append('N500JA')  # pg 39
aircraftIDs.append('N16909')
aircraftIDs.append('N125MF')
aircraftIDs.append('N72PH')
aircraftIDs.append('N505LS')
aircraftIDs.append('N75RR')
aircraftIDs.append('N778ME')
aircraftIDs.append('N4424E')
aircraftIDs.append('N307BG')
aircraftIDs.append('Other')

# aircraft make list
aircraftMakes = []
aircraftMakes.append('Gulfstream')
aircraftMakes.append('Boeing')

# aircraft models list


# Input
while True:
    # check if flight number already exists
    # looks like there may be duplicate flight numbers, may have to check to make sure that the flight and aircraft id
    # or ignore what appears to be maintenance flights with duplicate flight numbers
    pprint("|-------------------------------------------------------------|")
    flightNumber = input("Flight Number: ")
    for i in range(len(logs)):
        if flightNumber == logs[i]['flightNumber']:
            passengers = logs[i]['passengers']
            flightNumCheck = True
            break
        else:
            flightNumCheck = False
            continue

    if len(flightNumber) > 0:
        if not flightNumCheck:
            pprint('Adding Flight Number ' + flightNumber)
            break
        else:
            pprint('Flight Number ' + flightNumber + ' already exists.')
            continue
    else:
        pprint('Flight number must not be blank.')
        continue

while True:
    # shouldn't be prior to 1997-12-14
    # shouldn't be after 2006-01-19 (appears to be latest date, but pages may be out of order)
    pprint("|-------------------------------------------------------------|")
    flightDate = input("Date of flight (yyyy-mm-dd): ")
    break

pprint("|-------------------------------------------------------------|")
simulation = input("Simulation (True/False): ")
# auto-answer aircraft ID if simulation = True
pprint("|-------------------------------------------------------------|")
notes = input("Notes: ")

# may want to order or group these in some way, or store in an array that is iterated and printed
pprint("|-------------------------------------------------------------|")
pprint("Aircraft IDs:")
for i, id in enumerate(aircraftIDs):
    pprint(str(i) + ' - ' + str(id))
aircraftID_choice = input("Aircraft ID: ")
aircraftID = aircraftIDs[int(aircraftID_choice)]

pprint("|-------------------------------------------------------------|")
pprint("Aircraft Make:")
for i, id in enumerate(aircraftMakes):
    pprint(str(i) + ' - ' + str(id))
aircraftMake_choice = input("Aircraft Make: ")
aircraftMake = aircraftMakes[int(aircraftMake_choice)]

aircraftModel = input("Aircraft Model: ")
origin = input("Origin: ")
destination = input("Destination: ")
pilot = input("Pilot: ")
passengers = input("Comma Separated list of passengers: ")
# Validation
# TODO

# Create JSON
# TODO add default behavior

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
# will need to trim the passenger
for passenger in passengers.split(','):
    passengers_list.append(passenger)
flight_log['passengers'] = passengers_list

logs.append(flight_log)
pprint(logs)

with open('flight_log', 'w') as outfile:
    json.dump(logs, outfile, indent=4)
