import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# # Load data
Golf_df = pd.read_csv('Descriptive-Analytics\Golf_Stats_2016.csv') # importing the csv file

# #Renaming Columns
Golf_df.columns = [s.strip().replace(' ', '_') for s in Golf_df.columns] # all columns


# # Descriptive statistics
# print(Golf_df.describe()) # show summary statistics for each column

df = pd.DataFrame(Golf_df)
# print(df)
df_mn = df.fillna(df.mean(numeric_only=True))
# print(df_mn)

# #Finding Correlation
correlation_matrix = df_mn.corr()
covariance_matrix = df_mn.cov()
print(correlation_matrix)
print(covariance_matrix)

# sn.heatmap(correlation_matrix, annot=True)
# plt.show()