# First we'll import the os module and create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('/Users/karlaflores/Desktop/Git/Python----Challenge/PyPoll/Resources/election_data.csv')


# List
Candidate = []
c_candidate = []
CountVotes = []
PerVotes = []
# Variable
count = 0
countvotes = 0
pervotes = 0

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader,None)
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
        CountVotes.append(countvotes)
        # Create a new variable for %
        pervotes = ((countvotes/count)*100)
        PerVotes.append(pervotes)
winner_max = max(CountVotes)
winner = c_candidate[CountVotes.index(winner_max)]   
#Round float to 3 decimals   
f_Pervotes = ['%.3f' % elem for elem in PerVotes]

print (f"Election Results")
print (f"-------------------------")
print (f"Total Votes: {count}")
print (f"-------------------------")
# Create Output to sort list then reverse it and print it
#Output = sorted(PerVotes, key = lambda x:float(x))
#Output.sort(reverse= False)
#print(Output)
for x in range(len(c_candidate)):
    print (f"{c_candidate[x]} : {(f_Pervotes[x])}%  ({CountVotes[x]})\n")

print ("-------------------------")
print (f"The winner is: {winner}")
print ("-------------------------")

#Export TXT file
PollResuls_file = os.path.join("/Users/karlaflores/Desktop/Git/Python----Challenge/PyPoll/Output/PollResuls_txt")
with open(PollResuls_file, "w") as outfile:
#Outfile each line to print and use \n to go to other row
    outfile.write(f"Election Results\n")
    outfile.write(f"---------------------------------------------------\n")
    outfile.write(f"Total Votes: {count}\n")
    outfile.write(f"---------------------------------------------------\n")
    for x in range(len(c_candidate)):
        outfile.write(f"{c_candidate[x]} : {(f_Pervotes[x])}%  ({CountVotes[x]})\n")
    outfile.write(f"---------------------------------------------------\n")
    outfile.write(f"The winner is: {winner}\n")
    outfile.write(f"---------------------------------------------------\n")
    