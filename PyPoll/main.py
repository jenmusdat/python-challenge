#import my needed modules
import os
import csv

# connect the csv path to Python so I can write my code
csvpath = os.path.join ("Resources", "election_data.csv")

#create the path to send a txt file to the repository
outpath = os.path.join ("Analysis", "election_data.txt")

#D. percentage of candidates
#E. the winner of the election based on popular vote

# create empty dictionary to store candidates
candidatelist = {}

with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")
           
    #set my variables
    vote_count=0
    total_votes=0
    total=0
    candidate=""
    candidate_name=""
    vote=0
    candidatechange=0

    for row in csvreader:
        vote_count = vote_count + 1
        candidate = row[2]
        if candidate not in candidatelist:
            candidatelist.update({candidate : 1})
        else: 
            candidatelist[candidate] += 1


#display my results
print("Election Results")
print("------------------------------")
print("Total Votes: ", str(vote_count))
print("------------------------------")
winner_votes=0
winner=""
for candidate in candidatelist:
    print((f"{candidate}: {candidatelist[candidate]vote_count)*100:.3f}%({candidatelist[candidate]})")
    if candidatelist[candidate] > winner_votes:
        winnercount=candidatelist[candidate]
        winner=candidate
print("------------------------------")
print(f"Winner: {greatvotewinner} ")
print("------------------------------")

