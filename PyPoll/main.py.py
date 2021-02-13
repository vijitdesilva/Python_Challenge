# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:17:31 2021

@author: Viji
"""

import os
import csv

total_vote_count = 0
votes = []
candidatesList = []


csvpath = os.path.join("..", "PyPoll", "Resources","election_data.csv")

with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
# use csv_header = next(csv_file) (Because there is a header in CSV file )
    csv_header = next(csv_reader) 


    for row in csv_reader:
        #if i [-1] not in candidatesList: 
        total_vote_count = total_vote_count + 1
        candidate = row[2]
        if candidate in candidatesList:
            candidate_index = candidatesList.index(candidate)
            votes[candidate_index] = votes[candidate_index] + 1 
        else:
            candidatesList.append(candidate)
            votes.append(1)


percentages = []
max_vote_count = votes[0]
max_vote_index = 0       
for count in range(len(candidatesList)):
    vote_percentage = votes[count]/total_vote_count*100
    percentages.append(vote_percentage)
    
    if votes[count] > max_vote_count:
        print(max_vote_count)
        max_vote_index = count
winner = candidatesList[max_vote_index]
percentages = [round(i,3) for i in percentages]

print("\nElection Results\n---------------------")
print(f"Total Votes: {total_vote_count}")
print("\n---------------------------------------")
for count in range(len(candidatesList)):
    print(f"{candidatesList[count]}: {percentages[count]}% ({votes[count]})")
print("\n---------------------------------------")
print(f"Winner: {winner}")
print("\n---------------------------------------")


with open('Election_Results.txt', 'w') as text:
    text.write("Election Results " + "\n")
    text.write(" --------------------------------\n")
    text.write("Total Votes: " + str(total_vote_count) +  "\n")
    text.write("---------------------------------\n")
    for count in range(len(candidatesList)):
        text.write(f"{candidatesList[count]}: {percentages[count]}% ({votes[count]})" + "\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + (winner) + "\n")
    text.write("--------------------------------------\n")
    text.close()









 