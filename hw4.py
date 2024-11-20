import sys          # Make sure config actually points to correct working directory
from data import CountyDemographics
import build_data
import argparse




# make pretty later ************************
def display(counties:list[CountyDemographics]):
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")

def filter_state(counties:list[CountyDemographics], state:str):
    count = 0
    for county in counties:
        if county.state == state:
            count += 1
    print("Filter: state ==" + " " + state + " " + "(" + str(count) + " entries" + ")")

def filter_gt(counties, field, gt_value) -> list:
    count = 0
    gt_filtered_counties = []
    new_gt_value = float(gt_value)

    for county in counties:
        field_key = field.split(".")

        try:
            if len(field_key) > 1:
                if field_key[0] == 'age':
                    value = county.age.get(field_key[1])
                elif field_key[0] == 'county':
                    value = county.county.get(field_key[1])
                elif field_key[0] == 'Education':
                    value = county.education.get(field_key[1])
                elif field_key[0] == 'ethnicities':
                    value = county.ethnicities.get(field_key[1])
                elif field_key[0] == 'income':
                    value = county.income.get(field_key[1])
                elif field_key[0] == 'population':
                    value = county.population.get(field_key[1])
                elif field_key[0] == 'state':
                    value = county.state.get(field_key[1])
                else:
                    value = None
        except (IndexError, KeyError):
            value = None

        if value is not None and value > new_gt_value:
            count += 1
            gt_filtered_counties.append(county)
    print("Filter: " + " " + field + " " + "(" + str(count) + " entries" + ")")
    return gt_filtered_counties

def filter_lt(counties:list[CountyDemographics], field:str, gt_value:str) -> list:
    count = 0
    lt_filtered_counties = []
    new_lt_value = float(gt_value)

    for county in counties:
        field_key = field.split(".")

        try:
            if len(field_key) > 1:
                if field_key[0] == 'age':
                    value = county.age.get(field_key[1])  # Where field_key[0] is the class attribute.
                elif field_key[0] == 'county':
                    value = county.county.get(field_key[1])
                elif field_key[0] == 'Education':
                    value = county.education.get(field_key[1])
                elif field_key[0] == 'ethnicities':
                    value = county.ethnicities.get(field_key[1])
                elif field_key[0] == 'income':
                    value = county.income.get(field_key[1])
                elif field_key[0] == 'population':
                    value = county.population.get(field_key[1])
                elif field_key[0] == 'state':
                    value = county.state.get(field_key[1])
                else:
                    value = None
        except (IndexError, KeyError):
            value = None

        if value is not None and value < new_lt_value:
            count += 1
            lt_filtered_counties.append(county)
    print("Filter: " + " " + field + " " + "(" + str(count) + " entries" + ")")
    return lt_filtered_counties

def population_total(counties: list):
    sum_of_2014_population = 0

    for county in counties:
        temp = county.population['2014 Population']
        sum_of_2014_population += temp
    print("2014 Population:" + " " + str(sum_of_2014_population))


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
            counties = filter_gt(counties, field, gt_value)

        elif "filter-lt" in operation:
            field = operation.split(":")[1]
            lt_value = operation.split(":")[2]
            counties = filter_lt(counties, field, lt_value)

        elif "population-total" in operation:
            counties = build_data.get_data()
            population_total(counties)


if __name__ == "__main__":
    all_operations()
