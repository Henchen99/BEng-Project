import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import time

#skip_list=[m for m in range(66288,70000)]
skip_list=[m for m in range(11230,70000)]
data = pd.read_csv('csv_agile_C_London.csv',usecols=[0,1,4], skiprows=skip_list)

data.columns = ['Date','Time','Price'] # Naming columns

date = data['Date']
time_of_day = data['Time']
price = data['Price']

# date=date.drop(date.index[0:64847])
# time_of_day=time_of_day.drop(time_of_day.index[0:64847])
# price=price.drop(price.index[0:64847])
date=date.drop(date.index[0:11181])
time_of_day=time_of_day.drop(time_of_day.index[0:11181])
price=price.drop(price.index[0:11181])

#print(len(date))
print(date,price)

# Format date with date and time, time having newlined
date=date.apply(str)    #turn panda column into string
date=date.str.replace(' ','\n')
date=date.str.replace('Z','')

# #reduce number of values to hourly
months = [i for i in range(1,31)]
time_= ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30'
, '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30'  
, '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30'
, '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'
, '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30'
, '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']
price_tick = [ '-5', '0', '5', '10', '15', '20', '25', '30', '35' ]
print(len(time_))
#print(months)

#Plot date vs price
plt.figure(figsize=(25,14))
# plt.plot(date_reduce,price_reduce,linewidth=0.5)    
# plt.xticks(np.arange(0,len(date_reduce),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.plot(date,price,linewidth=1.5)    
#plt.xticks(np.arange(0,len(date),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.xticks(np.linspace(0,len(date)-1,48), time_,fontsize=16, rotation=90)
plt.yticks(np.linspace(-5,35,9), price_tick, fontsize=16)
plt.ylabel("Price (p/kWh)",fontsize=30)
plt.xlabel("Date",fontsize=30)
plt.grid()
plt.title('Octopus Energy Agile Tariff 10/10/2018',fontsize=30)
plt.savefig('OctopusEnergyAgileTariffoneday.png')
#plt.show()
