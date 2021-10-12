import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

priceData = pd.read_csv('<YOUR_CSV_DATA>')

xrp_xlm_ratios = priceData[['xrp_xlm_ratio']]
time = priceData[['xrp_date']]

x_values = time
y_values = xrp_xlm_ratios

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel('XRP to XLM Ratio')
plt.title('XRP to XLM over time')

plt.plot_date(new_x, y_values, fmt="b-", tz=None, xdate=True)

plt.legend()

plt.show()

""" Programmatic save of file

plt.savefig('xdc_tel_ratios_graph.png', format='png')

"""