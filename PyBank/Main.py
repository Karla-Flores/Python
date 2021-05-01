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
    Profit = []
    Change = []
    Date = []
        
    #V ariables
    count = 0
    total = 0
    i_profit = 0

    # Read each row of data after the header
    for row in csvreader:
        # Counts of months in csvreader
        count = count + 1
        # Storage Profit in list
        Profit.append(int(row[1]))
        # Storage Date in list
        Date.append(str(row[0]))
        # Sum of profit & losses
        total = total + int(row[1])
        # Average of change
        f_profit = int(row[1])
        m_change = f_profit - i_profit
        Change.append(m_change)
print (Change)
print (f_profit)
print (m_change)

        
print ("Financial Analysis")
print ("----------------------------\n")
print ("Total Months: " + str(count))
print ("Total: $" + str(total))
print ("Average Change: $")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")