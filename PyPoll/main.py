import os
import csv

csvpath = os.path.join ("Resources", "election_data.csv")


outpath = os.path.join ("Analysis", "election_data.txt")


with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    #print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    #set my variables
    total_votes = 0
    candidates = dict()








print("Election Results")
print("------------------------------")
print("Total Votes: ")
print("------------------------------")
print(candidates)
print("------------------------------")
print("Winner:  ")
print("------------------------------")
