import os

import csv

data = []

csvpath = os.path.join('pybank', 'resources', 'budget_data.csv')

total = 0

initial = 867884

with open(csvpath, 'r') as csvfile:
    
    profit = csv.reader(csvfile, delimiter=',')


    csv_header = next(profit)
    print(f"CSV Header: {csv_header}")
              
    Months=len(list(profit))
    
    print(f"total months: {Months}")

with open(csvpath, 'r') as csvfile:

    profit = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(profit)    
    total = sum(float(row[1]) for row in profit)
    
    print(f"total: {total}")


with open(csvpath) as csvfile:
    
   profit = csv.reader(csvfile, delimiter=',')

   csv_header = next(profit)     
   
   for row in profit:
    data.append(row())
   
   col = [x[1] for x in data]

