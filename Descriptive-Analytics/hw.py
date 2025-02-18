
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

golf_df = pd.read_csv('Descriptive-Analytics\BaseSal.csv') # importing the csv file
# print(golf_df)


df = pd.DataFrame(golf_df)
# print(df)
golf_df = golf_df.iloc[:, 2:]
# print(golf_df)
df_filled_bfill = golf_df.fillna(golf_df.bfill())
# print(df_filled_bfill)
# _____________________________________________________
#not needed
# #df_filled_bfill['Earnings'] = df_filled_bfill['Earnings'].round().astype(int)
# #print(df_filled_bfill['Earnings'].dtype)
# #df1=int(df_filled_bfill['Earnings'])
 # _____________________________________________________
# print("\nDataFrame after filling missing values with bfill:")
# print(df_filled_bfill)
# print(df_filled_bfill.dtypes)

# Finding Correlation

correlation_matrix = df_filled_bfill.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

correlation_matrix.to_csv('correlationMatrix.csv') #save it as csv file 
sn.heatmap(correlation_matrix, annot=True)
plt.show()


