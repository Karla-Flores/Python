# First we'll import the os module and create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('/Users/karlaflores/Desktop/Git/Python----Challenge/PyBank/Resources/budget_data.csv')

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


        
    # Lists for storing
    profit = []
    changes = []
    date = []
        
    #V ariables
    count = 0

    # Read each row of data after the header
    for row in csvreader:
        # Counts of months in csvreader
        count = count + 1
        # Storage profit in list
        profit.append(int(row[1]))
    print (profit)
        
print ("Financial Analysis")
print ("----------------------------\n")
print ("Total Months: " + str(count))