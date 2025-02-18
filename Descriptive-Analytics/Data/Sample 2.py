import pandas as pd
import numpy as np

# Sample dataset
data = {
     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
     'Age': [25, 200, 35, 45, 23],  # 200 is an outlier
     'Salary': [50000, 60000, 70000, 80000, 90000]
 }

df = pd.DataFrame(data)

 # Show the dataset
#print("Original DataFrame:")
#print(df)

 # 1. Detecting outliers using IQR (Interquartile Range)
#Q1 = df['Age'].quantile(0.25)
#Q3 = df['Age'].quantile(0.75)
#IQR = Q3 - Q1

# # Define outlier thresholds
#lower_bound = Q1 - 1.5 * IQR
#upper_bound = Q3 + 1.5 * IQR

# print(f"\nOutlier thresholds: Lower bound = {lower_bound}, Upper bound = {upper_bound}")
# print(df.describe())

# # Identify and filter outliers
#outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
# print("\nDetected Outliers:")
# print(outliers)

# # 2. Removing outliers
#df_no_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
#print("\nDataFrame after removing outliers:")
#print(df_no_outliers)

# # 3. Capping outliers (e.g., setting a maximum/minimum limit)
# df['Age_capped'] = np.where(df['Age'] > upper_bound, upper_bound, 
#                             np.where(df['Age'] < lower_bound, lower_bound, df['Age']))
# print("\nDataFrame after capping outliers:")
# print(df)

# # 2. Z-Score

from scipy import stats

# # Using Z-score for outlier detection
z_scores = np.abs(stats.zscore(df['Age'].dropna()))
threshold = 3  # Common threshold is 3 for Z-score
outliers_z = df[z_scores > threshold]

print("\nOutliers detected using Z-score:")
print(outliers_z)

# # Removing Z-score outliers
# df_no_outliers_z = df[z_scores <= threshold]
# print("\nDataFrame after removing Z-score outliers:")
# print(df_no_outliers_z)
