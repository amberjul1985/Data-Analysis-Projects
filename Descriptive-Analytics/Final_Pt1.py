import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from scipy.stats import chi2_contingency
from scipy.stats import zscore
import numpy as np
from re import X
from statsmodels.stats.diagnostic import het_breuschpagan

# DATA CLEANING + PREP

# print(Crossd.head())  # Check the first few rows
# print(Crossd.shape)   # Ensure it's not empty
# print("Minimum expected frequency:", expected1.min())
# print("Minimum expected frequency:", expected2.min())

# Combine sparse categories
# Crossed = Cross.loc[(Cross.sum(axis=1) >= 5), :]  # Filter rows
# Crosseed = Crossed.loc[:, (Crossed.sum(axis=0) >= 5)]  # Filter columns
# chi2_stat3, chi2_p_val3, dof3, expected3 = chi2_contingency(Crosseed)
# print(f'Chi-Squared Test 1 Results: Chi-squared stat: {chi2_stat3}, P-value: {chi2_p_val3}')
# print("Minimum expected frequency:", expected3.min())

# # DataFrames
# df1 = pd.read_csv('LAHD_Affordable_Housing_MOD.csv')
# df2 = pd.read_csv('Crime_Data_MOD.csv')

# # Merge the DataFrames
# result = pd.merge(df1, df2, on='LAT + LON', how='outer')

# # Save to a CSV file
# # index=False prevents saving the row indices
# result.to_csv('output.csv', index=False)

# # Sample DataFrames
# df1 = pd.read_csv('sampled_output.csv')
# df2 = pd.read_csv('New_Apartment_MOD.csv')

# # Merge the DataFrames
# result = pd.merge(df1, df2, on='Zip Code', how='outer')

# # Save to a CSV file
# # index=False prevents saving the row indices
# result.to_csv('2_Merge_output.csv', index=False)

# # Sample DataFrames
# df1 = pd.read_csv('2_Merge_output.csv')
# df2 = pd.read_csv('sampled3_output.csv')
# # df2 = pd.read_csv('new_buildings_MOD.csv')

# # Merge the DataFrames
# result = pd.merge(df1, df2, on='Zip Code', how='outer')

# # Save to a CSV file
# # index=False prevents saving the row indices
# result.to_csv('Final_Merge_output.csv', index=False)

# # Load your combined dataset
# df = pd.read_csv('Final_Project_Joined_HousingDataset.csv')

# # Define the proportion of rows to keep (e.g., 10% of the original size)
# sample_fraction = 0.1

# # Stratified sampling based on the 'LAT + LON' column
# sampled_df = (
#     # Group by the stratification key
#     df.groupby('Zip Code', group_keys=False)
#     # Sample from each group
#     .apply(lambda x: x.sample(frac=sample_fraction, random_state=42))
# )

# # Save the reduced dataset to a new CSV file
# sampled_df.to_csv('stratified_sample_output.csv', index=False)

# df = pd.read_csv('stratified_sample_output.csv')

# # Fill missing values in numerical columns with the mean
# df_filled_mean = df.fillna(df.mean(numeric_only=True))

# # Select only numeric columns
# numeric_df = df_filled_mean.select_dtypes(include=['number'])
# numeric_columns = numeric_df.columns

# # Compute quantiles and IQR
# Q1 = numeric_df.quantile(0.25)
# Q3 = numeric_df.quantile(0.75)
# IQR = Q3 - Q1

# # Define outlier bounds
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# # Identify and remove outliers
# df_no_outliers = df_filled_mean[
#     ~((df_filled_mean[numeric_columns] < lower_bound) |
#       (df_filled_mean[numeric_columns] > upper_bound)).any(axis=1)
# ]

# # Fill missing values in categorical columns with the mode
# categorical_cols = df_no_outliers.select_dtypes(
#     include=['object', 'category']).columns
# df_filled_mode = df_no_outliers.copy()
# df_filled_mode[categorical_cols] = df_no_outliers[categorical_cols].fillna(
#     df_no_outliers[categorical_cols].mode().iloc[0])

# print("\nDataFrame after filling missing values with mode (categorical) and mean (numerical):")
# print(df_filled_mode)

