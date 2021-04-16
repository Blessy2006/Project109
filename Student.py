import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
Marklist = df["math score"].to_list()

#Mean
mean = statistics.mean(Marklist)


#Median 
median = statistics.median(Marklist)

#Mode 
mode = statistics.mode(Marklist)


#Printing mean, median and mode to validate
print("Mean, Median and Mode is {}, {} and {} respectively".format(mean, median, mode))

#Standard deviation 
std_deviation = statistics.stdev(Marklist)

#1, 2 and 3 Standard Deviations 
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations 
list_of_data_within_1_std_deviation = [result for result in Marklist if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in Marklist if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in Marklist if result > third_std_deviation_start and result < third_std_deviation_end]

#Printing data 
print("{}% of data for marks lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(Marklist)))
print("{}% of data for marks lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(Marklist)))
print("{}% of data for marks lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(Marklist)))
