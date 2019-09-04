#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Modules
import os
import csv


# In[49]:


# Set path for file
csvpath = os.path.join("budget_data.csv")


# In[50]:


# Open the CSV
count_months = 0
sum_profit = 0
change = 0
last_profit = 0
average_change = 0
max_change = 0
min_change = 100000000

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the titles of the file
    next(csvreader)
    for row in csvreader:
        # Counts the number of months
        count_months += 1
        # Summarizes the total of profits
        sum_profit  += float(row[1])
        if count_months == 1:
            # print(row[0], row[1], last_profit, change, average_change)
            last_profit = float(row[1])
        else:
            # Calculates the change in profits and cumulates the
            # value to calculate the average
            change = float(row[1]) - last_profit
            average_change += change
            #print(row[0], row[1], last_profit, change, average_change)
            last_profit = float(row[1])
        # Keeps track of the greatest increase in profits
        if change > max_change :
            max_change = change
            max_change_date = row[0]
        # Keeps track of the greatest decrease in profits
        if change < min_change :
            min_change = change
            min_change_date = row[0]
# Calculates the average with the total change divided by the number of 
# months, excluding the first row that does not contained any changes
average_change = average_change / (count_months-1)


# In[51]:


print('Financial Analysis')
print('----------------------------------------------------------------------------------')
print(f'Total Months:\t\t\t{count_months}')
print(f'Average Change: \t\t${average_change:0,.2f}')
print(f'Total: \t\t\t\t${sum_profit:0,.0f}')
print(f'Greatest Increase in Profits:\t{max_change_date} \t(${max_change:0,.0f})')
print(f'Greatest Increase in Profits: \t{min_change_date} \t(${min_change:0,.0f})')


# In[68]:


# Method 1: Same as output on screen
# Set variable for output file
output_file = os.path.join("Results_Screen.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:  
    datafile.write('Financial Analysis\n')
    datafile.write('----------------------------------------------------------------------------------\n')
    datafile.write(f'Total Months:\t\t\t{count_months}\n')
    datafile.write(f'Average Change: \t\t${average_change:0,.2f}\n')
    datafile.write(f'Total: \t\t\t\t${sum_profit:0,.0f}\n')
    datafile.write(f'Greatest Increase in Profits:\t{max_change_date} \t(${max_change:0,.0f})\n')
    datafile.write(f'Greatest Increase in Profits: \t{min_change_date} \t(${min_change:0,.0f})')

print('----------------------------------------------------------------------------------')
print (f'Method 1: The file "{output_file}" has been created with the results')   


# In[52]:


# Method 2: Save csv file Line by Line
# Set variable for output file
output_file = os.path.join("Results_Line_by_Line.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(['Financial Analysis', '', ''])
    csvwriter.writerow(['------------------', '', ''])
    csvwriter.writerow(['Total Months', count_months, ''])
    csvwriter.writerow(['Average Change', "%.2f" % average_change, ''])
    csvwriter.writerow(['Greatest Increase in Profits', max_change_date, "%.0f" % max_change])
    csvwriter.writerow(['Greatest Decrease in Profits', min_change_date, "%.0f" % min_change])

print('----------------------------------------------------------------------------------')
print (f'Method 2: The file "{output_file}" has been created with the results')


# In[63]:


# Method 3: Save csv file using dictionaries

financial_analisys = {
    "Total Months": count_months,
    "Average Change": "%.2f" % average_change,
    "Date of Greatest Increase in Profits" : max_change_date,
    "Greatest Increase in Profits" : "%.0f" % max_change,
    "Date of Greatest Decrease in Profits" : min_change_date,
    "Greatest Decrease in Profits" : "%.0f" % min_change
}

# Set variable for output file
output_file = os.path.join("Results_Dictionary.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    for row in financial_analisys.items():
        csvwriter.writerow([row[0],row[1]])
print('----------------------------------------------------------------------------------')
print (f'Method 3: The file "{output_file}" has been created with the results')
print('----------------------------------------------------------------------------------')