# df_no_outliers.to_csv('LAHousing_AnalysisPrepped_Dataset.csv')

# df = pd.read_csv('/content/LAHousing_AnalysisPrepped_Dataset.csv')

# df['Zip Code'] = 'A' + df['Zip Code'].astype(str)

# Correlation Matrix

# p = df.select_dtypes(exclude=['object', 'category'])

# # Correctly selecting the columns for the correlation matrix
# correlation_matrix = p[['SITE UNITS', 'PROJECT TOTAL UNITS', 'LAHD FUNDED',
#                         'LEVERAGE', 'TECB', 'TDC', 'Valuation_x',
#                         'Valuation_y', 'Residential Units_y']].corr()

# # covariance_matrix = p.cov()
# print(correlation_matrix)
# # print(covariance_matrix)

# plt.figure(figsize=(18, 18))
# sns.heatmap(correlation_matrix, square=True, cmap="RdBu_r", linewidth=.5,
#             vmin=-1, vmax=1, annot=True, annot_kws={"size": 18}, fmt='.2f')  # annot = annotations which include numbers for correlation coeffecient
# # fmt='.2f' = format that only includes the first 2 decimal places

# plt.yticks(fontsize=14)
# plt.xticks(rotation=30, fontsize=14)
# plt.title('Correlation Co', fontsize=18)
# plt.show()

# ________________________________________________________________________
### RESEARCH QUESTIONS

## Q1

# numeric_df = df_mean.select_dtypes(include=['number'])

# print(numeric_df)
# print(df['TDC'].describe())
# print(df['PROJECT TOTAL UNITS'].describe())

# skewness1 = df['TDC'].skew()
# kurtosis1 = df['TDC'].kurtosis()
# skewness2 = df['PROJECT TOTAL UNITS'].skew()
# kurtosis2 = df['PROJECT TOTAL UNITS'].kurtosis()

# print(f'Skewness: {skewness1}')
# print(f'Kurtosis: {kurtosis1}')
# print(f'Skewness: {skewness2}')
# print(f'Kurtosis: {kurtosis2}')

# X = df[['TDC']]
# y = df['PROJECT TOTAL UNITS']

# # # Fit the model
# model = LinearRegression()
# model.fit(X, y)
# # # #---

# print("Coeffecient", model.coef_[0])
# print("Intercept", model.intercept_)

# yPred=model.predict(X)
# error= mean_squared_error(y, yPred)
# print("Error", error)

# # # Evaluating the model

# r_squared = model.score(X, y)
# print('R-squared:', r_squared)

# X_with_const = sm.add_constant(X)
# model_sm = sm.OLS(y, X_with_const).fit()
# print(model_sm.summary())

# # # Assumptions Check

# residuals = y - model.predict(X)
# plt.hist(residuals, bins=20)
# plt.title('Residuals Distribution')
# plt.show()

# # Scatter plot and regression line
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.xlabel('TOTAL DEVELOPMENT COSTS')
# plt.ylabel('PROJECT TOTAL UNITS')
# plt.title('Simple Linear Regression')
# plt.show()

## Q2

# print(df['LAHD FUNDED'].describe())
# print(df['TDC'].describe())

# skewness1 = df['LAHD FUNDED'].skew()
# kurtosis1 = df['LAHD FUNDED'].kurtosis()
# skewness2 = df['TDC'].skew()
# kurtosis2 = df['TDC'].kurtosis()

# print(f'Skewness: {skewness1}')
# print(f'Kurtosis: {kurtosis1}')
# print(f'Skewness: {skewness2}')
# print(f'Kurtosis: {kurtosis2}')

# X = df[['LAHD FUNDED']]
# y = df['TDC']

# # # Fit the model
# model = LinearRegression()
# model.fit(X, y)
# # # #---

# print("Coeffecient", model.coef_[0])
# print("Intercept", model.intercept_)

# yPred=model.predict(X)
# error= mean_squared_error(y, yPred)
# print("Error", error)

# # # Evaluating the model

# r_squared = model.score(X, y)
# print('R-squared:', r_squared)

# X_with_const = sm.add_constant(X)
# model_sm = sm.OLS(y, X_with_const).fit()
# print(model_sm.summary())

