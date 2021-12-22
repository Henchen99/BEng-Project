import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import figure

#data = pd.read_csv('CLEAN_House1.csv',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
data = pd.read_csv('CLEAN_House4.csv',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
#read_csv automatically assumes separation using ',' so dont need to add
#usecols singles out specific columns

time = data['Time']     #label time column to 'time'
power = data['Aggregate']       #label aggregate column to 'power'

time=time.apply(str)    #turn panda column into string
time=time.str.replace(' ','\n')
time=time.str.replace('2013','13')

print(type(time))
print(time.dtype)
#print(time)

rows = 2766    #number of rows
t_reduce = time.head(rows)        #reduce the total number of data to first 'rows' rows
p_reduce = power.head(rows)

t_filter = t_reduce[t_reduce.index % 300 == 0]       #filter columns by using every 1000th value or every 100th minute
p_filter = p_reduce[p_reduce.index % 300 == 0]

data=[t_filter,p_filter]    #create 2 column list

df=pd.DataFrame(data)   #turn data into pandas dataframe
df=df.T #transpose dataframe
# print(df.shape)

# print(df)

#df.to_csv('Filtered_output_myriad')

frequency = 500
plt.figure(figsize=(25,8))
plt.plot(t_filter,p_filter,linewidth=0.5)    
plt.xticks(np.arange(0,len(t_filter),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.ylabel("Power",fontsize=15)
plt.xlabel("Time",fontsize=15)
#plt.grid()
plt.title('Household load profile',fontsize=15)
#plt.savefig('filtered_output_plot.png')
#plt.show()

# hi = 'hello my name is henry'

# hi=hi.replace(" ","\n")
# print(hi)


months = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(np.linspace(0,66380,35), months)

print(len(months))