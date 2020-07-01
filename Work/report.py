# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):

    with open(filename, 'r') as file:
        
        csv_reader = csv.reader(file)
        headers = next(csv_reader)

        portfolio = [dict(zip(headers, (row[0], int(row[1]), float(row[2]))))for row in csv_reader]

    return portfolio


def read_prices(filename):

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = {}
        for line in csv_reader:
            if len(line) == 2:
                data[line[0]] = float(line[1])
        return data


def gain_loss(filename_1, filename_2):
   
    gl = {}
    prices = read_prices(filename_2)
    for stock in read_portfolio(filename_1):
        name, shares, price = stock.values()
        if name in prices:
            gl[name] = prices[name] - price
    return gl


def make_report(stocks, prices):

    report = []
    for stock in stocks:
       name, shares, price = stock.values()
       if name in prices:
           report.append((name, shares, price, prices[name] - price))
    return report


def print_report(report):
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print(' '.join('-'*10 for _ in range(len(headers))))

    for name, shares, price, diff in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {diff:>10.2f}')