# # # Assumptions Check

# residuals = y - model.predict(X)
# plt.hist(residuals, bins=20)
# plt.title('Residuals Distribution')
# plt.show()

# # Scatter plot and regression line
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.xlabel('LAHD FUNDED')
# plt.ylabel('TDC')
# plt.title('Simple Linear Regression')
# plt.show()

## Q3 

# print(df['Crm Cd Desc'].describe())
# print(df['SITE ADDRESS'].describe())

# Crossd = pd.crosstab(df['Crm Cd Desc'], df['SITE ADDRESS'])
# chi2_stat2, chi2_p_val2, dof2, expected2 = chi2_contingency(Crossd)
# print(f'Chi-Squared Test Results: Chi-squared stat: {chi2_stat2}, P-value: {chi2_p_val2}')

# # Descriptive statistics for 'SITE ADDRESS'
# print("\nFrequency distribution for 'SITE ADDRESS':")
# print(df['SITE ADDRESS'].value_counts())
# print("Relative frequency distribution for 'SITE ADDRESS':")
# print(df['SITE ADDRESS'].value_counts(normalize=True))

# # Descriptive statistics for 'Crime Type'
# print("\nFrequency distribution for 'Crime Type':")
# print(df['Crm Cd Desc'].value_counts())
# print("Relative frequency distribution for 'Crm Cd Desc':")
# print(df['Crm Cd Desc'].value_counts(normalize=True))

#  Example Chi-Squared Test: Testing relationship between Crime Type and Site Address
# contingency_table = pd.crosstab(df_mode['Crm Cd Desc'], df_mode['SITE ADDRESS'])
# chi2_stat, chi2_p_val, dof, expected = stats.chi2_contingency(contingency_table)
# print(f'Chi-Squared Test Results: chi2_stat = {chi2_stat}, p-value = {chi2_p_val}')

# # Overall most widespread crime
# most_widespread_crime = df['Crm Cd Desc'].value_counts()
# print(most_widespread_crime.head())

# # Crime frequency by location
# crime_by_location = df.groupby(['Zip Code', 'Crm Cd Desc']).size().reset_index(name='Count')
# crime_by_location = crime_by_location.sort_values(by='Count', ascending=False)
# print(crime_by_location.head())

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Top 10 most frequent crimes
# top_crimes = most_widespread_crime.head(10)
# sns.barplot(x=top_crimes.values, y=top_crimes.index, palette="viridis")
# plt.title("Top 10 Most Frequent Crimes")
# plt.xlabel("Frequency")
# plt.ylabel("Crime Type")
# plt.show()

# # Heatmap for crimes by location
# crime_pivot = crime_by_location.pivot(index='Zip Code', columns='Crm Cd Desc', values='Count').fillna(0)
# sns.heatmap(crime_pivot, cmap='YlGnBu', linewidths=0.5)
# plt.title("Crime Types by Location (Heatmap)")
# plt.show()

# from scipy.stats import chi2_contingency

# # Create contingency table
# contingency_table = pd.crosstab(df['SITE ADDRESS'], df['Crm Cd Desc'])

# # Perform Chi-Square Test
# chi2, p, dof, expected = chi2_contingency(contingency_table)

# print(f"Chi-Square Statistic: {chi2}")
# print(f"P-Value: {p}")

# if p < 0.05:
#     print("Significant variation in crime types across locations.")
# else:
#     print("No significant variation in crime types across locations.")

## Q4

# print(df['Crm Cd Desc'].describe())
# print(df['Work Description_x'].describe())

# Crossd = pd.crosstab(df['Crm Cd Desc'], df['Work Description_x'])
# chi2_stat2, chi2_p_val2, dof2, expected2 = chi2_contingency(Crossd)
# print(
#     f'Chi-Squared Test 1 Results: Chi-squared stat: {chi2_stat2}, P-value: {chi2_p_val2}')

# crime_by_apartment_type = df.groupby(
#     'Work Description_x').size().reset_index(name='CrimeCount')

# crime_by_apartment_type_sorted = crime_by_apartment_type.sort_values(
#     by='CrimeCount', ascending=False)

