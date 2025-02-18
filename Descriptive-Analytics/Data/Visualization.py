import pandas as pd

##------------------------------------------------------##
# Boston housing data
housing_df = pd.read_csv('Descriptive-Analytics\BostonHousing.csv')
housing_df = housing_df.rename(columns={'CAT. MEDV': 'CAT_MEDV'})

print(housing_df.describe())
# print(housing_df.dtypes)

##------------------------------------------------------##
# #Bar chart Using matplotlib:
# #Pip Install Matplotlib # If needed
import matplotlib.pyplot as plt

# # compute mean MEDV per CHAS = (0, 1)
# dataForPlot = housing_df.groupby('CHAS').mean().MEDV
# fig, ax = plt.subplots()
# ax.bar(dataForPlot.index, dataForPlot, color=['C2', 'C3'])
# ax.set_xlabel('CHAS')
# ax.set_ylabel('Avg.MEDV')
# plt.show()

# print(dataForPlot)

##------------------------------------------------------##
#Scatterplot Using matplotlib:
# Set the color of points and draw as open circles.
# import matplotlib.pyplot as plt
# plt.scatter(housing_df.LSTAT, housing_df.MEDV, color=['C2', 'C4'], facecolor='black')
# plt.xlabel('LSTAT')
# plt.ylabel('MEDV')
# plt.show()

# # Code for Scatterplot with Color Added
# # Color the points by the value of CAT.MEDV
# import matplotlib.pyplot as plt
# housing_df.plot.scatter(x='LSTAT', y='NOX', c=['C0' if c == 1 else 'C1' for c in housing_df.CAT_MEDV])
# plt.show()

# # Code for Scatterplot with Color Added
# # Plot first the data points for CAT.MEDV of 0 and then of 1
# # Setting color to 'none' gives open circles
# import matplotlib.pyplot as plt
# _, ax = plt.subplots()
# for catValue, color in (0, 'C1'), (1, 'C0'):
#     subset_df = housing_df[housing_df.CAT_MEDV == catValue]
#     ax.scatter(subset_df.LSTAT, subset_df.NOX, color='none', edgecolor=color)
# ax.set_xlabel('LSTAT')
# ax.set_ylabel('NOX')
# ax.legend(["CAT.MEDV 0", "CAT.MEDV 1"])
# plt.show()

## Matrix Scaterplot 1
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = housing_df[['CRIM', 'INDUS', 'LSTAT', 'MEDV']]

# axes = pd.plotting.scatter_matrix(df, alpha=0.5, figsize=(6, 6), diagonal='kde')
# corr = df.corr().values
# corr = df.to_numpy()
# for i, j in zip(*plt.np.triu_indices_from(axes, k=1)):
#     axes[i, j].annotate('%.3f' %corr[i,j], (0.8, 0.8), 
#                         xycoords='axes fraction', ha='center', va='center')
# plt.show()

# #Matrix Scaterplot 2
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = housing_df[['CRIM', 'INDUS', 'LSTAT', 'MEDV']]
# pd.plotting.scatter_matrix(df, alpha=0.5, figsize=(6, 6), diagonal='kde')
# plt.show()

# #Matrix Scaterplot 3

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = housing_df[['CRIM', 'INDUS', 'LSTAT', 'MEDV']]
# pd.plotting.scatter_matrix(df)
# plt.show()

# # scatter plot: regular and log scale
# import matplotlib.pyplot as plt

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 4))
# # regular scale
# housing_df.plot.scatter(x='CRIM', y='MEDV', ax=axes[0])
# # log scale
# ax = housing_df.plot.scatter(x='CRIM', y='MEDV', logx=True, logy=True, 
#      ax=axes[1])
# ax.set_yticks([5, 10, 20, 50])
# ax.set_yticklabels([5, 10, 20, 50])
# plt.tight_layout()
# plt.show()

##------------------------------------------------------##
# # histogram of MEDV
# import matplotlib.pyplot as plt

# ax = housing_df.TAX.hist()
# ax.set_xlabel('TAX')
# ax.set_ylabel('count')
# plt.show()

##------------------------------------------------------##
#boxplot
# import matplotlib.pyplot as plt

# ax = housing_df.boxplot(column='MEDV', by='CHAS')
# ax.set_ylabel('MEDV')
# plt.suptitle('')  # Suppress the titles
# plt.title('boxplot')
# plt.show()

# # #manual boxplot using IQR
# import matplotlib.pyplot as plt

# # Calculate IQR and identify outliers
# Q1 = housing_df['MEDV'].quantile(0.25)
# Q3 = housing_df['MEDV'].quantile(0.75)
# IQR = Q3 - Q1

# # # Outliers are values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR
# outliers = housing_df[(housing_df['MEDV'] < (Q1 - 1.5 * IQR)) | (housing_df['MEDV'] > (Q3 + 1.5 * IQR))]

# # # Create the boxplot
# ax = housing_df.boxplot(column='MEDV', by='CHAS')
# ax.set_ylabel('MEDV')

# # Label the outliers
# for i in outliers.index:
#     ax.text(x=1, y=housing_df['MEDV'].loc[i], s=i, color='red')  # 's=i' labels with index

# # Suppress the titles
# plt.suptitle('')
# plt.title('Boxplot with Outliers Labeled')
# plt.show()


