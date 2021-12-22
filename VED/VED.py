import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import time

#data = pd.read_excel('car id 455.xlsx', usecols=['DayNum','HV Battery SOC[%]'])
data = pd.read_excel('455 plot 19 november.xlsx', usecols=['charge','increment'])

daynumber = data['increment']
SOC = data['charge']

#print(daynumber.head())

# for idx, row in data.iterrows():
#     a=data['DayNum'].iloc[idx]

#     b=a-int(a)
#     # b=b*100
#     # print(b)
#     # hours = int(b)
#     # minutes = (b*60) % 60
#     # seconds = (b*3600) % 60
#     # #print("%d:%02d.%02d" % (hours, minutes, seconds))

#     # time_of_day = 24*b
#     # c = time_of_day - int(time_of_day)
#     # minutes_of_day = 60*c
#     # minutes_of_day = round(minutes_of_day,2)


# for idx, row in data.iterrows():
#     a=data['DayNum'].iloc[idx]
#     start = datetime.datetime(2017,1,11)

#     data


##df.ffill(axis=1)
time_= ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30'
, '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30'  
, '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30'
, '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'
, '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30'
, '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']
price_tick = [ '-5', '0', '5', '10', '15', '20', '25', '30', '35' ]
#frequency = 1

plt.figure(figsize=(25,14))
plt.plot(daynumber,SOC,linewidth=1.5)  
#plt.scatter(daynumber,SOC,s=10)     
#plt.xticks(np.arange(0,len(daynumber),frequency))      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.ylabel("SOC %",fontsize=20)
plt.xlabel("daynumber",fontsize=20)
plt.xticks(np.linspace(0,len(daynumber)-1,48), time_,fontsize=16, rotation=90)
plt.yticks(fontsize=16)
plt.grid()
plt.title('State of charge profile 19/11/2017',fontsize=30)
plt.savefig('19 november VED.png')
#plt.show()
