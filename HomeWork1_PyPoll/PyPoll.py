# Import library 
import os
import csv

    # Grab the poll csv file
poll_CSV = os.path.join('..', 'Python-Challenge', 'election_data_2.csv')

    # Set empty list variables :
Total_Votes = []
Khan_percent = []
Correy_percent = []
Li_percent = []
OTooley_percent = []
Winner = []
    
    # open pollcsv file :
    
with open(poll_CSV, newline="") as csvfile:
        csvreader= csv.reader(csvfile, delimiter=",")
        mydict = {rows[0]:rows[2] for rows in csvreader}

from collections import defaultdict
Counter = defaultdict(int)
for v in mydict.values():
    Counter[v]+=1



# Estimate the percent for each candidate and format
Khan_percent = Counter['Khan']/len(mydict.keys())
Correy_percent = Counter['Correy']/len(mydict.keys())
Li_percent = Counter['Li']/len(mydict.keys())
OTooley_percent = Counter["O'Tooley"]/len(mydict.keys())

# Print final results

print("---Election Results-------")
print(" Total Votes : " + str(len(mydict.keys())))
print("----------------------")
print("Khan : " + str("{:.1%}".format(Khan_percent))+ "  ("+str(Counter["Khan"])+")")
print("Correy : " + str("{:.1%}".format(Correy_percent))+ "  ("+str(Counter["Correy"])+")")
print("Li : "  + str("{:.1%}".format(Li_percent))+ "  ("+str(Counter["Li"])+")")
print("O'Tooley : " +  str("{:.1%}".format(OTooley_percent))+ "  ("+str(Counter["O'Tooley"])+")")

