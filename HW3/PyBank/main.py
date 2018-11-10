import os
import csv
import numpy as np

# get the path of the file
pathfile = os.path.join('Homeworks_HW03-Python_PyBank_Resources_budget_data.csv')

# initialize the variables
max_increase = 0
max_decrease = 0
tot_month = 0
tot_value = 0
previous_value = 0
change = []
month = []

with open(pathfile, encoding = 'utf-8') as file:
    reader = csv.reader(file,delimiter = ',')
    header = next(reader)
    for row in reader:
        month.append(row[0])
        tot_month += 1
        row[1] = int(row[1])
        tot_value += row[1]
        if previous_value != 0:
            change.append(row[1]-previous_value)
        previous_value = row[1]

# find the average
avg_chg = round(sum(change)/len(change),2)
max_increase = max(change)
max_index = change.index(max(change)) + 1
max_decrease = min(change)
min_index = change.index(min(change)) + 1

with open(os.path.join('output.csv'),'w') as file:
    print('Financial Analysis\n----------------------------')   
    file.write('Financial Analysis\n---------------------------\n')
    print(f'Total Months: {tot_month}')
    print(f'Total : ${tot_value}')
    print(f'Average  Change: ${avg_chg }')
    file.write(f'Total Months: {tot_month}\nTotal : ${tot_value}\nAverage  Change: ${avg_chg}\n')
    print(f'Greatest Increase in Profits: {month[max_index]} (${max_increase})' )
    print(f'Greatest Decrease in Profits: {month[min_index]} (${max_decrease})' )
    file.write(f'Greatest Increase in Profits: {month[max_index]} (${max_increase})\n')
    file.write(f'Greatest Decrease in Profits: {month[min_index]} (${max_decrease})')