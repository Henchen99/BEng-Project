import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import figure

## opening the data ##
data = pd.read_csv('CLEAN_House1.csv',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
#data = pd.read_csv('CLEAN_House4.csv',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
#read_csv automatically assumes separation using ',' so dont need to add
#usecols singles out specific columns


# computing a 7 day rolling average
data[ 'moving_avg' ] = data.Aggregate.rolling(window=100).mean() #moving average of 100 is approximately 10 minutes

# viewing the dataset
#print(data.head(10))

time = data['Time']     #label time column to 'time'
power = data['Aggregate']       #label aggregate column to 'power'
moving_average=data[ 'moving_avg' ] 

time=time.drop(time.index[0:5166])
power=power.drop(power.index[0:5166])
moving_average=moving_average.drop(moving_average.index[0:5166])

## formatting graph axis ##
time=time.apply(str)    #turn panda column into string

time=time.str.replace(' ','\n')
# time=time.str.replace('09/10/2013','')
time=time.str.replace('10/10/2013','')

#time=time.str.replace('2013','13')
# print(time.dtype)
# print(type(time[1]))

## reducing the data ##
#rows = 20000    #number of rows
rows = 13000    #rows for a day
#rows = 100000  #rows for a week
t_reduce = time.head(rows)        #reduce the total number of data to first 'rows' rows
p_reduce = power.head(rows)
mva_reduce = moving_average.head(rows)

t_filter = t_reduce[t_reduce.index % 10 == 0]       #filter columns by using every 1000th value or every 100th minute
p_filter = p_reduce[p_reduce.index % 10 == 0]
mva_filter = mva_reduce[mva_reduce.index % 10 == 0]

## converting back to csv ##
#data=[t_filter,p_filter]    #create 2 column list
#df=pd.DataFrame(data)   #turn data into pandas dataframe
#df=df.T #transpose dataframe
# print(df.shape)
# print(df)
#df.to_csv('Filtered_output_myriad')

## plot ##
frequency = 40
plt.figure(figsize=(50,20))
plt.plot(t_filter,p_filter,linewidth=1,label='Data')    
plt.plot(t_filter,mva_filter,linewidth=2,label='Moving average')    
plt.xticks(np.arange(0,len(t_filter),frequency),fontsize=20)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.yticks(np.arange(0,11000,1000),fontsize=20)
plt.ylabel("Power",fontsize=40)
plt.xlabel("Time",fontsize=40)
#plt.grid()
# plt.title('Household load profile with moving average for 1 day',fontsize=35)
plt.title('Household load profile with moving average on 10/10/2013',fontsize=45)
#xposition = [105, 365, 640, 915, 1190, 1465, 1740, 2015] #plotting vertical lines to show start of each day, where 24 hours is approximately 275 rows
#plt.axvline(x=105, color='k', linestyle='--')
plt.legend(fontsize=25)
plt.grid()
plt.savefig('filtered_output_plot.png')
#plt.show()

