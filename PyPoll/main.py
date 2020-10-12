#import my needed modules
import os
import csv

# connect the csv path to Python so I can write my code
csvpath = os.path.join ("Resources", "election_data.csv")

#create the path to send a txt file to the repository
outpath = os.path.join ("Analysis", "election_data.txt")
#A. total votes cast
#B. unique candidates list
#C. total number of votes each candidate got
#D. percentage of candidates
#E. the winner of the election based on popular vote
#voterid, county, candidate
#1, county_a, candidate-a
#2, county_a, candidate_a
#3, county_b, candidate_b

with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")
    #create the dictionary
    candidates_list = (
        "Khan",
        "Correy",
        "Li",
        "O'Tooley",
    )
    #set my variables
    vote_count=0
    total_votes=1
    total=0
    totaluniqueKhan=0
    totaluniqueCorrey=0
    totaluniqueLi=0
    totaluniqueotooley=0
    greatestvotecount=0
    greatvotewinner=""
   
    
    for row in csvreader:
        total = total - 1
        total_votes = total-1
     # for row in reader:
    #for A what will we do? sum the total number of rows
        #total_votes +=1
   
     #  For unique candidates 
    #all_candidate_with_duplicate.append(row[2])
    #candidates_list = (Candidate)
    #x = dict_candidates["Candidate"]

    totaluniqueKhan.count
    #count = 0
    #all_candidate_with_duplicate + []
    #create a dictionary
    #candidate_totals = {}

#with open file to load as poll_csv
    #reader = csv (poll_csv)

    #discard header if you want
    #next on the reader object

    #the goal is to loop everything once
 
#    For unique candidates 
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
   
#display my results
print("Election Results")
print("------------------------------")
print("Total Votes: " +str(total_votes))
print("------------------------------")
print("Khan: " +str(totaluniqueKhan))
print("------------------------------")
print("Winner:  ")
print("------------------------------")