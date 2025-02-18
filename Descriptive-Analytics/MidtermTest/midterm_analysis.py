import numpy as np
import pandas as pd
import scipy as sc
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# READING AND FORMATTING DATA

data = pd.read_csv('MidtermTest\healthData.csv')
data = data.astype({'heart_attack': 'category', 'work_out_habit': 'category', 'gender': 'category',
              'smoking_habit': 'category', 'education': 'category'})
data.dtypes

# print(data)

# # Variables for numerical 

numerical = data[['age', 'salary']]
categorical = data.drop(['age', 'salary'], axis=1)


# # # Calculate descriptive statistics
# mean = numerical.mean()
# median = numerical.median()
# mode = numerical.mode()
# maximum = numerical.max()
# minimum = numerical.min()
# variance = numerical.var() #square of std dev
# std_dev = numerical.std() #requires mean
# skewness = numerical.skew()
# kurtosis = numerical.kurtosis()
# distribution_range = maximum - minimum

# # # Display the results
# print(f'Mean: \n{mean}\n')
# print(f'Median: \n{median}\n')
# print(f'Maximum: \n{maximum}\n')
# print(f'Minimum: \n{minimum}\n')
# print(f'Variance: \n{variance}\n')
# print(f'Standard Deviation: \n{std_dev}\n')
# print(f'Skewness: \n{skewness}\n')

# print(f'Kurtosis: \n{kurtosis}\n') 
# # # It helps in understanding the distribution's extremities
# # # particularly how heavy (has extreme values) or light the tails are compared to a normal distribution
# print(f'Range: \n{distribution_range}\n')

# # # # Using describe function
# summary = data.describe()
# print(summary)

# Histogram for 'age'
# plt.hist(data['age'].dropna(), bins=20)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# # Histogram for 'salary'
# plt.hist(data['salary'].dropna(), bins=20)
# plt.title('Salary Distribution')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.show()

# # Boxplot for 'age'
# plt.boxplot(data['age'].dropna())
# plt.title('Boxplot of Age')
# plt.ylabel('Age')
# plt.show()

# # Boxplot for 'salary'
# plt.boxplot(data['salary'].dropna())
# plt.title('Boxplot of Salary')
# plt.ylabel('Salary')
# plt.show()

# # # Percentiles (25th, 50th, 75th percentiles) and IQR
# # percentile_25 = data.quantile(0.25)
# # percentile_50 = data.quantile(0.50)  # Same as median
# # percentile_75 = data.quantile(0.75)
# # percentile_1 = data.quantile(0.01)
# # percentile_10 = data.quantile(0.10)
# # percentile_90 = data.quantile(0.90)
# # percentile_99 = data.quantile(0.99)

# # Inter_Quartile_Range = percentile_75 - percentile_25

# # print(f'1st Percentile (Median): {percentile_1}')
# # print(f'25th Percentile: {percentile_25}')
# # print(f'50th Percentile (Median): {percentile_50}')
# # print(f'75th Percentile: {percentile_75}')

# # print(f'10th Percentile: {percentile_10}')
# # print(f'90th Percentile: {percentile_90}')
# # print(f'99th Percentile: {percentile_99}')

# # print(f'IQR: {Inter_Quartile_Range}')



# print(data.head()) # print out the first 5 lines of sample file

# gender_cat = data['gender'].cat.categories.values
# print(f'List of Gender Categories: {gender_cat}')

# smoking_cat = data['smoking_habit'].cat.categories.values
# print(f'List of Smoking Categories: {smoking_cat}')

# HeartAttack_cat = data['heart_attack'].cat.categories.values
# print(f'List of Heart Attack Categories: {HeartAttack_cat}')

# education_cat = data['education'].cat.categories.values
# print(f'List of Education Categories: {education_cat}')

# workout_cat = data['work_out_habit'].cat.categories.values
# print(f'List of Workout Categories: {workout_cat}')


## Relative Frequency: How often something happens divided by all outcomes

# # Descriptive statistics for 'gender'
# print("\nFrequency distribution for 'gender':")
# print(data['gender'].value_counts())
# print("Relative frequency distribution for 'gender':")
# print(data['gender'].value_counts(normalize=True))

# print("\nFrequency distribution for 'work_out_habit':")
# print(data['work_out_habit'].value_counts())
# print("Relative frequency distribution for 'work_out_habit':")
# print(data['work_out_habit'].value_counts(normalize=True))

