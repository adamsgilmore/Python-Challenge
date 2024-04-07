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

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

import pandas as pd
df = pd.read_csv(csvpath)

#Command to open file
with open(csvpath) as csvfile:
    # CSV reader to specify delimiter and variable) <-- problem. Need multiple deliminaters for "-" to get months and "," to get values
    csvreader = csv.reader(csvfile, delimiter= ',')
   # ***Only use to Validate data loaded correctly** <- accomplished
    # print(csvreader)
    # Read header row first
    csv_header = next(csvreader)
    # ***Only use to Validate headers loaded correctly** <- accomplished
#print(f"CSV Header: {csv_header}")



## Formatting
    print("Election Results")
    print("-------------------------")


# ****Ouputs... ANALYZE AND CALCULATE THE FOLLOWING STEPS: ****

#pre steps - define candidates and votes
   
   
# DONE! Step 3 Total number of votes cast
    def count_rows(csvpath):
        with open(csvpath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader)
        return row_count
    number_rows = count_rows(csvpath)
    print("Total number of votes cast:", number_rows) 



## Formatting
    print("-------------------------")


# Step 4 Complete list of candidates who recieved votes
 #I want a script to go to through each row of a single column and grab the name
# that script will be a function
    #  I want that function to count how many times a unique name is identifed

# Step 5 percentage of votes each candidate won
def print_string_data(df, column_name):
    column_data = df["Candidate"]
    string_data = column_data[column_data.apply(lambda x: isinstance(x,str))]
    for data in string_data:
        print(data)

        print_string_data(df, 'Candidate')

# Step 6 Total number of votes each candidate won

## Formatting
# print Candidate + percentage + number of votes
    print("-------------------------")

# Step 7  Winner of election based on popular vote
## Formatting
    print("-------------------------")
        