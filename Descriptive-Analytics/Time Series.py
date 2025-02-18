# Required Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Slide # 4

# Example dataset: Monthly sales
data = {
    'Date': pd.date_range(start='2022-01-01', periods=12, freq='M'),
    'Sales': [200, 220, 250, 270, 300, 350, 400, 420, 380, 360, 400, 450]
}
df = pd.DataFrame(data)

# # Plotting sales data
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Sales'], marker='o')
# plt.title("Monthly Sales Data")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 5

# # Creating a daily dataset
# daily_data = {
#     'Date': pd.date_range(start='2022-01-01', periods=30, freq='D'),
#     'Value': [i + (i % 7) * 2 for i in range(30)]
# }
# df_daily = pd.DataFrame(daily_data)

# Plotting daily data
# plt.figure(figsize=(10, 5))
# plt.plot(df_daily['Date'], df_daily['Value'], label="Daily Granularity")
# plt.title("Daily Time Series Data")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

# # Setting the 'Date' column as the index for resampling
# df_daily.set_index('Date', inplace=True)

# # Resample to weekly
# df_weekly = df_daily.resample('W').mean().reset_index()

# # Plotting weekly data
# plt.figure(figsize=(10, 5))
# plt.plot(df_weekly['Date'], df_weekly['Value'], marker='o', label="Weekly Granularity")
# plt.title("Weekly Aggregated Data")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# # Create a sample dataset for slides 8,9, 10, 11
# data = {
#     'Date': pd.date_range(start='2022-01-01', periods=100, freq='D'),
#     'Value': [i + np.random.normal(0, 2) for i in range(100)]
# }
# df = pd.DataFrame(data)

#-------------------------------------------------------------------------------------------------------------#

# Slide 8 - Trend 

# # Calculate rolling mean for trend
# df['Trend'] = df['Value'].rolling(window=10).mean()

# # Plot original data and trend
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Data', alpha=0.7)
# plt.plot(df['Date'], df['Trend'], label='Trend (Rolling Mean)', color='red')
# plt.title("Trend Component")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

#---------------------------------------------------------------------------------------------------------#

# Slide # 9 - Seasonality

# Add synthetic seasonality to data
# df['Seasonality'] = 10 * np.sin(2 * np.pi * df.index / 365)

# # Plot seasonality
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Seasonality'], label='Seasonality')
# plt.title("Seasonality Component")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 10 - Cyclical 

# Add synthetic cyclicality
# df['Cyclicality'] = 5 * np.sin(2 * np.pi * df.index / 100)

# # Plot cyclicality
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Cyclicality'], label='Cyclicality')
# plt.title("Cyclical Component")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 11 - Noise

# Add noise to the dataset
# df['Noise'] = np.random.normal(0, 2, size=len(df))

# # Plot noise
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Noise'], label='Noise')
# plt.title("Irregular Component (Noise)")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 12

# from statsmodels.tsa.seasonal import seasonal_decompose

# # Decompose the time series (additive)
# decomposition = seasonal_decompose(df['Value'], model='additive', period=10)
# decomposition.plot()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Data for slides 13, 14, 15, 16, 21, 32, 41, 43, 44, 45, 46, 51, 53, 54, 56, 59, 60, 61

# Create synthetic data
date_range = pd.date_range(start='2022-01-01', periods=365, freq='D')
data = [50 + 0.2 * i + 10 * np.sin(2 * np.pi * i / 365) + np.random.normal(0, 2) for i in range(365)]
df = pd.DataFrame({'Date': date_range, 'Value': data})

#-------------------------------------------------------------------------------------------------------------#

# Slide # 13

# # Line plot
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Time Series Data')
# plt.title("Time Series Line Plot")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 14

# Summary statistics
# print(df.describe())

# # Plot histogram for distribution
# plt.figure(figsize=(8, 4))
# plt.hist(df['Value'], bins=20, color='skyblue', edgecolor='black')
# plt.title("Distribution of Time Series Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 15

# Introduce some missing values for demonstration
df.loc[50:60, 'Value'] = None

# # Check for missing values
# print("Missing Values Count:\n", df.isnull().sum())

# # Visualize missing data
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Time Series Data', marker='o', color='blue')
# plt.title("Missing Data Visualization")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 16

# Detect outliers using IQR
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Value'] < (Q1 - 1.5 * IQR)) | (df['Value'] > (Q3 + 1.5 * IQR))]

