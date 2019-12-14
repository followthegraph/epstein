import json
from pprint import pprint
from shutil import copyfile
from colorama import init, Fore, Style
from prettytable import PrettyTable
from os import system
from lists import aircraftIDs, aircraftMakes, aircraftModels, origs_dests, neo4j_import_dir
# TODO: alphabetize lists (just use sort)


def main():
    init()  # for colorama
    with open('flight_log.json') as f:
        logs = json.load(f)
    enterFlightLog(logs)
    copyfile('flight_log.json', neo4j_import_dir+'\\flight_log.json')


def enterFlightLog(logs):
    # Input
    system('cls')
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

    system('cls')
    while True:
        # shouldn't be prior to 1997-12-14
        # shouldn't be after 2006-01-19 (appears to be latest date, but pages may be out of order)
        pprint("|-------------------------------------------------------------|")
        flightDate = input("Date of flight (yyyy-mm-dd): ")
        break

    system('cls')
    pprint("|-------------------------------------------------------------|")
    simulation = input("Simulation (True/False): ")
    # auto-answer aircraft ID if simulation = True
    system('cls')
    pprint("|-------------------------------------------------------------|")
    notes = input("Notes: ")

    # may want to order or group these in some way, or store in an array that is iterated and printed
    system('cls')
    pprint("|-------------------------------------------------------------|")
    pprint("Aircraft IDs:")
    for i, id in enumerate(aircraftIDs):
        pprint(str(i) + ' - ' + str(id))
    aircraftID_choice = input("Aircraft ID: ")
    if int(aircraftID_choice)+1 == len(aircraftIDs):
        aircraftID = input("Aircraft ID (Other): ")
    else:
        aircraftID = aircraftIDs[int(aircraftID_choice)]

    system('cls')
    pprint("|-------------------------------------------------------------|")
    pprint("Aircraft Make:")
    for i, id in enumerate(aircraftMakes):
        pprint(str(i) + ' - ' + str(id))
    aircraftMake_choice = input("Aircraft Make: ")
    if int(aircraftMake_choice)+1 == len(aircraftMakes):
        aircraftMake = input("Aircraft Make (Other): ")
    else:
        aircraftMake = aircraftMakes[int(aircraftMake_choice)]

    system('cls')
    pprint("|-------------------------------------------------------------|")
    pprint("Aircraft Model:")
    for i, id in enumerate(aircraftModels):
        pprint(str(i) + ' - ' + str(id))
    aircraftModel_choice = input("Aircraft Model: ")
    if int(aircraftModel_choice)+1 == len(aircraftModels):
        aircraftModel = input("Aircraft Model (Other): ")
    else:
        aircraftModel = aircraftModels[int(aircraftModel_choice)]

    system('cls')
    pprint("|-------------------------------------------------------------|")
    originList = sectionTable(
        "Origin", """       Choose the origin """, 'origs_dests', logs)

    origin_choice = input("Origin: ")
    if int(origin_choice)+1 == len(origs_dests):
        origin = input("Origin (Other): ")
    else:
        origin = origs_dests[int(origin_choice)]

    system('cls')
    pprint("|-------------------------------------------------------------|")
    pprint("Destination:")
    destinationList = sectionTable(
        "Destination", """       Choose the destination """, 'origs_dests', logs)

    destination_choice = input("destination: ")
    if int(destination_choice)+1 == len(origs_dests):
        destination = input("Destination (Other): ")
    else:
        destination = origs_dests[int(destination_choice)]

    system('cls')
    pilot = input("Pilot: ")

    system('cls')
    passengers = []
    while True:

        # TODO: ability to edit awaiting passengers
        passengerList = sectionTable("Passengers", """       Choose the number corresponding to the passenger
                 OR enter a new passenger"
               Type x to indicate no more passengers """, 'passengers', logs)
        passenger = input("Passenger(s) (" + str(passengers) + "): ")

        if passenger.isnumeric() and int(passenger) < len(passengerList):
            passengers.append(passengerList[int(passenger)])
            system('cls')
            continue
        elif len(passenger) > 0 and passenger not in passengerList and passenger != 'x':
            passengers.append(passenger)
            system('cls')
            continue
        elif len(passenger) == 0:
            warningMSG = Fore.RED + \
                '   !!!!!       must be at least one passenger   !!!!!       ' + Style.RESET_ALL
            system('cls')
            print(warningMSG)
            continue
        else:
            break

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
    flight_log['passengers'] = passengers

    logs.append(flight_log)
    pprint(logs)

    with open('flight_log.json', 'w') as outfile:
        json.dump(logs, outfile, indent=4)

    enterFlightLog(logs)


def sectionTable(header, instructions, sectionKey, logs):
    print("|-------------------------------------------------------------|")
    print(Fore.BLUE + "    " + header + Style.RESET_ALL)
    print("|-------------------------------------------------------------|")
    print(Fore.RED + instructions + Style.RESET_ALL)
    print("|-------------------------------------------------------------|")
    if sectionKey == 'origs_dests':
        # optionList = set()
        # optionList = getUniqueValuesForKey(logs, 'origin')
        # optionList += getUniqueValuesForKey(logs, 'destination')
        # optionList = list(optionList)
        optionList = list(origs_dests)
    else:
        optionList = getUniqueValuesForKey(logs, sectionKey)

    optionList.sort()
    line = []
    tbl = PrettyTable(header=False, hrules=True,
                      horizontal_char='_', junction_char='/')
    for i in range(len(optionList)):
        line.append('[' + str(i) + '] - ' + Fore.GREEN +
                    optionList[i] + Style.RESET_ALL)
        if len(line) % 5 == 0:
            tbl.add_row(line)
            line = []
    tbl.align = "l"
    print(tbl)
    return optionList


def getUniqueValuesForKey(jsonData, searchKey):
    # return a list of unique values for a given key in a json variable
    values = set()
    if searchKey != 'passengers':
        for item in jsonData:
            values.add(item[searchKey])
    else:
        for item in jsonData:
            for passenger in item[searchKey]:
                values.add(passenger)

    return list(values)


if __name__ == "__main__":
    main()
