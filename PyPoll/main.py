#!/usr/bin/env python
# coding: utf-8

# In[288]:


# Modules
import os
import csv


# In[289]:


# Set path for file
csvpath = os.path.join("election_data.csv")


# In[290]:


# Open the CSV

count_votes = 0
candidates = []
votes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the titles of the file
    next(csvreader)
    for row in csvreader:
        # Counts the number of votes
        count_votes += 1
        # Verifies if the candidate does not exist
        if (row[2] in candidates) == False: 
            # Add the candidate to the list
            candidates.append(row[2]) 
            # Add a position in the list of votes to count them
            votes.append(0) 
            
        # Looks for the index of the candidate of the loop in the list of candidates
        index = candidates.index(row[2]) 
        # Adds a vote in the list of votes in the same order than the list of candidates
        votes[index] += 1


# In[291]:


# Calculates the percentage of votes and stores it to a list using comprehensions
votes_percentage = [vote / count_votes for vote in votes]


# In[292]:


# Calculates the winner
max([100,2,110,4,5,110])
# Max number of votes
max_votes = max(votes)
# Index of max number of votes
index_max_votes = votes.index(max_votes)
# Return the candidate with max number of votes
winner = candidates[index_max_votes]


# In[293]:


# Print the results
print('Election Results')
print('--------------------------------------')
print(f'Total Votes:    100.00%\t {count_votes:0,.0f}')
print('--------------------------------------')
for x in range(len(candidates)):
  print(f'{candidates[x]}      \t{votes_percentage[x]:.2%}\t({votes[x]:0,.0f})')
print('--------------------------------------')
print(f'Winner: \t{winner}')
print('--------------------------------------')


# In[297]:


# Method 1: Same as output on screen
# Set variable for output file
output_file = os.path.join("Results_Screen.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('--------------------------------------\n')
    datafile.write(f'Total Votes:    100.00%\t {count_votes:0,.0f}\n')
    datafile.write('--------------------------------------\n')
    for x in range(len(candidates)):
        datafile.write(f'{candidates[x]}      \t{votes_percentage[x]:.2%}\t({votes[x]:0,.0f})\n')
    datafile.write('--------------------------------------\n')
    datafile.write(f'Winner: \t{winner}\n')
    datafile.write('--------------------------------------\n')
print (f'Method 1: The file "{output_file}" has been created with the results')   


# In[295]:


# Save the results to a file
# Method 2: Save csv file Line by Line
# Set variable for output file
output_file = os.path.join("Results_Line_by_Line.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(['Election Results', '', ''])
    csvwriter.writerow(['------------------', '', ''])
    csvwriter.writerow(['Total Votes', "%.0f" % count_votes, ''])
    csvwriter.writerow(['------------------', '', ''])
    for x in range(len(candidates)):
        csvwriter.writerow([candidates[x], "%.2f%%" %  (votes_percentage[x]*100) , "%.0f" % votes[x] ])
    csvwriter.writerow(['------------------', '', ''])
    csvwriter.writerow(['Winner', winner, ''])    
    csvwriter.writerow(['------------------', '', ''])
print (f'Method 2: The file "{output_file}" has been created with the results')   


# In[296]:


# Method 3: Save csv file using dictionaries
# Creates a dictionary with the basic information
election_results = {
    "Total Votes": "%.0f" % count_votes,
    "Winner" : winner
}
# Adds number of votes per candidate to the dictionary
for x in range(len(candidates)):
    election_results.update({(candidates[x] + " Votes"): "%.0f" % votes[x]})
# Adds percentage of votes to the dictionary
for x in range(len(candidates)):
    election_results.update({(candidates[x] + " Percentage"): ("%.2f%%" %  (votes_percentage[x]*100))})
    
# Set variable for output file
output_file = os.path.join("Results_Dictionary.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    for row in election_results.items():
        csvwriter.writerow([row[0],row[1]])
print (f'Method 3: The file "{output_file}" has been created with the results')   

