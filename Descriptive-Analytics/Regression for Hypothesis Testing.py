import pandas as pd
 # Load Advertising dataset 
data = pd.read_csv('Descriptive-Analytics/advertising_data_large.csv') 
X = data[['TV']] 
y = data['Sales']
         
from sklearn.linear_model import LinearRegression 

# Fit model for Simple Linear Regression
model = LinearRegression() 
model.fit(X, y)
print("Coefficient (β1):", model.coef_[0])
print("Intercept (β0):", model.intercept_)

#Statistical Signifcance
import statsmodels.api as sm

X_with_const = sm.add_constant(X)  # Adds intercept
model_sm = sm.OLS(y, X_with_const).fit()
print(model_sm.summary())


# Model for Multiple Linear Regression
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

X_with_const = sm.add_constant(X)
model_sm = sm.OLS(y, X_with_const).fit()
print(model_sm.summary())


#Confidence Intervals

# Display confidence intervals
print("Confidence Intervals:\n", model_sm.conf_int())

# Predict Sales with significant predictors (e.g., TV and Radio if significant)
significant_X = X[['TV', 'Radio']]
model_sig = LinearRegression()
model_sig.fit(significant_X, y)
predictions = model_sig.predict(significant_X)
print("Predictions:", predictions)