# plt.figure(figsize=(10, 6))
# sns.barplot(data=crime_by_apartment_type_sorted.head(10),
#             x='CrimeCount', y='Work Description_x', palette="plasma")

# plt.title('Top 10 Apartment Types with Most Homelessness Crimes', fontsize=16)
# plt.xlabel('Crime Count', fontsize=12)
# plt.ylabel('Apartment Type', fontsize=12)
# plt.show()

## Q5

# #Descriptive statistics for 'LAHD FUNDED'
# print("\nDescriptive statistics for 'LAHD FUNDED' after cleaning:")
# print(df['LAHD FUNDED'].describe())
# print("Mode of 'LAHD FUNDED':", df['LAHD FUNDED'].mode()[0])
# print("Skewness of 'LAHD FUNDED':", df['LAHD FUNDED'].skew())
# print("Kurtosis of 'LAHD FUNDED':", df['LAHD FUNDED'].kurtosis())
# print("Percentiles for 'LAHD FUNDED':", df['LAHD FUNDED'].quantile([0.01, 0.10, 0.25, 0.75, 0.90, 0.99]))
# IQR_LAHDFUNDED = df['LAHD FUNDED'].quantile(0.75) - df['LAHD FUNDED'].quantile(0.25)
# print("IQR (Interquartile Range) of 'LAHD FUNDED':", IQR_LAHDFUNDED)
# print("Range of 'LAHD FUNDED':", df['LAHD FUNDED'].max()- df['LAHD FUNDED'].min())

# # Descriptive statistics for 'HOUSING TYPE'
# print("\nFrequency distribution for 'HOUSING TYPE':")
# print(df['HOUSING TYPE'].value_counts())
# print("Relative frequency distribution for 'HOUSING TYPE':")
# print(df['HOUSING TYPE'].value_counts(normalize=True))

#Boxplot 
# sns.boxplot(data=df, y='LAHD FUNDED', notch=True)  # Use 'y' for vertical boxplots
# plt.title('Distribution of LAHD funded housing', fontsize=14)
# plt.ylabel('LAHD funded housing')
# plt.show()


#T-test: HOUSING TYPE & LAHD FUNDED
# group_FAMILY = df[df['HOUSING TYPE'] == 'FAMILY']['LAHD FUNDED']
# group_SENIORS = df[df['HOUSING TYPE'] == 'SENIORS']['LAHD FUNDED']
# t_stat, p_value = stats.ttest_ind(group_FAMILY, group_SENIORS)
# print(f'T-Test Results: t-statistic = {t_stat}, p-value = {p_value}')


## Q6

# # Simple Linear Regression
# p = df.select_dtypes(exclude=['object', 'category'])
# df = p.fillna(df.mean(numeric_only=True))

# print(df['Valuation_x'].describe())
# skewness3 = df['Valuation_x'].skew()
# kurtosis3 = df['Valuation_x'].kurtosis()
# print(f'Skewness: {skewness3}')
# print(f'Kurtosis: {kurtosis3}')

# print(df['LAHD FUNDED'].describe())
# skewness4 = df['LAHD FUNDED'].skew()
# kurtosis4 = df['LAHD FUNDED'].kurtosis()
# print(f'Skewness: {skewness4}')
# print(f'Kurtosis: {kurtosis4}')


# X = df[['LAHD FUNDED']]
# y = df['Valuation_x']

# # Fit the model
# model = LinearRegression()
# model.fit(X, y)
# # #---

# print("Coeffecient", model.coef_[0])
# print("Intercept", model.intercept_)

# yPred = model.predict(X)
# error = mean_squared_error(y, yPred)
# print("Error", error)

# # Evaluating the model

# r_squared = model.score(X, y)
# print('R-squared:', r_squared)

# X_with_const = sm.add_constant(X)
# model_sm = sm.OLS(y, X_with_const).fit()
# print(model_sm.summary())

# # Assumptions Check

# residuals = y - model.predict(X)
# plt.hist(residuals, bins=20)
# plt.title('Residuals Distribution')
# plt.show()

# # Scatter plot and regression line
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.xlabel('Valuations for Apartments')
# plt.ylabel('Funding for Affordable Housing Project')
# plt.title('Simple Linear Regression')
# plt.show()

