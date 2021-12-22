import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import time


data = pd.read_csv('csv_agile_C_London.csv',usecols=[0,1,4])

data.columns = ['Date','Time','Price'] # Naming columns

date = data['Date']
time_of_day = data['Time']
price = data['Price']

date=date.drop(date.index[0:57504])
time_of_day=time_of_day.drop(time_of_day.index[0:57504])
price=price.drop(price.index[0:57504])

print(date,price)
print(date.shape)

# Format date with date and time, time having newlined
date=date.apply(str)    #turn panda column into string
date=date.str.replace(' ','\n')
date=date.str.replace('Z','')

# #reduce number of values to hourly
months = [ '01/06/2021', '01/07/2021', '01/08/2021', '01/09/2021', '01/10/2021', '01/11/2021', '01/12/2021']
price_tick = ['-10', '-5', '0', '5', '10', '15', '20', '25', '30', '35' ]
#Plot date vs price
plt.figure(figsize=(25,14))
# plt.plot(date_reduce,price_reduce,linewidth=0.5)    
# plt.xticks(np.arange(0,len(date_reduce),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.plot(date,price,linewidth=0.5)    
#plt.xticks(np.arange(0,len(date),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.xticks(np.linspace(0,8973,7), months,fontsize=12)
plt.yticks(np.linspace(-10,35,10), price_tick, fontsize=12)
plt.ylabel("Price (p/kWh)",fontsize=20)
plt.xlabel("Date",fontsize=20)
plt.grid()
plt.title('Octopus Energy Agile Tariff Since June 2021',fontsize=20)
#plt.savefig('OctopusEnergyAgileTariffHalfYear.png')
plt.show()