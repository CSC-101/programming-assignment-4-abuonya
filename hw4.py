import sys
from data import CountyDemographics
import build_data
import argparse
# Make sure config actually points to correct



# make pretty later ************************
def display(counties):
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")

def filter_state(counties, state):
    filtered_by_state = []
    count = 0
    for county in counties:
        if county.state == state:
            filtered_by_state.append(county)
            count += 1
    print("Filter: state ==" + " " + state + " " + "(" + str(count) + " entries"+")")
    return filtered_by_state

def all_operations():
    try:
        given_operation = sys.argv[1]           # Take first argument from the command line.
    except IndexError:
        print("Could not access the file provided.")
        sys.exit(1)

    with open(given_operation, "r") as temporary:
        operations = temporary.readlines()

    counties = build_data.get_data()

    for operation in operations:
        operation = operation.strip()       # Remove extra whitespace so code can filter properly (n/ was an issue).

        if "display" in operation:
            display(counties)

        elif "filter-state" in operation:
            component = operation.split(":")[1]         # Separate operation from component; filter-state and *state abbr*
            filtered_states = filter_state(counties, component)
            display(filtered_states)

if __name__ == "__main__":
    all_operations()
