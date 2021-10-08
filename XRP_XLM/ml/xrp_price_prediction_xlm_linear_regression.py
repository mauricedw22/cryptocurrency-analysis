import pandas as pd
import numpy as np
from sklearn import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

priceData = pd.read_csv('../cryptoData/xrp-xlm-01_01_18-10_07_21.csv')

xlm_price_data = priceData[['xlm_price']]
xrp_price_results = priceData[['xrp_price']]

X_train, X_test, y_train, y_test = train_test_split(xlm_price_data, xrp_price_results, test_size=0.30)

#Training the model with set of predictors in X
hypothesis = LinearRegression(fit_intercept=True) # hypothesis = SVR(kernel="rbf") # epsilon=0.0001)
hypothesis.fit(X_train, y_train)

# Prediction Scoring: r2_score and root mean squared error
y_pred_test = hypothesis.predict(X_test)
y_pred_train = hypothesis.predict(X_train)

print(np.abs(r2_score(y_train, y_pred_train)))
print(np.sqrt(mean_squared_error(y_train, y_pred_train)))

'''
# Individual Prediction
new_pred  = {'xlm_price': [0.40]}
df  = pd.DataFrame(new_pred,columns=['xlm_price'])
xrpPredictedPrice = hypothesis.predict(df)
print(xrpPredictedPrice)
'''

'''
# SCATTER PLOT VISUALIZATION of training data
plt.figure(figsize=(15,10))
plt.scatter(y_train,y_pred_train,c='green')
plt.plot([y_train.min(),y_train.max()],[y_train.min(),y_train.max()],'k--',c='blue',lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
'''