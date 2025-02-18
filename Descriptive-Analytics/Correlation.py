import numpy as np
import pandas as pd

# # Load data
housing_df = pd.read_csv('Descriptive-Analytics\WestRoxbury.csv') # importing the csv file

# #Renaming Columns
housing_df.columns = [s.strip().replace(' ', '_') for s in housing_df.columns] # all columns

# # Descriptive statistics
# print(housing_df.describe()) # show summary statistics for each column


df = pd.DataFrame(housing_df)
# print(df)

# # #Finding Correlation
correlation_matrix = df.corr()
print(correlation_matrix)

# # Visualize the finding
import seaborn as sn
import matplotlib.pyplot as plt


sn.heatmap(correlation_matrix, annot=True)
plt.show()
