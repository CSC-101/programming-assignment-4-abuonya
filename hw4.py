import sys          # Make sure config actually points to correct working directory
from types import NoneType

from data import CountyDemographics
import build_data
import argparse




# Purpose of Function: This function 'display' iterates through the entire list of counties and prints every counties information to the terminal.
def display(counties:list[CountyDemographics]) -> None:
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")
    return None

def filter_state(counties:list[CountyDemographics], state:str) -> None:
    count = 0
    for county in counties:
        if county.state == state:
            count += 1
        else:
            print("There is an issue with your input.")
    print("Filter: state ==" + " " + state + " " + "(" + str(count) + " entries" + ")")
    return None

# Purpose of Function: This function 'filter_gt' takes a list of counties, a field, and a threshold value, 'gt_value.' This narrows the collection of entries to only counties specified by the field.
def filter_gt(counties:list[CountyDemographics], field:str, gt_value:str) -> list:
    count = 0       # Set variable 'count' to 0 so we can count every entry that exists within the parameters specified in this function.
    gt_filtered_counties = []       # Initiate an empty list to store filtered counties greater than threshold value.
    new_gt_value = float(gt_value)  # Convert gt_value into a float because text files are automatically strings.

    for county in counties:     # Iterate through list[CountyDemographics] at every index, aka 'county.'
        field_key = field.split(".")   # Split our field into two compare our key-value pairs as we iterate through the list of counties.
        try:
            if len(field_key) > 1:
                if field_key[0] == 'Age':
                    value = county.age.get(field_key[1])  #.get() to extract our value from our key in the dictionary.
                elif field_key[0] == 'County':
                    value = county.county.get(field_key[1])
                elif field_key[0] == 'Education':
                    value = county.education.get(field_key[1])
                elif field_key[0] == 'Ethnicities':
                    value = county.ethnicities.get(field_key[1])
                elif field_key[0] == 'income':
                    value = county.income.get(field_key[1])
                elif field_key[0] == 'Population':
                    value = county.population.get(field_key[1])
                elif field_key[0] == 'State':
                    value = county.state.get(field_key[1])
                else:
                    value = None
        except (IndexError, KeyError):      # Catch any errors.
            value = None
            print("There is an issue with your input.")

        if value is not None and value > new_gt_value:
            count += 1
            gt_filtered_counties.append(county)
    print("Filter: " + " " + field + " " + "(" + str(count) + " entries" + ")")
    return gt_filtered_counties

def filter_lt(counties:list[CountyDemographics], field:str, lt_value:str) -> list:
    count = 0
    lt_filtered_counties = []
    new_lt_value = float(lt_value)

    for county in counties:
        field_key = field.split(".")

        try:
            if len(field_key) > 1:
                if field_key[0] == 'Age':
                    value = county.age.get(field_key[1])  # Where field_key[0] is the class attribute.
                elif field_key[0] == 'County':
                    value = county.county.get(field_key[1])
                elif field_key[0] == 'Education':
                    value = county.education.get(field_key[1])
                elif field_key[0] == 'Ethnicities':
                    value = county.ethnicities.get(field_key[1])
                elif field_key[0] == 'Income':
                    value = county.income.get(field_key[1])
                elif field_key[0] == 'Population':
                    value = county.population.get(field_key[1])
                elif field_key[0] == 'State':
                    value = county.state.get(field_key[1])
                else:
                    value = None
        except (IndexError, KeyError):
            value = None
            print("There is an issue with your input.")

        if value is not None and value < new_lt_value:
            count += 1
            lt_filtered_counties.append(county)
    print("Filter: " + " " + field + " " + "(" + str(count) + " entries" + ")")
    return lt_filtered_counties

def population_total(counties: list) -> float:
    sum_of_2014_population = 0

    for county in counties:
        temp = county.population['2014 Population']
        sum_of_2014_population += temp

    return sum_of_2014_population


def population(counties, field) -> float:
    sub_population_total = 0.0
    field_key = field.split(".")

    try:
        for county in counties:
            if field_key[0] == 'Age':
                value = county.age.get(field_key[1]) # Where field_key[0] is the class attribute.
            elif field_key[0] == 'County':
                value = county.county.get(field_key[1])
            elif field_key[0] == 'Education':
                value = county.education.get(field_key[1])
            elif field_key[0] == 'Ethnicities':
                value = county.ethnicities.get(field_key[1])
            elif field_key[0] == 'Income':
                value = county.income.get(field_key[1])
            elif field_key[0] == 'Population':
                value = county.population.get(field_key[1])
            elif field_key[0] == 'State':
                value = county.state.get(field_key[1])

            total_2014_population_for_sub_pop = county.population['2014 Population']
            sub_pop_per_county = total_2014_population_for_sub_pop * (value / 100)
            sub_population_total += sub_pop_per_county

    except (IndexError, KeyError):
        value = None
        print("There is an issue with your input.")

    return sub_population_total


def percent(sub_pop, total_population) -> float:
    sub_population_total_percent = (sub_pop / total_population) * 100

    return sub_population_total_percent

# Main Module

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
            sum_of_2014_population = population_total(counties)
            print("2014 Population:" + " " + str(sum_of_2014_population))

        elif "population:" in operation:
            field = operation.split(":")[1]
            sub_population_total = population(counties, field)
            print("2014" + " " + field + "Population:" + " " + str(sub_population_total))


        elif "percent:" in operation:
            field = operation.split(":")[1]
            sub_pop = population(counties, field)
            total_population = population_total(counties)
            sub_population_total_percent = percent(sub_pop, total_population)
            print("2014" + " " + field + "Population:" + " " + str(sub_population_total_percent))



if __name__ == "__main__":
    all_operations()
