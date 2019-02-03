import os
import csv

'''
main.py reads the "budget_data.csv" file with the monthly entries of profits and losses.
It calculates the net profit(or loss), finds the maximum profit
and the maximum loss, as well as which months they occured. 
Finally, main.py prints out a financial summary report to the terminal 
and saves the summary as a text file ("output.txt")
'''

filepath = 'budget_data.csv'

month_year = []
amount = []


with open(filepath, 'r') as file:
    reader = csv.reader(file, delimiter = ',')

    # Build two arrays: (1) month-year array (2) array with corresponding monthly profit/loss
    for line in reader:
        month_year.append(line[0]) # building array of strings (month-year)
        amount.append(line[1]) # building array of strings (profit/loss)



def extract_data(month_year, amount):
    '''
    Function extract_data() takes two arrays as an input:
    - array of months
    - array of loss/profit during these months

    extract_data() returns total number of records (num_months), net profit/loss (total_amount),
    position of greatest increase record (hi_ind), osition of greatest decrease record (lo_ind),
    the greatest monthly increase (maxincrease), the greatest monthly decrease (maxdecrease)
    
    '''
    num_months = len(month_year)-1

    # Transform an array with profit loss from string format to integer format
    profit_loss_arr = [int(item) for item in amount[1:len(month_year)]]

    # Calculate the net profit(or loss)
    total_amount = sum(profit_loss_arr)

    # Calculate the average Profit/Loss per months
    average = round(total_amount/num_months)

    # find maximum and minimum changes in a single month
    maxincrease = max(profit_loss_arr)
    maxdecrease = min(profit_loss_arr)

    # find array indices corresponding to the minimum and maximum monthly changes
    hi_ind = profit_loss_arr.index(maxincrease)
    lo_ind = profit_loss_arr.index(maxdecrease)

    return average, num_months, total_amount, hi_ind, lo_ind, maxincrease, maxdecrease

def report(average, num_months, total_amount, hi_ind, lo_ind, maxincrease, maxdecrease):
    return [f'\n',f'Financial Analysis\n',
        '-----------------------------------------------\n',
        f'Total months: {num_months}\n',
        f'Total: ${total_amount}\n',
        f'Average Change: ${average}\n'
        f'Greatest Increase in Profits: {month_year[hi_ind+1]} (${maxincrease})\n',
        f'Greatest Decrease in Profits: {month_year[lo_ind+1]} (${maxdecrease})\n']

average, num_months, total_amount, hi_ind, lo_ind, maxincrease, maxdecrease = extract_data(month_year, amount)

#Create an output.txt file
with open('output.txt', 'w+') as file:
    text=report(average, num_months, total_amount, hi_ind, lo_ind, maxincrease, maxdecrease)

    # Write summary data into the output.txt file and print it to the therminal
    for line in text:
        print(line.strip('\n'))
        file.write(line)