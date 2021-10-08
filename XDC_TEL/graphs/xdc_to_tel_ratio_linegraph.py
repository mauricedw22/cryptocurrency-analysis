import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

priceData = pd.read_csv('../cryptoData/tel-xdc-04_15_18-10_03_21.csv')

xdc_tel_ratios = priceData[['xdc_tel_ratio']]
time = priceData[['xdc_date']]

x_values = time
y_values = xdc_tel_ratios

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel('XDC to TEL Ratio')
plt.title('XDC to TEL over time')

plt.plot_date(new_x, y_values, fmt="b-", tz=None, xdate=True)

plt.legend()

plt.show()

""" Programmatic save of file

plt.savefig('xdc_tel_ratios_graph.png', format='png')

"""