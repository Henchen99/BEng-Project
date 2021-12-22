import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#data = pd.read_csv('CLEAN_House1.csv',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
data = pd.read_csv('Filtered_output_myriad',usecols=['Time','Aggregate'])     #data is stored as comma-separated-value so 'read_csv' method is used
#read_csv automatically assumes separation using ',' so dont need to add
#usecols singles out specific columns 

time = data['Time']     #set time column to time
power = data['Aggregate']       #set aggregate column to power



frequency = 50
plt.plot(time,power)     
#plt.xticks(np.arange(0,len(time),frequency))      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.ylabel("Power",fontsize=20)
#plt.xlabel("Time",fontsize=20)
#plt.grid()
plt.title('Household load profile',fontsize=20)

plt.show()