import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

xrpData = pd.read_csv('<YOUR_CSV_DATA>')

xrpPrice = xrpData[['xrp_price']]
xlmPrice = xrpData[['xlm_price']]
time = xrpData[['xrp_date']]

x_values = time
y_values = xrpPrice
y_values2 = xlmPrice

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel('XRP & XLM Price')
plt.title('XRP & XLM Prices over time')

plt.plot_date(new_x, y_values, fmt="-", tz=None, xdate=True, c='blue')
plt.plot_date(new_x, y_values2, fmt="-", tz=None, xdate=True, c='red')

plt.legend()

plt.show()