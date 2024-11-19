import sys
from data import CountyDemographics
import build_data
import argparse




# make pretty later ************************
def display(counties):
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")

def filter_state(counties, state):
    filtered_by_state = []
    for county in counties:
        if county.state == state:
            filtered_by_state.append(county)
    return filtered_by_state

def all_operations():
    try:
        given_operation = sys.argv[1]
    except IndexError:
        print("Could not access the file provided.")
        sys.exit(1)

    with open(given_operation, "r") as temporary:
        operations = temporary.readlines()

    counties = build_data.get_data()

    for operation in operations:
        if "display" in operation:
            display(counties)

        elif "filter-state" in operation:
            component = operation.split(":")[1]
            filter_state(counties, component)
            display(counties)


if __name__ == "__main__":
    all_operations()
