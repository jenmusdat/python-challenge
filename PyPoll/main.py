import os
import csv

csvpath = os.path.join ("Resources", "election_data.csv")


outpath = os.path.join ("Analysis", "election_data.txt")


with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    #
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")