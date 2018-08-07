#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Written by Domas Budrys
"""

import csv

column_station = []
column_name = []
column_date = []
column_prcp = []
column_snow = []
column_snwd = []
column_tavg = []
column_tmax = []
column_tmin = []


tavg_zero_count = 0
tavg_none_count = 0

tmax_zero_count = 0
tmax_none_count = 0

tmin_zero_count = 0
tmin_none_count = 0

prcp_zero_count = 0
prcp_none_count = 0

snow_zero_count = 0
snow_none_count = 0


with open("Clarksville_weather_history.csv", "r") as dataIn:
    
    reader = csv.DictReader(dataIn)
    
    for row in reader:
        
        
        #clean up data in TAVG column 
        if row['TAVG'] > '0':
            row['TAVG'] = float(row['TAVG'])
        
        elif row['TAVG'] == '0':
            row['TAVG'] = None
            tavg_zero_count += 1
            
        else:
            row['TAVG'] = None
            tavg_none_count += 1
        
        
        
        #clean up data in TMAX column
        if row['TMAX'] > '0':
            row['TMAX'] = float(row['TMAX'])
        
        elif row['TMAX'] == '0':
            row['TMAX'] = None
            tmax_zero_count += 1
            
        else:
            row['TMAX'] = None
            tmax_none_count += 1
            
            
            
        #clean up data in TMIN column
        if row['TMIN'] > '0':
            row['TMIN'] = float(row['TMIN'])
        
        elif row['TMIN'] == '0':
            row['TMIN'] = None
            tmin_zero_count += 1
            
        else:
            row['TMIN'] = None
            tmin_none_count += 1
            
            
            
        #clean up data in PRCP column
        if row['PRCP'] == "0.00":
            row['PRCP'] = None
            prcp_zero_count += 1
        
        elif row['PRCP'] > '0':
            row['PRCP'] = float(row['PRCP'])
            
            
        else:
            row['PRCP'] = None
            prcp_none_count += 1
        

        #clean up data in SNOW column
        if row['SNOW'] == '0.0':
            row['SNOW'] = None
            snow_zero_count += 1
          
        
        elif row['SNOW'] > '0':
            row['SNOW'] = float(row['SNOW'])
            
        else:
            row['SNOW'] = None
            snow_none_count += 1
          
        
        column_station.append(row['STATION'])
        column_name.append(row['NAME'])
        column_date.append(row['DATE'])
        column_prcp.append(row['PRCP'])
        column_snow.append(row['SNOW'])
        column_snwd.append(row['SNWD'])
        column_tavg.append(row['TAVG'])
        column_tmax.append(row['TMAX'])
        column_tmin.append(row['TMIN'])
        

    
    max_tavg= float(max(x for x in column_tavg if x is not None))
    min_tavg= float(min(x for x in column_tavg if x is not None))
    
    max_tmax= float(max(x for x in column_tmax if x is not None))
    min_tmax= float(min(x for x in column_tmax if x is not None))
    
    max_tmin= float(max(x for x in column_tmin if x is not None))
    min_tmin= float(min(x for x in column_tmin if x is not None))
    
    max_prcp= float(max(x for x in column_prcp if x is not None))


    #Find index of 'TAVG' and assign date using index
    max_tavg_index = column_tavg.index(max_tavg)
    max_tavg_date = column_date[max_tavg_index]
    
    min_tavg_index = column_tavg.index(min_tavg)
    min_tavg_date = column_date[min_tavg_index]
    
    #Find index of 'TMAX' and assign date using index
    max_tmax_index = column_tmax.index(max_tmax)
    max_tmax_date = column_date[max_tmax_index]
    
    min_tmax_index = column_tmax.index(min_tmax)
    min_tmax_date = column_date[min_tmax_index]
    
    #Find index of 'TMAX' and assign date using index
    max_tmin_index = column_tmin.index(max_tmin)
    max_tmin_date = column_date[max_tmin_index]
    
    min_tmin_index = column_tmin.index(min_tmin)
    min_tmin_date = column_date[min_tmin_index]
    
    
    #Find index of 'PRCP' and assign date using index
    prcp_index = column_prcp.index(max_prcp)
    prcp_date = column_date[prcp_index]
    
    
    #Find index of 'SNOW' and assign date using index
    #Cannot be displayed
#    snow_index = column_snow.index(max_snow)
#    snow_date = column_date[snow_index]
    
    
    
    
with open("results2.txt", "w") as dataOut: 
    
    print ("Prepared by: Domas Budrys", file = dataOut)
    print (file = dataOut)
    
    print ("The highest average temperature: ",max_tavg,
           " and the day it occurred: " ,max_tavg_date, file = dataOut)
    print(file = dataOut)
    print ("The lowest average temperature: ",min_tavg,
           " and the day it occurred: " ,min_tavg_date, file = dataOut)
    
    print(file = dataOut)
    print ("The number of values in the column (TAVG) that are empty :",
           tavg_none_count, file = dataOut)
    print ("The number of values in the column (TAVG) that are zero(0) :",
           tavg_zero_count, file = dataOut)
    
    print("-------------------------------------------------------------", 
          file = dataOut)
    print( file = dataOut)
    
    
    
    print ("The highest maximum temperature: ",max_tmax,
           " and the day it occurred: " ,max_tmax_date, file = dataOut)
    print(file = dataOut)
    print ("The lowest maximum temperature: ",min_tmax,
           " and the day it occurred: " ,min_tmax_date, file = dataOut)
    
    print(file = dataOut)
    print ("The number of values in the column (TMAX) that are empty :",
           tmax_none_count, file = dataOut)
    print ("The number of values in the column (TMAX) that are zero(0) :",
           tmax_zero_count, file = dataOut)
    
    print("-------------------------------------------------------------",
          file = dataOut)
    print( file = dataOut)
    



    print ("The highest minimum temperature: ",max_tmin,
           " and the day it occurred: " ,max_tmin_date, file = dataOut)
    print(file = dataOut)
    print ("The lowest minimum temperature: ",min_tmin,
           " and the day it occurred: " ,min_tmin_date, file = dataOut)
    
    print(file = dataOut)
    print ("The number of values in the column (TMIN) that are empty :",
           tmin_none_count, file = dataOut)
    print ("The number of values in the column (TMIN) that are zero(0) :",
           tmin_zero_count, file = dataOut)
    
    print("-------------------------------------------------------------",
          file = dataOut)
    print(file = dataOut)
    
    
    
    print ("The highest precipitation: ",max_prcp,
           " and the day it occurred: " ,prcp_date, file = dataOut)
    print(file = dataOut)
   
    
    print(file = dataOut)
    print ("The number of values in the column (PRCP) that are empty :",
           prcp_none_count, file = dataOut)
    print ("The number of values in the column (PRCP) that are zero(0) :",
           prcp_zero_count, file = dataOut)
    
    print("-------------------------------------------------------------", 
          file = dataOut)
    print(file = dataOut)
    
    print ("Highest value of SNOW cannot be calculated because none of the\n",
           "values are higher than (0) or something else than 'None' ", 
           file = dataOut)
    print(file = dataOut)
    print ("The number of values in the column (SNOW) that are empty :",
           snow_none_count, file = dataOut)
    print ("The number of values in the column (SNOW) that are zero(0) :",
           snow_zero_count, file = dataOut)
    
    print ("Proof: ", snow_none_count, "+", snow_zero_count, 
           ' = (Number of Rows)', len(column_snow), file = dataOut)
    
  
    
    