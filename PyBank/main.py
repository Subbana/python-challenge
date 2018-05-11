#import module
import os
import csv
#set up the path
csvpath1 = os.path.join('..', 'resource', 'budget_data_1.csv')
# lists to store data
date1 = []
revenue1 = []
change1 = []

# Use method 2: Improved Reading using CSV module
with open(csvpath1, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader1 = csv.DictReader(csvfile, delimiter=',')
    #  Each row is read as a row
    for row in csvreader1:
        date1.append(row["Date"])
        revenue1.append(int(row["Revenue"]))
# total month
total_month1 = len(date1)
# total revenue
total_revenue1 = sum(revenue1)
# find the change
lastrow1 = len(revenue1) - 1
for x in range(0, lastrow1):
    change_1 =int(revenue1[x + 1] - revenue1[x])
    change1.append(change_1)
#find average revenue change
total_change1 = sum(change1)
average_change1 = (total_change1)/(len(date1) - 1)
#find the greatest change
max_value1 = max(change1)
# find the index
max_index1 = change1.index(max_value1) + 1
#find the date
max_date1 = date1[max_index1]
#find the leastest chagne
min_value1 = min(change1)
#find the index
min_index1 = change1.index(min_value1) + 1
#find the date
min_date1 = date1[min_index1]

# do the same for file 2
csvpath2 = os.path.join('..', 'resource', 'budget_data_2.csv')
#list to store data
date2 = []
revenue2 = []
change2 = []
with open(csvpath2, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.DictReader(csvfile, delimiter=',')
    #  Each row is read as a row
    for row in csvreader2:
        date2.append(row["Date"])
        revenue2.append(int(row["Revenue"]))
# total month
total_month2 = len(date2)
# total revenue
total_revenue2 = sum(revenue2)
# find the change
lastrow2 = len(revenue2) - 1
for x in range(0, lastrow2):
    change_2 =int(revenue2[x + 1] - revenue2[x])
    change2.append(change_2)
#find average revenue change
total_change2 = sum(change1)
average_change2 = (total_change2)/(len(date2) - 1)
#find the greatest change
max_value2 = max(change2)
# find the index
max_index2 = change2.index(max_value2) + 1
#find the date
max_date2 = date2[max_index1]
print(max_date2)
#find the leastest chagne
min_value2 = min(change2)
#find the index
min_index2 = change2.index(min_value2) + 1
#find the date
min_date2 = date2[min_index2]

# print everything
print('Financial Analysis')
print('--------------------------------')
print('For first data:')
print('Total Months: ', total_month1)
print('Total Revenue: $', total_revenue1)
print('Average Revenue Change: $', average_change1)
print('Greatest Increase in Revenue: ' +str(max_date1)+'($'+ str(max_value1) + ')' )
print('Greatest Increase in Revenue: ' +str(min_date1)+'($'+ str(min_value1) + ')' )
print('')
print('For second data:')
print('Total Months: ', total_month2)
print('Total Revenue: $', total_revenue2)
print('Average Revenue Change: $', average_change2)
print('Greatest Increase in Revenue: ' +str(max_date2)+'($'+ str(max_value2) + ')' )
print('Greatest Increase in Revenue: ' +str(min_date2)+'($'+ str(min_value2) + ')' )


