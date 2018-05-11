#import module
import os
import csv
#set up the path
csvpath = os.path.join('..','resource', 'election_data_1.csv')
# lists to store data
voter_id = []
county = []
candidate_total = []
candidate_unique = []
vote_frequency = []
with open(csvpath, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #  Each row is read as a row
    for row in csvreader:
        candidate_total.append(row["Candidate"])
# get candidate name 
candidate_unique = list(set(candidate_total))
candidate1 = (candidate_unique[0])
candidate2 = (candidate_unique[1])
candidate3 = (candidate_unique[2])
candidate4 = (candidate_unique[3])
# find out the votes number for the name
import collections
counter=collections.Counter(candidate_total)
vote1 = counter[candidate1]
vote2 = counter[candidate2]
vote3 = counter[candidate3]
vote4 = counter[candidate4]
# total vote
vote_total = len(candidate_total)
# percentage
percent1 = (vote1 / vote_total) * 100
percent2 = (vote2 / vote_total) * 100
percent3 = (vote3 / vote_total) * 100
percent4 = (vote4 / vote_total) * 100
#Find the winter
if (vote1 > vote2) and (vote1 > vote3):
    winnter_candidate = candidate1
elif vote2 > vote3:
    winnter_candidate = candidate2
else:
    winnter_candidate = candidate3

# print everything
print("Election Results")
print("---------------------------")
print("total Votes: ", vote_total)
print("---------------------------")
print(str(candidate1)+': '+ str(percent1) + '%(' + str(vote1) + ')')
print(str(candidate2)+': '+ str(percent2) + '%(' + str(vote2) + ')')
print(str(candidate3)+': '+ str(percent3) + '%(' + str(vote3) + ')')
print(str(candidate4)+': '+ str(percent4) + '%(' + str(vote4) + ')')
print('----------------------------')
print('Winnter: ', winnter_candidate)
print('----------------------------')


# Do the same for file2
#set up the path
csvpath = os.path.join('..','resource', 'election_data_2.csv')
# lists to store data
voter_id = []
county = []
candidate_total = []
candidate_unique = []
vote_frequency = []
with open(csvpath, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #  Each row is read as a row
    for row in csvreader:
        candidate_total.append(row["Candidate"])
# get candidate name 
candidate_unique = list(set(candidate_total))
candidate1 = (candidate_unique[0])
candidate2 = (candidate_unique[1])
candidate3 = (candidate_unique[2])
candidate4 = (candidate_unique[3])
# find out the votes number for the name
import collections
counter=collections.Counter(candidate_total)
vote1 = counter[candidate1]
vote2 = counter[candidate2]
vote3 = counter[candidate3]
vote4 = counter[candidate4]
# total vote
vote_total = len(candidate_total)
# percentage
percent1_raw = (vote1 / vote_total) * 100
percent2_raw = (vote2 / vote_total) * 100
percent3_raw = (vote3 / vote_total) * 100
percent4_raw = (vote4 / vote_total) * 100
# format
percent1 = format(percent1_raw,'.2f')
percent2 = format(percent2_raw,'.2f')
percent3 = format(percent3_raw,'.2f')
percent4 = format(percent4_raw,'.2f')
#Find the winter
if (vote1 > vote2) and (vote1 > vote3):
    winnter_candidate = candidate1
elif vote2 > vote3:
    winnter_candidate = candidate2
else:
    winnter_candidate = candidate3

# print everything
print("")
print("Second Election Results: ")
print("---------------------------")
print("total Votes: ", vote_total)
print(str(candidate1)+': '+ str(percent1) + '%(' + str(vote1) + ')')
print(str(candidate2)+': '+ str(percent2) + '%(' + str(vote2) + ')')
print(str(candidate3)+': '+ str(percent3) + '%(' + str(vote3) + ')')
print(str(candidate4)+': '+ str(percent4) + '%(' + str(vote4) + ')')
print('----------------------------')
print('Winnter: ', winnter_candidate)
print('----------------------------')


