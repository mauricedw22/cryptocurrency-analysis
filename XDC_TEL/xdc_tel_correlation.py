import pandas as pd
import numpy as np

correlationData = pd.read_csv('C:/Users/mauri/Desktop/cryptoAnalysis/cryptoData/tel-xdc-04_15_18-10_03_21.csv')

correlation1 = correlationData['xdc_price'].corr(correlationData['tel_price'])
correlation2 = correlationData['xdc_volume'].corr(correlationData['tel_volume'])

correlation3 = correlationData['xdc_price'].corr(correlationData['xdc_volume'])
correlation4 = correlationData['tel_price'].corr(correlationData['tel_volume'])

print('XDC-TEL price corr: ' + str(correlation1))
print('XDC-TEL volume corr: ' + str(correlation2))
print('XDC price-to-volume corr: ' + str(correlation3))
print('TEL price-to-volume corr: ' + str(correlation4))