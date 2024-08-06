import os
import csv

# csv filepath
csvpath = os.path.join("..", 'Resources', 'budget_data.csv')

total_months = 0
total_value = 0
net_change = []
max_increase = 0
max_decrease = 0
max_month = ""
months = []
profit_losses = []

with open(csvpath, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    first_row = next(csv_reader)
    total_months += 1
    total_value += int(first_row[1])
    previous_value = int(first_row[1])
    profit_losses.append(int(first_row[1]))
        
    for row in csv_reader:
        total_months += 1
        total_value += int(row[1])  # Accumulate the total value correctly
        months.append(row[0])
        current_net = int(row[1]) - previous_value
        previous_value = int(row[1])
        net_change.append(current_net)
        profit_losses.append(int(row[1]))
   
    #calculate average chagne
    average_change = sum(net_change) / len(net_change)  

    # Iterate through the Profit/Losses data to find the greatest increase
    for i in range(1, len(profit_losses)):
        increase = profit_losses[i] - profit_losses[i-1]
       

        if increase > max_increase:
            max_increase = increase
            month = months[i-1]
            max_month_increase = month
        if increase < max_decrease:
            max_decrease = increase
            month = months[i-1]
            max_month_decrease = month
              


print("Total Months:", total_months)
print("Total:", total_value)
print("Average Change:", average_change )
print("Greatest Increase in Profits:", max_month_increase, "($", max_increase, ")" )
print("Greatest Decrease in Profits:", max_month_decrease, "($", max_decrease, ")" )

# Convert an integer to a string
total_months = 86
total_months_str = str(total_months)
total_value = 22564198
total_value_str = str(total_value)
average_change = -8311.105882352942
average_change_str = str(average_change)
max_increase_str = str(max_increase)
max_decrease_str = str(max_decrease)



# Open a file in write mode ('w')
with open("output_PyBank.txt", "w") as file:
    file.write("Total Months: " + total_months_str + "\n")
    file.write("Total: " + total_value_str + "\n")
    file.write("Average Change: " + average_change_str + "\n")
    file.write("Greatest Increase in Profits: " + max_month_increase + " ($" + max_increase_str + ")\n")
    file.write("Greatest Decrease in Profits: " + max_month_decrease + " ($" + max_decrease_str + ")\n")