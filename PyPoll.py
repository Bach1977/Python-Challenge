# Import library 
import os
import csv

    # Grab the poll csv file
#poll_CSV = os.path.join('..', "pyPoll",  "raw_data",  'election_data_2.csv')

    # Create new CSV
    #newWrestlingCSV = os.path.join('..', 'output', 'WWE-Data-' + yearToCheck + '.csv')


    # Set empty list variables :
Total_Votes = []
Rogers = []
Gomez = []
Brentwood = []
Higgins = []
Winner = []
    
    # open pollcsv file :
    
#with open(poll_CSV, newline="") as csvfile:
        #csvreader= csv.reader(csvfile, delimiter=",")

with open('election_data_2.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('election_data_2_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[2]:rows[0] for rows in reader}

#for myKey in mydict.keys():
 #   print "{2}: {0}".format(myKey, len(myDict[myKey])
#        # Skipp headers
 #       next(csvreader, None)
        
#        unique_items = set(csvreader)
 #       keys = [[entry[0]] for entry in unique_items]
  #      for key in set (keys):
   #         print("Key '{}' appears {} unique times".format(key, keys.count(key)))
from collections import Counter
c = Counter(mydict)

print( c.items() )

        