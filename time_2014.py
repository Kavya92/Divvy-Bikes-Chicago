# Importing packages
import csv
import pandas as pd

#Specifying paths to open the csv files which were merged
path1 = 'C:/Users/uamul/Desktop/kavya/output.csv'
path2 = 'C:/Users/uamul/Desktop/kavya/output1.csv'

#lists declared
start_date = []
start_hours = []
stop_date = []
stop_hours = []
start_h =[]
start_m = []
stop_h =[]
stop_m = []
timeValues = []
time = dict()



for i in range(0,24):                                                   #intializing dictionary keys to hours ranging from 0 to 23
    time.setdefault(i)
for key in time.keys() :                                                #initializing the values to Zero
    time[key] = 0

with open(path1,'r') as f1:                                             #opening the csv file 
    reader1 = csv.DictReader(f1)
    rows1 = list(reader1)

#looping over the rows from csv file

for rows1 in rows1:
    starttime1 = rows1['starttime']                                    # retrieving the values from columns
    stoptime1 = rows1['stoptime']
    starthours1 = starttime1.split(" ")                               #getting the column values with space
    stophours1 = stoptime1.split(" ")
    start_hours1.append(starthours1[1])                               #storing only time
    stop_hours1.append((stophours1[1]))


#looping over the time
for i in range(0, len(start_hours1)):
    start_time1 = start_hours1[i].split(":")                         #splitting the time into hours and minutes
    start_h1.append(start_time1[0])                                   # storing the hours
    stop_time1 = stop_hours1[i].split(":")
    stop_h1.append(stop_time1[0])
count = 0
for i in range(0, len(start_hours1)):                                #looping over the hours
    start1 = int(start_h1[i])
    stop1 = int(stop_h1[i])
    if (start_h1[i] == stop_h1[i]):                                  # checking if start and stop hours are same
        time1[start1] += 1                                           # adding the key value for corresponding hour in dictionary
    else:
        if start_h1[i] < stop_h1[i]:                                 #checking if stop time is greater than start time
            for j in range(start1, stop1 + 1):
                time1[j] += 1                                        #adding the key value for corresponding hour in dictionary
        else:
            while (start1 != stop1):

                if (start1 >= 24):                                   # check for start time greater than 24
                    start1 = 0                                       # changing the hour to 0
                time1[start1] += 1                                   #adding the key value for corresponding hour in dictionary
                if (start1 == stop1):
                    break
                start1 += 1

for key, value in time1.items():
    timeValues1.append(value)
totalTime1 = range(0, 24)
df1 = pd.DataFrame(timeValues1, index=totalTime1)                   #converting into data frame
print(df1)
with open('C:/Users/uamul/Desktop/kavya/output_2014.csv','w') as f1:  # writing into csv file
    df1.to_csv('C:/Users/uamul/Desktop/kavya/output_2014.csv')
f1.close()
