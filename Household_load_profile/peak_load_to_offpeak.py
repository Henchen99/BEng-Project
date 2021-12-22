from typing import OrderedDict
from numpy.lib.function_base import average
import pandas as pd
import numpy as np

#for house 1, first full day 10/10/2013 starts at row 5166 and ends row 18043, difference 12877 - IS A THURSDAY
#for day after: 11/11/2013 row 18044 and ends 31694 difference 13651
#for day after: 12/11/2013 row 31695 and ends 45584 difference 13890
#skip_list=[m for m in range(18044,10000000)]
skip_list=[m for m in range(25000,10000000)]
data = pd.read_csv('CLEAN_House1.csv',usecols=['Time','Aggregate','Unix'], skiprows=skip_list)     #data is stored as comma-separated-value so 'read_csv' method is used
#read_csv automatically assumes separation using ',' so dont need to add
#usecols singles out specific columns

data[ 'moving_avg' ] = data.Aggregate.rolling(window=100).mean() #moving average of 300 is approximately 30 minutes

time = data['Time']
power = data['Aggregate']       #set aggregate column to power - it is a panda type called Series
unixtime = data['Unix']       #set Unix column to unixtime
mvingave = data['moving_avg']

data=[time, power, unixtime, mvingave] #create 2 column list

df=pd.DataFrame(data)   #turn data into pandas dataframe
df=df.T #transpose dataframe
# df=df.drop(df.index[0:5164]) # lose first 5164 rows as it is data from previous day
df=df.drop(df.index[0:2585]) # lose first 5164 rows as it is data from previous day
#df.to_csv('kwh_calc')

# Calculate number of days
difference = df.Unix.iloc[12877]-df.Unix.iloc[0]
days=difference/(60*60*24)
days=round(days)
print(days)

# initialise lists for peak kWh
peak_kwh_per_day=[]
start_row=df['Unix'].iloc[0]

#print(df.Unix.shape)

# for p in df.Unix:   #iterate through Unix column
#     time = round((p-start_row)/86400,4) #time between rows in days
#     print(time)
#     shouldbetime=2
#     if time==shouldbetime:    #check if time is an integer (full day) 
#         highest=0   #set highest back to 0
#         for m, row in df.loc[0:26528].iterrows(): #If 1 day is itereated, itereate m between the range of rows
#             if df['moving_avg'].iloc[m]>highest: #if the value m is greater than highest
#                 highest=df['moving_avg'].iloc[m] #make highest equal m
#         peak_kwh_per_day.append(highest)    #add highest value to list
    
    #start_row=p #start_row equals last value of p now and repeat
highest=0
for m, row in df.loc[0:18000].iterrows(): #Itereate m between the range of rows # 12877
    if df['moving_avg'].iloc[m]>highest: #if the value at m is greater than highest
        highest=df['moving_avg'].iloc[m] #make highest equal m
peak_kwh_per_day.append(highest)    #add highest value to list

#print(peak_kwh_per_day)
average_peak = sum(peak_kwh_per_day)/1
print('Average peak kwh is: ',average_peak,'kWh')
offpeak=average_peak*(30/100)
print('Off peak kwh is: ',round(offpeak,2),'kWh')

dup_time_intervals=[]
for op, row in df.loc[0:18000].iterrows():    #loop through to find time intervals less than offpeak
    #print(df.Time.iloc[op],df.moving_avg.iloc[op])
    if df['moving_avg'].iloc[op]<offpeak:
        dup_time_intervals.append(df['Time'].iloc[op])

time_intervals=[]
for k in dup_time_intervals:
    if k not in time_intervals:
        time_intervals.append(k)

#print(time_intervals)

df2=pd.DataFrame(time_intervals)
df2.to_csv('Offpeak_times.csv')