## Q7

# print("\nDescriptive statistics for 'Valuation_y' after cleaning:")
# print(df['Valuation_y'].describe())
# print("Mode of 'Valuation_y':", df['Valuation_y'].mode()[0])
# print("Skewness of 'Valuation_y':", df['Valuation_y'].skew())
# print("Kurtosis of 'Valuation_y':", df['Valuation_y'].kurtosis())
# print("Percentiles for 'Valuation_y':", df['Valuation_y'].quantile([0.01, 0.10, 0.25, 0.75, 0.90, 0.99]))
# IQR_LAHDFUNDED = df['Valuation_y'].quantile(0.75) - df['Valuation_y'].quantile(0.25)
# print("IQR (Interquartile Range) of 'Valuation_y':", IQR_LAHDFUNDED)
# print("Range of 'Valuation_y':", df['Valuation_y'].max()- df['Valuation_y'].min())

# print("\nFrequency distribution for 'Initiating Office_y':")
# print(df['Initiating Office_y'].value_counts())
# print("Relative frequency distribution for 'Initiating Office_y':")
# print(df['Initiating Office_y'].value_counts(normalize=True))

# sns.boxplot(data=df, y='Valuation_y', notch=True)  # Use 'y' for vertical boxplots
# plt.title('Distribution of New Buildings Valuation', fontsize=14)
# plt.ylabel('Building Valuation')
# plt.show()

# T-test: Initiating Office_y & Valuation_y
# group_METRO = df[df['Initiating Office_y'] == 'METRO']['Valuation_y']
# group_WESTLA = df[df['Initiating Office_y'] == 'WEST LA']['Valuation_y']
# t_stat, p_value = stats.ttest_ind(group_METRO, group_WESTLA)
# print(f'T-Test Results: t-statistic = {t_stat}, p-value = {p_value}')

## Q8

# print("\nDescriptive statistics for 'Valuation_x' after cleaning:")
# print(df['Valuation_x'].describe())
# print("Mode of 'Valuation_x':", df['Valuation_x'].mode()[0])
# print("Skewness of 'Valuation_x':", df['Valuation_x'].skew())
# print("Kurtosis of 'Valuation_x':", df['Valuation_x'].kurtosis())
# print("Percentiles for 'Valuation_x':", df['Valuation_x'].quantile([0.01, 0.10, 0.25, 0.75, 0.90, 0.99]))
# IQR_LAHDFUNDED = df['Valuation_x'].quantile(0.75) - df['Valuation_x'].quantile(0.25)
# print("IQR (Interquartile Range) of 'Valuation_x':", IQR_LAHDFUNDED)
# print("Range of 'Valuation_x':", df['Valuation_x'].max()- df['Valuation_x'].min())

# print("\nFrequency distribution for 'Initiating Office_x':")
# print(df['Initiating Office_x'].value_counts())
# print("Relative frequency distribution for 'Initiating Office_x':")
# print(df['Initiating Office_x'].value_counts(normalize=True))

# sns.boxplot(data=df, y='Valuation_x', notch=True)  # Use 'y' for vertical boxplots
# plt.title('Distribution of New Apartment Valuation', fontsize=14)
# plt.ylabel('Apartment Valuation')
# plt.show()

# F-test: Initiating Office_x & Valuation_x
# VANNUYS_group = df[df['Initiating Office_x'] == 'VAN NUYS']['Valuation_x']
# SOUTHLA_group = df[df['Initiating Office_x'] == 'SOUTH LA']['Valuation_x']
# f_stat, f_p_value = stats.levene(VANNUYS_group, SOUTHLA_group)
# print(f'F-Test Results: F-statistic = {f_stat}, p-value = {f_p_value}')


## Q9

# # Simple Linear Regression
# p = df.select_dtypes(exclude=['object', 'category'])
# df = p.fillna(df.mean(numeric_only=True))

# print(df['Valuation_y'].describe())
# skewness1 = df['Valuation_y'].skew()
# kurtosis1 = df['Valuation_y'].kurtosis()
# print(f'Skewness: {skewness1}')
# print(f'Kurtosis: {kurtosis1}')

