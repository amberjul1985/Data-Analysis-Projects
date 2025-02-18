# # Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# # Load the dataset into a DataFrame
healthData = pd.read_csv('MidtermTest\healthData.csv')

# # Step 3: Perform Descriptive Statistics
# # -------------------------------------
# Descriptive statistics for numerical variables ('age' and 'salary')
# Including mean, median, mode, standard deviation, variance, min, max, range, percentiles, IQR, skewness, and kurtosis

# # Descriptive statistics for 'age'
# print("Descriptive statistics for 'age':")
# print(healthData['age'].describe())
# print("Mode of 'age':", healthData['age'].mode()[0])
# print("Skewness of 'age':", healthData['age'].skew())
# print("Kurtosis of 'age':", healthData['age'].kurtosis())
# print("Percentiles for 'age':", healthData['age'].quantile([0.01, 0.10, 0.25, 0.75, 0.90, 0.99]))
# IQR_age = healthData['age'].quantile(0.75) - healthData['age'].quantile(0.25)
# print("IQR (Interquartile Range) of 'age':", IQR_age)

# # # Descriptive statistics for 'salary'
# print("\nDescriptive statistics for 'salary':")
# print(healthData['salary'].describe())
# print("Mode of 'salary':", healthData['salary'].mode()[0])
# print("Skewness of 'salary':", healthData['salary'].skew())
# print("Kurtosis of 'salary':", healthData['salary'].kurtosis())
# print("Percentiles for 'salary':", healthData['salary'].quantile([0.01, 0.10, 0.25, 0.75, 0.90, 0.99]))
# IQR_salary = healthData['salary'].quantile(0.75) - healthData['salary'].quantile(0.25)
# print("IQR (Interquartile Range) of 'salary':", IQR_salary)

# # Descriptive statistics for categorical variables
# # Including mode, frequency distribution, and relative frequency

# # Descriptive statistics for 'gender'
# print("\nFrequency distribution for 'gender':")
# print(healthData['gender'].value_counts())
# print("Relative frequency distribution for 'gender':")
# print(healthData['gender'].value_counts(normalize=True))

# print("\nFrequency distribution for 'gender':")
# print(healthData['gender'].value_counts())
# print("Relative frequency distribution for 'gender':")
# print(healthData['gender'].value_counts(normalize=True))


# # Step 3: Visualizations
# # ----------------------
# # Bar chart for 'gender'
# healthData['gender'].value_counts().plot(kind='bar')
# plt.title('Gender Distribution')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# # Histogram for 'age'
# plt.hist(healthData['age'].dropna(), bins=20)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# # Histogram for 'salary'
# plt.hist(healthData['salary'].dropna(), bins=20)
# plt.title('Salary Distribution')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.show()

# # Boxplot for 'age'
# plt.boxplot(healthData['age'].dropna())
# plt.title('Boxplot of Age')
# plt.ylabel('Age')
# plt.show()

# # Boxplot for 'salary'
# plt.boxplot(healthData['salary'].dropna())
# plt.title('Boxplot of Salary')
# plt.ylabel('Salary')
# plt.show()

# # Step 4: Handle Missing Values and Outliers
# # ------------------------------------------
# # Impute missing values in 'age' and 'salary' using the median of each column
# healthData['age'].fillna(healthData['age'].median(), inplace=True)
# healthData['salary'].fillna(healthData['salary'].median(), inplace=True)

# # Handle outliers in 'age' using the IQR method
# Q1_age = healthData['age'].quantile(0.25)
# Q3_age = healthData['age'].quantile(0.75)
# IQR_age = Q3_age - Q1_age
# lower_bound_age = Q1_age - 1.5 * IQR_age
# upper_bound_age = Q3_age + 1.5 * IQR_age
# # Remove outliers from 'age'
# healthData = healthData[(healthData['age'] >= lower_bound_age) & (healthData['age'] <= upper_bound_age)]

# # Handle outliers in 'salary' using the IQR method
# Q1_salary = healthData['salary'].quantile(0.25)
# Q3_salary = healthData['salary'].quantile(0.75)
# IQR_salary = Q3_salary - Q1_salary
# lower_bound_salary = Q1_salary - 1.5 * IQR_salary
# upper_bound_salary = Q3_salary + 1.5 * IQR_salary
# # Remove outliers from 'salary'
# healthData = healthData[(healthData['salary'] >= lower_bound_salary) & (healthData['salary'] <= upper_bound_salary)]

# # Step 3 (Re-run): Perform Descriptive Statistics After Cleaning
# # -------------------------------------------------------------
# # Descriptive statistics for 'age' after cleaning
# print("\nDescriptive statistics for 'age' after cleaning:")
# print(healthData['age'].describe())
# print("Skewness of 'age' after cleaning:", healthData['age'].skew())
# print("Kurtosis of 'age' after cleaning:", healthData['age'].kurtosis())

# # Descriptive statistics for 'salary' after cleaning
# print("\nDescriptive statistics for 'salary' after cleaning:")
# print(healthData['salary'].describe())
# print("Skewness of 'salary' after cleaning:", healthData['salary'].skew())
# print("Kurtosis of 'salary' after cleaning:", healthData['salary'].kurtosis())

# # Re-run Visualizations After Cleaning
# # Bar chart for 'gender' after cleaning
# healthData['gender'].value_counts().plot(kind='bar')
# plt.title('Gender Distribution After Cleaning')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# # Histogram for 'age' after cleaning
# plt.hist(healthData['age'].dropna(), bins=20)
# plt.title('Age Distribution After Cleaning')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# # Histogram for 'salary' after cleaning
# plt.hist(healthData['salary'].dropna(), bins=20)
# plt.title('Salary Distribution After Cleaning')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.show()

# # Boxplot for 'age' after cleaning
# plt.boxplot(healthData['age'].dropna())
# plt.title('Boxplot of Age After Cleaning')
# plt.ylabel('Age')
# plt.show()

# # Boxplot for 'salary' after cleaning
# plt.boxplot(healthData['salary'].dropna())
# plt.title('Boxplot of Salary After Cleaning')
# plt.ylabel('Salary')
# plt.show()
