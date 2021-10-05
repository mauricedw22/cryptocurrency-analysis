import pandas as pd
import numpy as np
from sklearn import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

priceData = pd.read_csv('https://crypto-pricing-data.s3.us-east-2.amazonaws.com/tel-xdc-04_15_18-10_03_21.csv')

tel_price_data = priceData[['tel_price']]
xdc_price_results = priceData[['xdc_price']]

X_train, X_test, y_train, y_test = train_test_split(tel_price_data, xdc_price_results, test_size=0.30)

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
new_pred  = {'tel_price': [0.05]}
df  = pd.DataFrame(new_pred,columns=['tel_price'])
xdcPredictedPrice = hypothesis.predict(df)
print(xdcPredictedPrice)
'''

'''
# SCATTER PLOT VISUALIZATION of training data
plt.figure(figsize=(15,10))
plt.scatter(y_train,y_pred_train,c='green')
plt.plot([y_train.min(),y_train.max()],[y_train.min(),y_train.max()],'k--',c='blue',lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
'''