# print(df['LAHD FUNDED'].describe())
# skewness2 = df['LAHD FUNDED'].skew()
# kurtosis2 = df['LAHD FUNDED'].kurtosis()
# print(f'Skewness: {skewness2}')
# print(f'Kurtosis: {kurtosis2}')

# # sns.boxplot(data=df, y='Valuation_y', notch=True)  # Use 'y' for vertical boxplots
# # plt.title('Distribution of New Buildings Valuation', fontsize=14)
# # plt.ylabel('Valuation')
# # plt.show()

# X = df[['LAHD FUNDED']]
# y = df['Valuation_y']

# # Fit the model
# model = LinearRegression()
# model.fit(X, y)
# # #---

# print("Coeffecient", model.coef_[0])
# print("Intercept", model.intercept_)

# yPred = model.predict(X)
# error = mean_squared_error(y, yPred)
# print("Error", error)

# # Evaluating the model

# r_squared = model.score(X, y)
# print('R-squared:', r_squared)

# X_with_const = sm.add_constant(X)
# model_sm = sm.OLS(y, X_with_const).fit()
# print(model_sm.summary())

# # Assumptions Check

# residuals = y - model.predict(X)
# plt.hist(residuals, bins=20)
# plt.title('Residuals Distribution')
# plt.show()

# # Scatter plot and regression line
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.xlabel('Valuations for Buildings')
# plt.ylabel('Funding for Affordable Housing Project')
# plt.title('Simple Linear Regression')
# plt.show()

## Q10

# X = df[['TDC', 'TECB', 'PROJECT TOTAL UNITS']]
# y = df['LAHD FUNDED']

# # X = df.drop(columns=['Satisfaction_Score'])
# # X = pd.get_dummies(X, drop_first=True)
# # y = df['Satisfaction_Score']

# print(df['TECB'].describe())
# skewness3 = df['TECB'].skew()
# kurtosis3 = df['TECB'].kurtosis()
# print(f'Skewness: {skewness3}')
# print(f'Kurtosis: {kurtosis3}')


# X_with_const = sm.add_constant(X)
# model_sm = sm.OLS(y, X_with_const).fit()
# residuals = model_sm.resid
# print(model_sm.summary())

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# #Confidence Intervals

# # Display confidence intervals
# print("Confidence Intervals:\n", model_sm.conf_int())

# # Predict Satisfaction Scores with significant predictors
# model_sig = LinearRegression()
# model_sig.fit(X_train, y_train)
# predictions = model_sig.predict(X_test)
# print("Predictions:", predictions)

# # Fit your model (assuming it's already been fitted)
# y_pred = model_sig.predict(df[['TDC', 'TECB', 'PROJECT TOTAL UNITS']])  # Predicted values

# # Actual values from the dependent variable in your dataset
# y_actual = df['LAHD FUNDED']

# # Calculate Mean Squared Error (MSE)
# mse = mean_squared_error(y_actual, y_pred) # CALCULATES THE AVERAGE DIFFERENCE BETWEEN THE ACTUAL VALUES AND THE PREDICTED VALUES SQUARED
# rmse = np.sqrt(mse)
# print("Mean Squared Error:", mse)
# print("Root Mean Squared Error:", rmse)

# vif_data = pd.DataFrame()
# vif_data['Feature'] = X.columns
# vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
# print("Variance Inflation Factor (VIF):\n", vif_data)

# # Perform Breusch-Pagan test
# bp_test = het_breuschpagan(residuals, X_with_const)

# # Unpack the test results
# bp_test_stat = bp_test[0]  # Lagrange Multiplier statistic
# bp_test_p_value = bp_test[1]  # p-value
# bp_test_f_stat = bp_test[2]  # f-statistic
# bp_test_f_p_value = bp_test[3]  # f p-value

# # Print the results
# print("Breusch-Pagan Test Results:")
# print(f"Lagrange Multiplier Statistic: {bp_test_stat}")
# print(f"P-value (LM Test): {bp_test_p_value}")
# print(f"F-statistic: {bp_test_f_stat}")
# print(f"P-value (F Test): {bp_test_f_p_value}")

# plt.scatter(y_test, predictions, alpha=0.5)
# plt.title('Actual vs Predicted')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.show()