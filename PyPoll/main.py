# Pre Steps   <see Day 3, ~90 minute mark>
    # *DONE!* Create new repository "python-challenge"
    # *Done!* Clone to Computer
    # *Done!* Inside local git reponsitory, create folder for each assignment, "PyBank" & PyPoll
        # In each folder, add:
        # New File "main.py"
        # "Resources" folder to hold CSV
        # "Analysis" folder containing text file of results
  # *NOT DONE* Push changes to GitHub or GitLab

# STEP 1 - PSEUDO-CODE 
# STEP 2-  IMPORT CSV & Store header (Day 2, ~50 minutes into class)
    # File path
import os
    # Module for reading CSV
import csv

#Establishing CSV location


# Candidate Count by vote - setting the counter to zero
#Charles Casper Stockham
Stockham_Counter = 0
DeGette_Counter = 0
Doane_Counter = 0
Vote_Counter = 0
candidate_votes = {}

# {} creates a dictionary, [] creates an empty list

#Placeholder for candidate winner. Needs to be a name
candidate_winner = ''

csv_path = os.path.join('Resources\\election_data.csv')

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
   #this will skip the header row so we don't count it when the code counts candidates
    next(csv_reader)
    for row in csv_reader:  
        
        #Count number of votes
        Vote_Counter = Vote_Counter + 1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

# print(Vote_Counter)
# print(candidate_votes)

# getting share of each word
# this sums up the votes and divides each candidate total by the total total (i.e the percentage)
candidate_percentages = {key: val / Vote_Counter for key, val in candidate_votes.items()}
candidate_perc={}
vote_check = 0
for key, value in candidate_votes.items():

    candidate_perc[key] = round(value/Vote_Counter *100, 3)
    if value > vote_check:
        vote_check = value
        candidate_winner = key

# print(candidate_percentages)
# print(candidate_perc)
# print(candidate_winner)

#Printing script to text file
csv_output_path = os.path.join('Analysis\\election_analysis.txt')

with open(csv_output_path, 'w') as output_file:
#note, python backslack means "next line"

    election_output_1 = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {Vote_Counter}\n"
    f"-------------------------\n")
    print(election_output_1)
    output_file.write(election_output_1)

    for key, value in candidate_votes.items():
        election_output_2 = f"{key}: {candidate_perc[key]}% ({value})\n"
    
        print(election_output_2)
        output_file.write(election_output_2)

    election_output_3 = (
    f"-------------------------\n"
    f"Winner: {candidate_winner}\n"
    f"-------------------------")

    print(election_output_3)
    output_file.write(election_output_3)



 


