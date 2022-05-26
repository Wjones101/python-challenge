import os

import csv

from prometheus_client import Counter

data = {}

csvpath = os.path.join('pypoll', 'resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    
    votes = csv.reader(csvfile, delimiter=',')


    csv_header = next(votes)
    print(f"CSV Header: {csv_header}")
              
    voters=len(list(votes))
    
    print(f"total votes: {voters}")
    


with open(csvpath, 'r') as csvfile:
    
    votes = csv.reader(csvfile, delimiter=',')
    csv_header = next(votes)
    
    for row in votes:
        data(row[2])
        
        count = Counter(data).items()
        percentages = {x: int(float(y) / len(votes) * 100) for x, y in count}

for votes, pct in percentages.iteritems():
    print ('%s - %s%s' % (votes, pct, '%'))