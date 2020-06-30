# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    with open (filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        s = 0

        for line in csv_reader:
            try:
                s += int(line['shares']) * float(line['price'])
            except ValueError:
                pass
        return s

if len(sys.argv) == 2:
    print(sys.argv)
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(cost)