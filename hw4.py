import sys
from data import CountyDemographics
import build_data
import argparse

counties = build_data.get_data()


# make pretty later ************************
def display():
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")

def filter_state():
    for county in counties:
        if county.state == sys.argv[1]:
            print(county)

def all_operations():
    try:
        given_operation = sys.argv[1]
    except IndexError:
        print("Could not access the file provided.")
        sys.exit(1)

    with open(given_operation, "r"):
        for line in


if __name__ == "__main__":
    given_operation = sys.argv[1]
    display()