# print("Outliers Detected:\n", outliers)

# # Visualize outliers with a boxplot
# plt.figure(figsize=(8, 5))
# plt.boxplot(df['Value'].dropna(), vert=False, patch_artist=True)
# plt.title("Boxplot for Outlier Detection")
# plt.xlabel("Value")
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 21

# # Plot autocorrelation with comments
# from statsmodels.graphics.tsaplots import plot_acf

# plt.figure(figsize=(10, 5))
# plot_acf(df['Value'].dropna(), lags=70, title="Autocorrelation Plot with Lag Analysis")
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

#Slide # 32

from statsmodels.graphics.tsaplots import plot_pacf

plt.figure(figsize=(10, 5))
plot_pacf(df['Value'].dropna(), lags=30, title="PACF Plot for AR Model Order Selection")
plt.grid()
plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 41

# from statsmodels.tsa.stattools import adfuller

# # Perform the ADF test
# adf_result = adfuller(df['Value'])

# # Print the results
# print("ADF Statistic:", adf_result[0])
# print("p-value:", adf_result[1])
# print("Critical Values:")
# for key, value in adf_result[4].items():
#     print(f"  {key}: {value}")

# # Interpretation
# if adf_result[1] < 0.05:
#     print("The series is stationary (reject H0).")
# else:
#     print("The series is non-stationary (fail to reject H0).")


#-------------------------------------------------------------------------------------------------------------#

# Slide # 43

# Apply differencing
# df['Differenced'] = df['Value'].diff()

# # Plot original vs. differenced series
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series')
# plt.plot(df['Date'], df['Differenced'], label='Differenced Series', color='orange')
# plt.title("Differencing to Achieve Stationarity")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide 44


# # Apply log transformation
# df['Log Transformed'] = np.log(df['Value'].clip(lower=1))  # Clip to avoid log(0)

# # Plot original vs. log-transformed series
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series')
# plt.plot(df['Date'], df['Log Transformed'], label='Log Transformed Series', color='green')
# plt.title("Log Transformation to Stabilize Variance")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 45

# Apply square root transformation
# df['Square Root Transformed'] = np.sqrt(df['Value'].clip(lower=0))  # Clip to avoid sqrt of negative values

# # Plot original vs. square root transformed series
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series', alpha=0.7)
# plt.plot(df['Date'], df['Square Root Transformed'], label='Square Root Transformed Series', color='orange', alpha=0.7)
# plt.title("Square Root Transformation to Stabilize Variance")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

#Slide # 46

# from scipy.stats import linregress

# # Fit a linear trend line
# x = np.arange(len(df))
# slope, intercept, _, _, _ = linregress(x, df['Value'])
# df['Detrended'] = df['Value'] - (slope * x + intercept)

# # Plot original vs. detrended series
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series')
# plt.plot(df['Date'], df['Detrended'], label='Detrended Series', color='purple')
# plt.title("Detrending to Remove Linear Trends")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 51

# # Calculate moving average with a window of 10
# df['Moving Average'] = df['Value'].rolling(window=10).mean()

# # Plot original series and moving average
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series', alpha=0.7)
# plt.plot(df['Date'], df['Moving Average'], label='Moving Average (Window=10)', color='red', alpha=0.7)
# plt.title("Moving Average Smoothing")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 53

# from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# # Apply Simple Exponential Smoothing
# ses_model = SimpleExpSmoothing(df['Value']).fit(smoothing_level=0.2, optimized=False)
# df['SES'] = ses_model.fittedvalues

# # Plot original series and SES smoothed series
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series', alpha=0.7)
# plt.plot(df['Date'], df['SES'], label='SES (Alpha=0.2)', color='green', alpha=0.7)
# plt.title("Simple Exponential Smoothing")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 54

# from statsmodels.tsa.ar_model import AutoReg
# import matplotlib.pyplot as plt

# # Ensure there are no missing values in the data
# df = df.dropna()

# # Fit an AR(2) model
# ar_model = AutoReg(df['Value'], lags=2).fit()
# df['AR'] = ar_model.fittedvalues

# # Adjust the AR predictions to align with the original time series
# df['AR'] = df['AR'].shift(2)

# # Plot original series and AR predictions
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series', alpha=0.7)
# plt.plot(df['Date'], df['AR'], label='AR(2) Model', color='orange', alpha=0.7)
# plt.title("Autoregressive Model (AR)")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 56

