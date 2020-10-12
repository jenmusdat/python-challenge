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
    greatestvotecount=0
    greatvotewinner=""
    candidate=""

    for row in csvreader:
        vote_count = vote_count + 1
        candidate = row[2]
        if candidate not in candidatelist:
            candidatelist.update({candidate : 1})
        else: 
            candidatelist[candidate] += 1

    
    for row in csvreader:
            
            total_votes = total_votes+1

            candidate_name = row[2]

            if not candidate_name in candidate:
                candidate.update({row[2] : candidate_name})
     # for row in reader:
    #for A what will we do? sum the total number of rows
        #total_votes +=1
   
    #for unique_candidates:
    #all_candidate_with_duplicate.append(row[2])
    #Candidate = "Khan"
    #dictionary = {"Candidate":"Khan"
#}
   # if Candidate in dictionary.values(): 

    #totaluniqueKhan.count
    #count = 0
    #all_candidate_with_duplicate + []
    #create a dictionary
    #candidate_totals = {}

#with open file to load as poll_csv
    #reader = csv (poll_csv)

    #discard header if you want
    #next on the reader object

    #the goal is to loop everything once
 
   # for uniquecandidates 
#    all_candidate_with_duplicate.append(row[2])
#
#    for total number of votes per candidate
#    add a dictionary with a key above the with
#    if candidate_totals.get(row[2]):
#        candidate_totals[row[2]]+=1
#    else:
#   candidate_totals[row[2]] = 0


#for candidate_name,vote_toatl in candidate_totals:
 #   print(candidate_name).items
#print(v/total_votes*100)
#print(max(candidate_name))

    #{
    #    "candidate_a": 2,
    #    "candidate_b": 1,
#previous=int(row[1])

#display my results
print("Election Results")
print("------------------------------")
print("Total Votes: " +str(total_votes))
print("------------------------------")
print(candidatelist)
print(vote_count)
print("------------------------------")
print("Winner:  ")
print("------------------------------")