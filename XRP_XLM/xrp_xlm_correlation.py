import pandas as pd
import numpy as np

correlationData = pd.read_csv('../cryptoData/xrp-xlm-01_01_18-10_07_21.csv')

correlation1 = correlationData['xrp_price'].corr(correlationData['xlm_price'])
correlation2 = correlationData['xrp_total_volume'].corr(correlationData['xlm_total_volume'])

correlation3 = correlationData['xrp_price'].corr(correlationData['xrp_total_volume'])
correlation4 = correlationData['xlm_price'].corr(correlationData['xlm_total_volume'])

print('XRP-XLM price corr: ' + str(correlation1))
print('XRP-XLM volume corr: ' + str(correlation2))
print('XRP price-to-volume corr: ' + str(correlation3))
print('XLM price-to-volume corr: ' + str(correlation4))