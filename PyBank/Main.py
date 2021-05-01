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
    t_changep = 0

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
        # Last profit value
        f_profit = int(row[1])
        # Average of change / wrong
        m_change = f_profit - i_profit
        Change.append(m_change)
        t_changep = t_changep + m_change
        avg = t_changep / count
        # Increase/ wrong
        increase = max (Change)
        idate = Date[Change.index(increase)]
        # Decrease / wrong
        decrease = min (Change)
        ddate = Date[Change.index(decrease)]

#print (f_profit)
#print (Change)
        
print ("Financial Analysis")
print ("----------------------------\n")
print ("Total Months: " + str(count))
print ("Total: $" + str(total))
print ("Average Change: $" + str(avg))
print ("Greatest Increase in Profits: " + str(idate) + " " + str(increase))
print ("Greatest Decrease in Profits: " + str(ddate) + " " + str(decrease))