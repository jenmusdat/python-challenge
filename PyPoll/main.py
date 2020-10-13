#import my needed modules
import os
import csv

# connect the csv path to Python so I can write my code
csvpath = os.path.join ("Resources", "election_data.csv")

#create the path to send a txt file to the repository
outpath = os.path.join ("Analysis", "election_data.txt")

vote_count=0

# create empty dictionary to store candidates
candidatelist = {}

#open the file
with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    
    #start on the second row
    csv_header = next(csvreader)
    
    #print(f"CSV Header: {csv_header}")
           
    #set my variables
    vote_count=0
    total_votes=0
    total=0
    candidate=""
    candidate_name=""



    #calculte the candidate vote counts
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
print(f"Total Votes: {vote_count}")
print("------------------------------")
winner_votes = 0
winner_candidate = ""
for candidate in candidatelist:
    print(f"{candidate}: {candidatelist[candidate]/vote_count*100:.3f}% {candidatelist[candidate]}")
    if candidatelist[candidate] > winner_votes:
        winner_votes = candidatelist[candidate]
        winner_candidate = candidate
print("------------------------------")
print(f"Winner: {winner_candidate} ")
print("------------------------------")

#send the results to a txt file
with open (outpath, "w") as textfile:
    textfile.write("Election Results")
    textfile.write("------------------------------")
    textfile.write(f"Total Votes: {vote_count}")
    textfile.write("------------------------------")
    winner_votes=0
    winner_candidate=""
    for candidate in candidatelist:
        textfile.write(f"{candidate}: {candidatelist[candidate]/vote_count*100:.3f}% {candidatelist[candidate]}")
        if candidatelist[candidate] > winner_votes:
            winnercount=candidatelist[candidate]
            winner_candidate=candidate
    textfile.write("------------------------------")
    textfile.write(f"Winner: {winner_candidate} ")
    textfile.write("------------------------------")

