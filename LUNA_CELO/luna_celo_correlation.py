import pandas as pd
import numpy as np

correlationData = pd.read_csv('<YOUR_CSV_DATA>')

correlation1 = correlationData['luna_price'].corr(correlationData['celo_price'])
correlation2 = correlationData['luna_total_volume'].corr(correlationData['celo_total_volume'])

correlation3 = correlationData['luna_price'].corr(correlationData['luna_total_volume'])
correlation4 = correlationData['celo_price'].corr(correlationData['celo_total_volume'])

print('LUNA-CELO price corr: ' + str(correlation1))
print('LUNA-CELO volume corr: ' + str(correlation2))
print('LUNA price-to-volume corr: ' + str(correlation3))
print('CELO price-to-volume corr: ' + str(correlation4))