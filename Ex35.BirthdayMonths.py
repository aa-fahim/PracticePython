## Birthday Months

# Reads how many birthdays are in each month

import json
from collections import Counter

def read_from_file():
    with open('birthdays.json', 'r') as f:
        info = json.load(f)
    
    return info

if __name__ == '__main__':
    months = []
    num_of_months = {}
    
    birthdays = read_from_file()
        
    for name in birthdays:
        month = birthdays[name].split('/')
        months.append(month[0])
    
    c = Counter(months)
    
    num_of_months['January']    = c['01']
    num_of_months['February']   = c['02']
    num_of_months['March']      = c['03']
    num_of_months['April']      = c['04']
    num_of_months['May']        = c['05']
    num_of_months['June']       = c['06']
    num_of_months['July']       = c['07']
    num_of_months['August']     = c['08']
    num_of_months['September']  = c['09']
    num_of_months['October']    = c['10']
    num_of_months['November']   = c['11']
    num_of_months['December']   = c['12']
    
    print(num_of_months)