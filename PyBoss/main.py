#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Modules
import os
import csv
import datetime


# In[83]:


# Set path for file
csvpath = os.path.join("employee_data.csv")


# In[84]:


# Open the CSV

emp_id = []
name = []
dob = []
ssn = []
state = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the titles of the file
    next(csvreader)
    for row in csvreader:
        emp_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
        # print (row)


# In[85]:


# US States Dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[86]:


# Modify through comprenhensions
new_emp_id = [employee for employee in emp_id]
new_name =[employee.split(' ', 1)[0] for employee in name]
new_last_name = [employee.split(' ', 1)[1] for employee in name]
#new_dob = [employee for employee in dob]
# Convert the text to date
new_dob = [datetime.datetime.strptime(employee, "%Y-%m-%d") for employee in dob]
# Convert the date to a specific format - Needs to have brackets to make it work
new_dob = [datetime.datetime.strftime(employee, "%m-%d-%Y") for employee in new_dob]
new_ssn = [("***-**-" + employee[-4:]) for employee in ssn]
new_state = [us_state_abbrev.get(employee) for employee in state]


# In[87]:


# Zip all three lists together into tuples
new_employee_data = zip(new_emp_id, new_name, new_last_name, new_dob, new_ssn, new_state)


# In[88]:


#Set variable for output file
output_file = os.path.join("employee_data_modified.csv")
        
# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    # write the zipped object to the csv
    csvwriter.writerows(new_employee_data)


# In[ ]:




