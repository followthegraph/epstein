import json
from pprint import pprint
from lists import aircraftIDs, aircraftMakes, aircraftModels, origs_dests
# TODO: alphabetize lists


def main():
    with open('flight_log.json') as f:
        logs = json.load(f)
    enterFlightLog(logs)


def enterFlightLog(logs):
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
    if int(aircraftID_choice)+1 == len(aircraftIDs):
        aircraftID = input("Aircraft ID (Other): ")
    else:
        aircraftID = aircraftIDs[int(aircraftID_choice)]

    pprint("|-------------------------------------------------------------|")
    pprint("Aircraft Make:")
    for i, id in enumerate(aircraftMakes):
        pprint(str(i) + ' - ' + str(id))
    aircraftMake_choice = input("Aircraft Make: ")
    if int(aircraftMake_choice)+1 == len(aircraftMakes):
        aircraftMake = input("Aircraft Make (Other): ")
    else:
        aircraftMake = aircraftMakes[int(aircraftMake_choice)]

    pprint("|-------------------------------------------------------------|")
    pprint("Aircraft Model:")
    for i, id in enumerate(aircraftModels):
        pprint(str(i) + ' - ' + str(id))
    aircraftModel_choice = input("Aircraft Model: ")
    if int(aircraftModel_choice)+1 == len(aircraftModels):
        aircraftModel = input("Aircraft Model (Other): ")
    else:
        aircraftModel = aircraftModels[int(aircraftModel_choice)]

    pprint("|-------------------------------------------------------------|")
    pprint("Origin:")
    for i, id in enumerate(origs_dests):
        pprint(str(i) + ' - ' + str(id))
    origin_choice = input("Origin: ")
    if int(origin_choice)+1 == len(origs_dests):
        origin = input("Origin (Other): ")
    else:
        origin = origs_dests[int(origin_choice)]

    pprint("|-------------------------------------------------------------|")
    pprint("Destination:")
    for i, id in enumerate(origs_dests):
        pprint(str(i) + ' - ' + str(id))
    destination_choice = input("destination: ")
    if int(destination_choice)+1 == len(origs_dests):
        destination = input("Destination (Other): ")
    else:
        destination = origs_dests[int(destination_choice)]

    pilot = input("Pilot: ")

    passengers = input("Comma Separated list of passengers: ")
    # Validation
    # TODO

    # Create JSON
    # TODO add default behavior

    flight_log = {}
    flight_log['date'] = flightDate
    flight_log['flightNumber'] = flightNumber
    flight_log['simulation'] = False if simulation == "" else simulation
    flight_log['notes'] = notes
    aircraft = {}
    aircraft['id'] = aircraftID
    aircraft['make'] = aircraftMake
    aircraft['model'] = aircraftModel
    flight_log['aircraft'] = aircraft
    flight_log['origin'] = origin
    flight_log['destination'] = destination
    flight_log['pilots'] = "David Rodgers" if pilot == "" else pilot
    passengers_list = []
    # will need to trim the passenger
    for passenger in passengers.split(','):
        passengers_list.append(passenger)
    flight_log['passengers'] = passengers_list

    logs.append(flight_log)
    pprint(logs)

    with open('flight_log.json', 'w') as outfile:
        json.dump(logs, outfile, indent=4)

    enterFlightLog(logs)


if __name__ == "__main__":
    main()
