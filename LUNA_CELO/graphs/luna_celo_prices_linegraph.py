import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

lunaData = pd.read_csv('https://crypto-pricing-data.s3.us-east-2.amazonaws.com/luna-celo-05_22_20-10_07_21.csv')

celoPrice = lunaData[['celo_price']]
lunaPrice = lunaData[['luna_price']]
time = lunaData[['luna_date']]

x_values = time
y_values = lunaPrice
y_values2 = celoPrice

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel('LUNA & CELO Price')
plt.title('LUNA & CELO Prices over time')

plt.plot_date(new_x, y_values, fmt="-", tz=None, xdate=True, c='blue')
plt.plot_date(new_x, y_values2, fmt="-", tz=None, xdate=True, c='red')

plt.legend()

plt.show()