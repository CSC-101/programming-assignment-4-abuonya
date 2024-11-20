import sys          # Make sure config actually points to correct working directory
from data import CountyDemographics
import build_data
import argparse




# make pretty later ************************
def display(counties):
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")

def filter_state(counties, state):
    count = 0
    for county in counties:
        if county.state == state:
            count += 1
    print("Filter: state ==" + " " + state + " " + "(" + str(count) + " entries" + ")")

def filter_gt(counties, field, gt_value):
    count = 0
    field_key = field.split(".")
    new_gt_value = float(gt_value)

    for county in counties:
        if field_key[0] == 'age':
            value = county.age
        elif field_key[0] == 'county':
            value = county.county
        elif field_key[0] == 'Education':
            value = county.education
        elif field_key[0] == 'ethnicities':
            value = county.ethnicities
        elif field_key[0] == 'income':
            value = county.income
        elif field_key[0] == 'population':
            value = county.population
        elif field_key[0] == 'state':
            value = county.state

        for key in field_key[1:]:
            try:
                    value = value[key]
            except (KeyError, IndexError):
                value = None

        if value is not None and value > new_gt_value:
            count += 1

    print("Filter: " + " " + field + " "  + "(" + str(count) + " entries" + ")")


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
            filter_state(counties, component)

        elif "filter-gt" in operation:
            field = operation.split(":")[1]
            gt_value = operation.split(":")[2]
            filter_gt(counties, field, gt_value)


if __name__ == "__main__":
    all_operations()
