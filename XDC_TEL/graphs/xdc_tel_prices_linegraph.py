import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

xdcData = pd.read_csv('<YOUR_CSV_DATA>')

xdcPrice = xdcData[['xdc_price']]
telPrice = xdcData[['tel_price']]
time = xdcData[['xdc_date']]

x_values = time
y_values = xdcPrice
y_values2 = telPrice

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel('XDC & TEL Price')
plt.title('XDC & TEL Prices over time')

plt.plot_date(new_x, y_values, fmt="-", tz=None, xdate=True, c='blue')
plt.plot_date(new_x, y_values2, fmt="-", tz=None, xdate=True, c='red')

plt.legend()

plt.show()