# # boxplot: regular and log scale
# import matplotlib.pyplot as plt

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
# # regular scale
# ax = housing_df.boxplot(column='CRIM', by='CAT_MEDV', ax=axes[0])
# ax.set_xlabel('CAT.MEDV'); ax.set_ylabel('CRIM')
# # log scale
# ax = housing_df.boxplot(column='CRIM', by='CAT_MEDV', ax=axes[1])
# ax.set_xlabel('CAT.MEDV'); ax.set_ylabel('CRIM'); ax.set_yscale('log')
# # suppress the title
# axes[0].get_figure().suptitle(''); plt.tight_layout()
# plt.show()

##------------------------------------------------------##
# #boxplots to detect outliers

# import pandas as pd
# import numpy as np

# # Create a sample dataset with some outliers
# data = {'Sample_Variable': [10, 12, 14, 15, 16, 18, 20, 25, 30, 35, 40, 100]  # 100 is an outlier
# }
# # Create a DataFrame
# df = pd.DataFrame(data)
# # Display the DataFrame
# print(df)

# import matplotlib.pyplot as plt

# # # Create a box plot for the 'Sample_Variable' column
# plt.boxplot(df['Sample_Variable'])
# # Add labels and title
# plt.title('Box Plot for Sample_Variable')
# plt.ylabel('Values')
# # Show the plot
# plt.show()

# ##------------------------------------------------------##
# #Heatmap
# # simple heatmap of correlations (without values)
# corr = housing_df.corr()
# print(corr)

# import numpy as np
# np.random.seed(0)

# import seaborn as sns
# sns.set_theme()

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
# plt.show()

# # Change to divergent scale and fix the range
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, vmin=-1, vmax=1, cmap="RdBu")
# plt.show()

# # Include information about values (example demonstrates how to control the size of the plot)
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# fig.set_size_inches(11, 7)
# sns.heatmap(corr, annot=True, fmt=".1f", cmap="RdBu", center=0, ax=ax)
# plt.show()



# ##------------------------------------------------------##
# #Lineplot Using matplotlib:
# #1
# # Load, convert Amtrak data for time series analysis
Amtrak_df = pd.read_csv('Descriptive-Analytics\Amtrak.csv')
Amtrak_df['Date'] = pd.to_datetime(Amtrak_df.Month,  format='%d/%m/%Y')
ridership_ts = pd.Series(Amtrak_df.Ridership.values, index=Amtrak_df.Date)

# print(Amtrak_df)

# import matplotlib.pyplot as plt
# plt.plot(ridership_ts.index, ridership_ts)
# plt.xlabel('Year')  # set x-axis label
# plt.ylabel('Ridership (in 000s)')  # set y-axis label
# plt.show()

# #2
# import matplotlib.pyplot as plt
# import numpy as np

# #fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7))

# Amtrak_df = pd.read_csv('Amtrak.csv')
# Amtrak_df['Month'] = pd.to_datetime(Amtrak_df.Month, 
#    format='%d/%m/%Y')
# Amtrak_df.set_index('Month', inplace=True)

# # fit quadratic curve and display 
# quadraticFit = np.poly1d(np.polyfit(range(len(Amtrak_df)), Amtrak_df.Ridership, 2))
# Amtrak_fit = pd.DataFrame({'fit': [quadraticFit(t) for t in range(len(Amtrak_df))]})
# Amtrak_fit.index = Amtrak_df.index

# ax = Amtrak_df.plot(ylim=[1300, 2300], legend=False)
# Amtrak_fit.plot(ax=ax)
# ax.set_xlabel('Year'); ax.set_ylabel('Ridership (in 000s)')  # set x and y-axis label
# plt.show()

##------------------------------------------------------##
#scatterplot with lables

# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the data
# utilities_df = pd.read_csv('Utilities.csv')

# # Create a scatter plot using matplotlib
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.scatter(utilities_df['Sales'], utilities_df['Fuel_Cost'])

# # Add labels to each point
# for i, row in utilities_df.iterrows():
#     ax.text(row['Sales'], row['Fuel_Cost'], row['Company'], 
#             rotation=20, horizontalalignment='left',
#             verticalalignment='bottom', fontsize=8)

# # Set labels for x and y axes
# ax.set_xlabel('Sales')
# ax.set_ylabel('Fuel Cost')

# # Show the plot
# plt.show()

# ##------------------------------------------------------##
# #Network Graph
# #pip install networkx on terminal
# #Network Graph for Swarovski Beads

# import matplotlib.pyplot as plt
# import pandas as pd
# import networkx as nx

# ebay_df = pd.read_csv('eBayNetwork.csv')

# G = nx.from_pandas_edgelist(ebay_df, source='Seller', target='Bidder')

# isBidder = [n in set(ebay_df.Bidder) for n in G.nodes()]
# pos = nx.spring_layout(G, k=0.13, iterations=60, scale=0.5)
# plt.figure(figsize=(10,10))
# nx.draw_networkx(G, pos=pos, with_labels=False,
#      edge_color='lightgray',
#      node_color=['gray' if bidder else 'black' for bidder in isBidder],
#      node_size=[50 if bidder else 200 for bidder in isBidder])
# plt.axis('off')
# plt.show()

##------------------------------------------------------##
