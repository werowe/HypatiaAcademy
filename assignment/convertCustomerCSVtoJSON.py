import csv
import simplejson as json

csvFilePath = '/Users/walkerrowe/Documents/customers.csv'
simplejsonFilePath = '/Users/walkerrowe/Documents/customers2.json'

data={}

with open (csvFilePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        print(rows)
        id = rows['customerNumber']
        data[id] = rows

with open (simplejsonFilePath, 'w') as simplejsonFile:
    simplejsonFile.write(json.dumps(data, indent=4))
