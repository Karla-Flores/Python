import os
import csv
csvpath = os.path.join("/Users/karlaflores/Desktop/Git/Python----Challenge/PyBank/Resources/budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader,None)
    #print(f"CSV Header: {csv_header}")

    # Lists for storing
    Profit = []
    Months = []
    Total = []
        
    #Variables
    # Total of months
    count = 0
    # Sum profit / losses
    total = 0
    # Last month profit / losses
    lmonth_profit = 0
    # Actual month profit / losses
    amonth_profit = 0

    
    # Read each row of data after the header
    for row in csvreader:
        # Counts of months in csvreader
        count = count + 1
        # Sum profit and losses
        Total.append(int(row[1]))
        total = sum(Total)  
        # Actual month
        amonth_profit = int(row[1])
        # First part of the average
        if (count == 1):
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

# Average of change - Final result
sump = sum(Profit)
Avg = round(sump/(count - 1),2)

#Greatest Increase in Profits / Date
increase = max (Profit)
increase_index = Profit.index(increase)
increse_date = Months[increase_index]
#Greatest Decrease in Profits / Date
decrease = min(Profit)
decrease_index = Profit.index(decrease)
decrese_date = Months[decrease_index]

print ("Financial Analysis")
print ("---------------------------------------------------\n")
print (f"Total Months: {count}")
print (f"Total: $ {total: ,}")
print (f"Average Change: $ {Avg: ,} ")
print (f"Greatest Increase in Profits: {increse_date}  ({increase:,})")
print (f"Greatest Decrease in Profits: {decrese_date}  ({decrease:,})")
