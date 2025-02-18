import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


# # Load data
golf_df = pd.read_csv('Descriptive-Analytics\Golf_Stats_2016.csv') # importing the csv file

# # Renaming Columns
# golf_df.columns = [s.strip().replace(' ', '_') for s in golf_df.columns] # all columns

# # Descriptive statistics
# print(golf_df.describe()) # show summary statistics for each column

df = pd.DataFrame(golf_df)
# print(df)
df_mn = df.fillna(df.median(numeric_only=True))
# print(df_mn)

# # # #Finding Correlation
correlation_matrix = df_mn.corr()
print(correlation_matrix)

sn.heatmap(correlation_matrix, annot=True)
plt.show()