# from statsmodels.tsa.arima.model import ARIMA

# # Fit an ARIMA(2, 1, 2) model
# arima_model = ARIMA(df['Value'], order=(2, 1, 2)).fit()
# df['ARIMA'] = arima_model.fittedvalues

# # Plot original series and ARIMA predictions
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Value'], label='Original Series', alpha=0.7)
# plt.plot(df['Date'], df['ARIMA'], label='ARIMA(2, 1, 2)', color='purple', alpha=0.7)
# plt.title("ARIMA Model")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 59

# # Train-Test Split
# train_size = int(len(df) * 0.8)
# train, test = df[:train_size], df[train_size:]

# # Plot train and test sets
# plt.figure(figsize=(10, 5))
# plt.plot(train['Date'], train['Value'], label='Train Data', alpha=0.7)
# plt.plot(test['Date'], test['Value'], label='Test Data', alpha=0.7, color='orange')
# plt.title("Train-Test Split")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

#-------------------------------------------------------------------------------------------------------------#

# Slide # 60

# from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
# import numpy as np

# # Train-Test Split
# train_size = int(len(df) * 0.8)
# train, test = df[:train_size], df[train_size:]


# # Generate dummy predictions (for demonstration purposes)
# test['Predictions'] = test['Value'] + np.random.normal(0, 2, len(test))

# # Calculate metrics
# mse = mean_squared_error(test['Value'], test['Predictions'])
# rmse = np.sqrt(mse)
# mape = mean_absolute_percentage_error(test['Value'], test['Predictions'])

# # Print metrics
# print("Mean Squared Error (MSE):", mse)
# print("Root Mean Squared Error (RMSE):", rmse)
# print("Mean Absolute Percentage Error (MAPE):", mape)

#-------------------------------------------------------------------------------------------------------------#

# Slide # 61

# from statsmodels.tsa.arima.model import ARIMA
# from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# # Train-Test Split
# train_size = int(len(df) * 0.8)
# train, test = df[:train_size], df[train_size:]

# # Fit ARIMA model on train data
# arima_model = ARIMA(train['Value'], order=(2, 1, 2)).fit()

# # Print model summary
# print(arima_model.summary())

# # Forecast on test data
# forecast = arima_model.get_forecast(steps=len(test))
# forecast_values = forecast.predicted_mean
# conf_int = forecast.conf_int(alpha=0.05)

# # Add forecast values to the test dataframe
# test['ARIMA Forecast'] = forecast_values

# # Evaluate Accuracy Metrics
# mse = mean_squared_error(test['Value'], test['ARIMA Forecast'])
# rmse = np.sqrt(mse)
# mape = mean_absolute_percentage_error(test['Value'], test['ARIMA Forecast'])

# # Print metrics
# print("Evaluation Metrics:")
# print(f"Mean Squared Error (MSE): {mse:.2f}")
# print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
# print(f"Mean Absolute Percentage Error (MAPE): {mape:.2%}")

# # Plot original series, ARIMA forecasts, and confidence intervals
# plt.figure(figsize=(12, 6))

# # Plot train data
# plt.plot(train['Date'], train['Value'], label='Train Data', alpha=0.7)

# # Plot test data
# plt.plot(test['Date'], test['Value'], label='Test Data', alpha=0.7)

# # Plot ARIMA forecasts
# plt.plot(test['Date'], test['ARIMA Forecast'], label='ARIMA Forecast', color='red', linestyle='--')

# # Plot confidence intervals
# plt.fill_between(test['Date'], conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3, label='95% Confidence Interval')

# plt.title("ARIMA Model Forecasting with Confidence Intervals")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.legend()
# plt.grid()
# plt.show()

# # Residual Diagnostics
# residuals = train['Value'] - arima_model.fittedvalues
# plt.figure(figsize=(10, 5))
# plt.plot(residuals, label='Residuals', color='orange')
# plt.axhline(0, linestyle='--', color='gray')
# plt.title("Residual Diagnostics")
# plt.xlabel("Time")
# plt.ylabel("Residuals")
# plt.legend()
# plt.grid()
# plt.show()

# # Residual Histogram
# import seaborn as sns
# sns.histplot(residuals, kde=True, bins=20, color='blue')
# plt.title("Residual Histogram")
# plt.xlabel("Residual Value")
# plt.ylabel("Frequency")
# plt.grid()
# plt.show()
