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

date=date.drop(date.index[0:479])
time_of_day=time_of_day.drop(time_of_day.index[0:479])
price=price.drop(price.index[0:479])

print(date,price)

# Format date with date and time, time having newlined
date=date.apply(str)    #turn panda column into string
date=date.str.replace(' ','\n')
date=date.str.replace('Z','')

# rows=66478
# date_reduce=date.head(rows)
# price_reduce=price.head(rows)
# #reduce number of values to hourly
months = ['01/03/2018', '01/04/2018', '01/05/2018', '01/06/2018', '01/07/2018', '01/08/2018', '01/09/2018', '01/10/2018', '01/11/2018', '01/12/2018'
          , '01/01/2019', '01/02/2019', '01/03/2019', '01/04/2019', '01/05/2019', '01/06/2019', '01/07/2019', '01/08/2019', '01/09/2019', '01/10/2019'
          , '01/11/2019', '01/12/2019', '01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020', '01/05/2020', '01/06/2020', '01/07/2020', '01/08/2020'
          , '01/09/2020', '01/10/2020', '01/11/2020', '01/12/2020', '01/01/2021', '01/02/2021', '01/03/2021', '01/04/2021', '01/05/2021', '01/06/2021'
          , '01/07/2021', '01/08/2021', '01/09/2021', '01/10/2021', '01/11/2021', '01/12/2021']
price_tick = ['-10', '-5', '0', '5', '10', '15', '20', '25', '30', '35' ]
#Plot date vs price
plt.figure(figsize=(25,14))
# plt.plot(date_reduce,price_reduce,linewidth=0.5)    
# plt.xticks(np.arange(0,len(date_reduce),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.plot(date,price,linewidth=0.5)    
#plt.xticks(np.arange(0,len(date),frequency),fontsize=7)      #change tick frequency, starting from 0, to length of array, taking every 'frequency' steps
plt.xticks(np.linspace(0,65998,46), months,fontsize=7,rotation=90)
plt.yticks(np.linspace(-10,35,10), price_tick)
plt.ylabel("Price (p/kWh)",fontsize=15)
plt.xlabel("Date",fontsize=15)
plt.grid()
plt.title('Octopus Energy Agile Tariff Since March 2018',fontsize=15)
#plt.savefig('OctopusEnergyAgileTariffFull.png')
#plt.show()
