#import os module & module for reading csv file
import os
import csv

# csv filepath
csvpath = os.path.join("..", 'Resources', 'budget_data.csv')
#empty variables for tracking paramaters
total_months = 0
total_value = 0
month_of_change = []
greatest_increase = ["", 0] # Date remains as a string
greatest_decrease = ["", 9999999999999999999] # Date remains as a string
net_change = []
#net change and month of change need to work together to get the date for the greatest
#increase and decrease

#greatest_increase = ["", 0]
#greatest_decrease = ["", 9999999999999999999]

with open('budget_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists
    
    first_row = next(csv_reader) #first row is second row in data frame
    total_months += 1 #total month counter can increase by 1 b/c each row is a month
    total_value += int(first_row[1])  #first row(2 row of data) reference cell with actual value
    previous_value = int(first_row[1])   #need to store previous value and use it with next value

    for row in csv_reader:
        # Assuming the date/month is in a specific column, replace the index below
        total_months += 1  # Adjust the index based on your CSV file
        total_value += int(row[1])
        current_net = int(row[1]) - previous_value 
        previous_value = int(row[1]) 
        net_change.append(current_net)
        month_of_change.append(row[0])
        
        if current_net > greatest_increase[1]:
            greatest_increase[0] = row[0]  # Store the date as a strin
            greatest_increase[1] = current_net

        if current_net < greatest_decrease[1]:
            greatest_decrease[0] = row[0]  # Store the date as a string
            greatest_decrease[1] = current_net


total_months = len(month_of_change)

print("Total Months:", total_months)

total_value = sum(net_change)

print("Total:", total_value)

