#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:15:15 2018

@author: Domo
"""


from math import sqrt

column1 = []
column2 = []
column3 = []
column4 = []
column5 = []



with open("data.txt", "r") as dataIn:
    
    for line in dataIn:
        line= line.strip()
        
        
        #This Loop read every number and assigns it to the columns
        column1.append(line.split()[0])
        column2.append(line.split()[1])
        column3.append(line.split()[2])
        column4.append(line.split()[3])
        column5.append(line.split()[4])
  


     




#initialize every number as a float
float_column1 = [float(i) for i in column1]
float_column2 = [float(i) for i in column2]
float_column3 = [float(i) for i in column3]
float_column4 = [float(i) for i in column4]
float_column5 = [float(i) for i in column5]






#Experiment 1
max_value1 = max(float_column1)
min_value1 = min(float_column1)
range_value1 = max_value1 - min_value1
sum_value1 = sum(float_column1)
average_value1 = sum(float_column1) / len(float_column1)
sddev_value1 = sqrt(sum((x - average_value1)**2 for x in float_column1) / len(float_column1))
variance_value1 = sum([(i - average_value1) ** 2 for i in float_column1]) / (len(float_column1) - 1)
          

#Experiment 2
max_value2 = max(float_column2)
min_value2 = min(float_column2)
range_value2 = max_value2 - min_value2
sum_value2 = sum(float_column2)
average_value2 = sum(float_column2) / len(float_column2)
sddev_value2 = sqrt(sum((x - average_value2)**2 for x in float_column2) / len(float_column2))
variance_value2 = sum([(i - average_value2) ** 2 for i in float_column2]) / (len(float_column2) - 1)

#Experiment 3
max_value3 = max(float_column3)
min_value3 = min(float_column3)
range_value3 = max_value3 - min_value3
sum_value3 = sum(float_column3)
average_value3 = sum(float_column3) / len(float_column3)
sddev_value3 = sqrt(sum((x - average_value3)**2 for x in float_column3) / len(float_column3))
variance_value3 = sum([(i - average_value3) ** 2 for i in float_column3]) / (len(float_column3) - 1)

#Experiment 4
max_value4 = max(float_column4)
min_value4 = min(float_column4)
range_value4 = max_value4 - min_value4
sum_value4 = sum(float_column4)
average_value4 = sum(float_column4) / len(float_column4)
sddev_value4 = sqrt(sum((x - average_value4)**2 for x in float_column4) / len(float_column4))
variance_value4 = sum([(i - average_value4) ** 2 for i in float_column4]) / (len(float_column4) - 1)

#Experiment 5
max_value5 = max(float_column5)
min_value5 = min(float_column5)
range_value5 = max_value5 - min_value5
sum_value5 = sum(float_column5)
average_value5 = sum(float_column5) / len(float_column5)
sddev_value5 = sqrt(sum((x - average_value5)**2 for x in float_column5) / len(float_column5))
variance_value5 = sum([(i - average_value5) ** 2 for i in float_column5]) / (len(float_column5) - 1)





with open("results.txt", "w") as dataOut:
    #
    print("Experiment 1 :", file = dataOut)
    print ("min: " , max_value1, file = dataOut)
    print ("max: " , min_value1, file = dataOut)
    print ("range: " , "{:10.5f}".format(range_value1), file = dataOut)
    print ("sum: ",  "{:10,.5f}".format(sum_value1), file = dataOut)
    print ("average: ", "{:10,.5f}".format(average_value1), file = dataOut)
    print ("sddev: ", "{:10,.5f}".format(sddev_value1), file = dataOut)
    print ("variance: ", "{:10,.5f}".format(variance_value1), file = dataOut)
    
    
     
    print ( file = dataOut)
    
    print ( file = dataOut)
    
    print("Experiment 2 :", file = dataOut)
    print ("max: " , max_value2, file = dataOut)
    print ("min: " , min_value2, file = dataOut)
    print ("range: " , "{:10.5f}".format(range_value2), file = dataOut)
    print ("sum: ",  "{:10,.5f}".format(sum_value2), file = dataOut)
    print ("average: ", "{:10,.5f}".format(average_value2), file = dataOut)
    print("sddev: ", "{:10,.5f}".format(sddev_value2), file = dataOut)
    print ("variance: ", "{:10,.5f}".format(variance_value2), file = dataOut)
    
    print ( file = dataOut)
    
    
    print ( file = dataOut)
    
    print("Experiment 3 :", file = dataOut)
    print ("max: " , max_value3, file = dataOut)
    print ("min: " , min_value3, file = dataOut)
    print ("range: " , "{:10.5f}".format(range_value3), file = dataOut)
    print ("sum: ",  "{:10,.5f}".format(sum_value3), file = dataOut)
    print ("average: ", "{:10,.5f}".format(average_value3), file = dataOut)
    print("sddev: ", "{:10,.5f}".format(sddev_value3), file = dataOut)
    print ("variance: ", "{:10,.5f}".format(variance_value3), file = dataOut)
    
    print ( file = dataOut)
    
    print ( file = dataOut)
    
    print("Experiment 4 :", file = dataOut)
    print ("max: " , max_value4, file = dataOut)
    print ("min: " , min_value4, file = dataOut)
    print ("range: " , "{:10.5f}".format(range_value4), file = dataOut)
    print ("sum: ",  "{:10,.5f}".format(sum_value4), file = dataOut)
    print ("average: ", "{:10,.5f}".format(average_value4), file = dataOut)
    print("sddev: ", "{:10,.5f}".format(sddev_value4), file = dataOut)
    print ("variance: ", "{:10,.5f}".format(variance_value4), file = dataOut)
    
    print ( file = dataOut)
    
    print ( file = dataOut)
    
    print("Experiment 5 :", file = dataOut)
    print ("max: " , max_value5, file = dataOut)
    print ("min: " , min_value5, file = dataOut)
    print ("range: " , "{:10.5f}".format(range_value5), file = dataOut)
    print ("sum: ",  "{:10,.5f}".format(sum_value5), file = dataOut)
    print ("average: ", "{:10,.5f}".format(average_value5), file = dataOut)
    print ("sddev: ", "{:10,.5f}".format(sddev_value5), file = dataOut)
    print ("variance: ", "{:10,.5f}".format(variance_value5), file = dataOut)