# print("\nFrequency distribution for 'smoking_habit':")
# print(data['smoking_habit'].value_counts())
# print("Relative frequency distribution for 'smoking_habit':")
# print(data['smoking_habit'].value_counts(normalize=True))

# print("\nFrequency distribution for 'heart_attack':")
# print(data['heart_attack'].value_counts())
# print("Relative frequency distribution for 'heart_attack':")
# print(data['heart_attack'].value_counts(normalize=True))

# print("\nFrequency distribution for 'education':")
# print(data['education'].value_counts())
# print("Relative frequency distribution for 'education':")
# print(data['education'].value_counts(normalize=True))


# #Bar Chart
# # USED FOR CATEGORICAL DATA

# data['gender'].value_counts().plot(kind='bar')
# plt.title('Gender Distribution')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# data['work_out_habit'].value_counts().plot(kind='bar')
# plt.title('Workout Habits')
# plt.xlabel('Habits')
# plt.ylabel('Count')
# plt.show()

# data['smoking_habit'].value_counts().plot(kind='bar')
# plt.title('Smoking Habits')
# plt.xlabel('Habits')
# plt.ylabel('Count')
# plt.show()

# data['heart_attack'].value_counts().plot(kind='bar')
# plt.title('Heart Attacks')
# plt.xlabel('Yes or No')
# plt.ylabel('Count')
# plt.show()

# data['education'].value_counts().plot(kind='bar')
# plt.title('Education Level')
# plt.xlabel('Degrees')
# plt.ylabel('Count')
# plt.show()

#Missing Values in Categorical
dfc_missing = data.replace({'work_out_habit': {None: 'None'}}, inplace=True)

# # REPLACE MISSING VALUES WITH MEDIAN

df_median_filled = numerical.fillna(numerical.median(numeric_only=True))

print("\nDataFrame after filling missing values with median:")
print(df_median_filled)

Q1 = df_median_filled['age'].quantile(0.25)
Q3 = df_median_filled['age'].quantile(0.75)
IQR = Q3 - Q1

# # Define outlier bounds (must be within these margins)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(lower_bound)
print(upper_bound)

# # Detect outliers w/IQR

print(df_median_filled['age'] < lower_bound)
outliers = df_median_filled[(df_median_filled['age'] < lower_bound) | (df_median_filled['age'] > upper_bound)]

print(f"\nOutliers detected in Age column (using IQR):\n{outliers}")

print("\nDataFrame after removing outliers:")

# # Remove outliers w/IQR

df_no_out = df_median_filled[(df_median_filled['age'] >= lower_bound) & (df_median_filled['age'] <= upper_bound)]

Q1_salary = data['salary'].quantile(0.25)
Q3_salary = data['salary'].quantile(0.75)
IQR_salary = Q3_salary - Q1_salary
lower_bound_salary = Q1_salary - 1.5 * IQR_salary
upper_bound_salary = Q3_salary + 1.5 * IQR_salary
# Remove outliers from 'salary'
healthData = data[(data['salary'] >= lower_bound_salary) & (data['salary'] <= upper_bound_salary)]

print(healthData)

# # Descriptive statistics for 'age' after cleaning
print("\nDescriptive statistics for 'age' after cleaning:")
print(df_no_out['age'].describe())
print("Skewness of 'age' after cleaning:", df_no_out['age'].skew())
print("Kurtosis of 'age' after cleaning:", df_no_out['age'].kurtosis())

# # Descriptive statistics for 'salary' after cleaning
print("\nDescriptive statistics for 'salary' after cleaning:")
print(healthData['salary'].describe())
print("Skewness of 'salary' after cleaning:", healthData['salary'].skew())
print("Kurtosis of 'salary' after cleaning:", healthData['salary'].kurtosis())

# # Histogram for 'age'
# plt.hist(df_no_out['age'].dropna(), bins=20)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# Histogram for 'salary'
plt.hist(healthData['salary'].dropna(), bins=20)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# # # Boxplot for 'age'
# plt.boxplot(df_no_out['age'].dropna())
# plt.title('Boxplot of Age')
# plt.ylabel('Age')
# plt.show()

# # Boxplot for 'salary'
plt.boxplot(healthData['salary'].dropna())
plt.title('Boxplot of Salary')
plt.ylabel('Salary')
plt.show()