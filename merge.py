#importing required packages
import csv
import pandas as pd

#specified path to open the csv files
path1 = 'C:/Materials/Classes/Data Viz/Projects/Project 02/Divvy_Stations_Trips_2014-20161012T040402Z/Divvy_Stations_Trips_2014/Divvy_Stations_Trips_2014_Q1Q2/Divvy_Stations_Trips_2014_Q1Q2'
path2 = 'C:/Materials/Classes/Data Viz/Projects/Project 02/Divvy_Stations_Trips_2014-20161012T040402Z/Divvy_Stations_Trips_2014/Divvy_Stations_Trips_2014_Q3Q4/Divvy_Stations_Trips_2014_Q3Q4'

#readign the csv files
df1 = pd.read_csv(path1+"/Divvy_Trips_2014_Q1Q2.csv")
df2 = pd.read_csv(path2+"/Divvy_Trips_2014-Q3-07.csv")
df3 = pd.read_csv(path2+"/Divvy_Trips_2014-Q3-0809.csv")
df4 = pd.read_csv(path2+"/Divvy_Trips_2014-Q4.csv")

#appending the files
merged = df1.append(df2)
merged1 = df3.append(df4)

#writing to csv files
merged1.to_csv("C:/Materials/Classes/Data Viz/Projects/Project 02/Divvy_Stations_Trips_2014-20161012T040402Z/Divvy_Stations_Trips_2014/output.csv")
merged.to_csv("C:/Materials/Classes/Data Viz/Projects/Project 02/Divvy_Stations_Trips_2014-20161012T040402Z/Divvy_Stations_Trips_2014/output1.csv")


