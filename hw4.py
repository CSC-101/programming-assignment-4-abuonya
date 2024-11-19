import sys
from data import CountyDemographics
import build_data
import argparse

counties = build_data.get_data()

def display():
    for county in counties:
        print(f"{county.county} {county.age} {county.education} {county.ethnicities} {county.income} {county.state}")


if __name__ == "__main__":
    display()