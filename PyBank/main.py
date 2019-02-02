import os
import csv

'''
This code reads a .csv file containing monthly entries of profit/loss
and calculates the net profit(loss); finds the maximum monthly profit
and the maximum monthly loss. Finally, it prints out a financial
summary report.
'''

filepath = 'budget_data.csv'

month_year = []
amount = []


with open(filepath, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    # Build two arrays: (1) month-year array (2) array with corresponding Profit/loss
    for line in reader:
        month_year.append(line[0]) # building array of strings (month-year)
        amount.append(line[1]) # building array of strings (profit/loss)

# Count the total number of months in the report
num_months = len(month_year)-1

# Transform an array with profit loss from string format to integer format
profit_loss_arr = [int(item) for item in amount[1:len(month_year)]]

# Calculate the net profit(or loss)
total_amount = sum(profit_loss_arr)

# Calculate the average Profit/Loss per months
average = total_amount/num_months

# find maximum and minimum changes in a single month
maxincrease = max(profit_loss_arr)
maxdecrease = min(profit_loss_arr)

# find array indices corresponding to the minimum and maximum monthly changes
hi_ind = profit_loss_arr.index(maxincrease)
lo_ind = profit_loss_arr.index(maxdecrease)

# Print the financial report
print('')
print('Financial Analysis')
print('-----------------------------------------------')
print(f'Total month: {num_months}')
print(f'Total: ${total_amount}')
print(f'Greatest Increase in Profits: {month_year[hi_ind+1]} (${maxincrease})')
print(f'Greatest Decrease in Profits: {month_year[lo_ind+1]} (${maxdecrease})')