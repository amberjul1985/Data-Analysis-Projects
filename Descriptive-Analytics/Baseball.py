import numpy as np
import pandas as pd

# # Load data
Baseball_df = pd.read_csv('Descriptive-Analytics\Baseball_Salaries_2016.csv') # importing the csv file

# #Renaming Columns
Baseball_df.columns = [s.strip().replace(' ', '_') for s in Baseball_df.columns] # all columns


# # Descriptive statistics
# print(Baseball_df.describe()) # show summary statistics for each column

df = pd.DataFrame(Baseball_df)
# print(df)
df_mn = df.fillna(df.mean(numeric_only=True))
# print(df_mn)

# df_mn_encoded = pd.get_dummies(df_mn, drop_first=True)
#Have to transform the categorical data into numerical data

# #Finding Correlation
correlation_matrix = df_mn.corr()
# print(correlation_matrix)

# # # Visualize the finding
import seaborn as sn
import matplotlib.pyplot as plt

sn.heatmap(correlation_matrix, annot=True)
plt.show()