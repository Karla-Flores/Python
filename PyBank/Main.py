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
    Months = []
        
    #Variables
    # Total of months
    count = 0
    # Total sum of profit / losses
    total = 0
    # Last month profit / losses
    lmonth_profit = 0
    # Actual month profit / losses
    amonth_profit = 0
    # Net value profit / losses
    net_profit = 0
    

    
    # Read each row of data after the header
    for row in csvreader:
        # Counts of months in csvreader
        count = count + 1

        amonth_profit = int(row[1])
        net_profit= amonth_profit + 1
        if (count== 1):
            # Define last month to be the actual one
            lmonth_profit = amonth_profit
            continue
        else:
            # Calculate profit / losses change
            c_profit = amonth_profit - lmonth_profit
            
            # Add change profit to list Months
            Months.append(row[0])

            # Add profit / losses change to a list Profit
            Profit.append(c_profit)

            # Now current month will be the previous one
            lmonth_profit = amonth_profit

#
sump = sum(Profit)
Avg = round(sump/(count - 1),2)
                
print ("Financial Analysis")
print ("----------------------------\n")
print ("Total Months: " + str(count))
print ("Total: $" + str(net_profit))
print ("Average Change: $" + str(Avg))
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")