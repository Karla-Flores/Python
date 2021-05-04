# First we'll import the os module and create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('/Users/karlaflores/Desktop/Git/Python----Challenge/PyPoll/Resources/election_data.csv')


# List
Candidate = []
c_candidate = []
countvotes = []
# Variable
count = 0

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader, None)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #Count of votes
        count = count + 1
        Candidate.append(row[2])
        # Loop Candidate as a set in order to not allow duplicates
    for x in set(Candidate):
        c_candidate.append(x)
        # Count total of votes for each candidate
        countvotes = Candidate.count(x)
        # Create a new variable for %
        pervotes = (countvotes/count)*100
        


        

print ("Election Results")
print ("-------------------------\n")
print ("Total Votes: " + str(count))
print ("-------------------------\n")
print ("Khan: ")
print ("Correy: ")
print ("Li: ")
print ("O'Tooley: ")
print ("-------------------------\n")
print ("Winner: ")
print ("-------------------------\n")