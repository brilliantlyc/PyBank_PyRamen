# -*- coding: utf-8 -*-
"""PyBank: Financial records analysis.
This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to capture: date, and profit/losses.
It will calculate: total number of months, 
net total amount of profit/losses over the entire period,
average of changes in profit/losses over the entire period,
greatest increase in profits (date and amount) over the entire period,
greatest decrease in losses (date and amount) over the entire period.
"""
# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('Resources/budget_data.csv')

# Initialize the list variable that will hold the budget_data.csv rows
# This will be a nested list containing the rows, and each row will be a sublist
# containing a date value and a profit/losses value
budget_data = []

# Initialize variable to count the total number of months
# which is the same as the total number lines of data
month = 0

# Open the input file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Capture the header of the file in a variable
    header = next(csvreader)
    
    # Read each row of budget data after the header
    for row in csvreader:
        # Append the row to the budget_data list
        budget_data.append(row)
        # Increment the month count by 1
        month += 1
        
# Initialize metric variables
net_total_amount = 0
# Variables to compute the average changes
monthly_change = 0
monthly_changes = []
average_change = 0
# Greatest increase in profits and the date
greatest_increase = 0
greatest_increase_date = ""
# Greatest decrease in losses and the date
greatest_decrease = 0
greatest_decrease_date = ""

# Loop through the budget_data list
for row in budget_data:
    # Calculate the net total amount of profit/losses over the entire period
    # by adding the profit/losses of each row
    net_total_amount += int(row[1])

# Calculate the monthly changes in profit/losses

# Skip the first month as there is no prior month to compute a change
# Loop through the budget_data list starting with the 2nd month and ending with the last month
for i in range(1, month):
    # Calculate the monthly change by obtaining the budget_data's profit/losses value of each month
    # and subtracting the prior month value
    monthly_change = int(budget_data[i][1]) - int(budget_data[i - 1][1])
    monthly_changes.append(monthly_change)
    
    # Compare monthly_change to greatest_increase or greatest_decrease and update metrics
    # To get the dates we access the first value (index = 0) in the current row of the budget_data list
    if monthly_change > greatest_increase:
        greatest_increase = monthly_change
        greatest_increase_date = budget_data[i][0]
    elif monthly_change < greatest_decrease:
        greatest_decrease = monthly_change
        greatest_decrease_date = budget_data[i][0]

# Calculate the average of the changes in profits/losses
# Initialize sum variable to calculate averaage
sum = 0

# Loop through monthly_changes list to add up the changes
for change in monthly_changes:
    sum += change
# Compute average_change
average_change = round(sum / len(monthly_changes), 2)

# Create the lines of text to be output to the terminal and to a text file
# Initialize a list for the output lines
output_lines = []
output_lines.append("Financial Analysis")
output_lines.append("----------------------------")
output_lines.append(f"Total Months: {month}")
output_lines.append(f"Total: ${net_total_amount}")
output_lines.append(f"Average Change: ${average_change}")
output_lines.append(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
output_lines.append(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print the analysis to the terminal and export a text file with the results

# Set the output file path
output_path = Path('output.txt')

# Open the output file for writing
with open(output_path, 'w') as file:
    # Loop through the output_lines list
    for line in output_lines:
        # Print each output line to the terminal
        print(line)
        # Write each output line to the text file
        file.write(line + "\n")

