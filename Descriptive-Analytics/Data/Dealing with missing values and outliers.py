# Step 1: Load Dataset

import numpy as np
from scipy import stats
import pandas as pd

# Load the dataset
df = pd.read_csv('Descriptive-Analytics\Student_Grades.csv')

# # Show the dataset
print("Original DataFrame:")
print(df)

# #-----------------------------------#

# #Step 2: Dealing with Missing Values

# # 2.1. Remove Rows with Missing Values
#     # Remove rows where any column has a missing value

# df_dropped_rows = df.dropna()

# print("\nDataFrame after removing rows with missing values:")
# print(df_dropped_rows)

# # 2.2. Remove Columns with Missing Values
#     # Remove columns that contain any missing values

# df_dropped_columns = df.dropna(axis=1)

# print("\nDataFrame after removing columns with missing values:")
# print(df_dropped_columns)

# # 2.3. Impute Missing Values Using Mean (for Numerical Data)
#     # Fill missing values in 'Age', 'Income', and 'Sales' with the mean of the respective columns

df_filled_mean = df.fillna(df.mean(numeric_only=True))

print("\nDataFrame after filling missing values with mean:")
print(df_filled_mean)

# # 2.4. Impute Missing Values Using Forward Fill
#     # Fill missing values using forward fill (fills with the previous row's value)

df_ffill = df.fillna(method='ffill')

print("\nDataFrame after forward filling missing values:")
print(df_ffill)

# # 2.5. Impute Missing Values Using Backward Fill
#     # Fill missing values using backward fill (fills with the next row's value)

df_bfill = df.fillna(method='bfill')

print("\nDataFrame after backward filling missing values:")
print(df_bfill)

# #-----------------------------------#

# # Step 3: Handling Outliers

# # 3.1. Detect and Remove Outliers Using IQR (Interquartile Range)
#     # Outliers in the Age column can be detected and removed using the IQR method.

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# # # # # Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# # # # Detect outliers
print(df['Age'] < lower_bound)
outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]

print(f"\nOutliers detected in Age column (using IQR):\n{outliers}")

# # # # Remove outliers
df_no_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

print("\nDataFrame after removing outliers:")
print(df_no_outliers)

# #3.2. Capping Outliers (Setting Upper/Lower Bound on Outliers)
#     #Instead of removing outliers, you can cap them at the upper or lower bounds.

# # Cap the outliers in the Age column
# df['Age_capped'] = df['Age'].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))

# print("\nDataFrame after capping outliers in Age column:")
# print(df[['Name', 'Age', 'Age_capped']])

#3.3. Detect and Remove Outliers Using Z-score
    # You can also use the Z-score method to detect and handle outliers.
    # A Z-score greater than 3 indicates a potential outlier.


# Calculate Z-scores for the Age column
ages = df['Age'].dropna()
z_scores = np.abs(stats.zscore(ages))  # dropna to ignore NaNs
threshold = 3  # Common threshold for Z-scores
outliers_z = ages.iloc[(z_scores > threshold).values]

mathscore = df['MathScore'].dropna()
z_scores = np.abs(stats.zscore(mathscore))  # dropna to ignore NaNs
threshold = 3  # Common threshold for Z-scores
outliers_z = mathscore.iloc[(z_scores > threshold).values]

print(z_scores)

print("\nOutliers detected in Age column (using Z-score):")
print(outliers_z)


# Remove outliers based on Z-score
# df_no_outliers_z = df.iloc[(z_scores <= threshold).values]

# print("\nDataFrame after removing outliers (based on Z-score):")
# print(df_no_outliers_z)


# Recap of Steps:
# Removing missing values: Demonstrates how to remove rows or columns with missing data.
# Imputing missing values: Shows how to fill missing values with methods like mean, forward fill, or backward fill.
# Handling outliers: Demonstrates detecting and handling outliers using both the IQR method and Z-score.
