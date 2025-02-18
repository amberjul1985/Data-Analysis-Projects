import pandas as pd  # importing pandas library
df = pd.read_csv('Descriptive-Analytics\Sample.csv') # here we are importing the csv file
#print(df.head()) # print out the first 5 lines of sample file

data= df['Salary'] # read an specific column from the dataframe
#print(data.head())

# Calculate descriptive statistics
#mean = data.mean()
#median = data.median()
#maximum = data.max()
#minimum = data.min()
#variance = data.var()
#std_dev = data.std()
#skewness = data.skew()
#kurtosis = data.kurtosis()

# Display the results
#print(f'Mean: {mean}')
#print(f'Median: {median}')
#print(f'Maximum: {maximum}')
#print(f'Minimum: {minimum}')
#print(f'Variance: {variance}')
#print(f'Standard Deviation: {std_dev}')
#print(f'Skewness: {skewness}')
#print(f'Kurtosis: {kurtosis}')

# Using describe function
#summary = data.describe()
#print(summary)

# Percentiles (25th, 50th, 75th percentiles)
#percentile_25 = data.quantile(0.25)
#percentile_50 = data.quantile(0.50)  # Same as median
#percentile_75 = data.quantile(0.75)
#percentile_1 = data.quantile(0.1)  # Same as median
#percentile_99 = data.quantile(0.99)

#print(f'25th Percentile: {percentile_25}')
#print(f'50th Percentile (Median): {percentile_50}')
#print(f'75th Percentile: {percentile_75}')
#print(f'1st Percentile (Median): {percentile_1}')
#print(f'99th Percentile: {percentile_99}')

# Mode using Pandas Library
#mode_value = data.mode()

#print(f"The mode is: {mode_value.values}")

# Mode using Statistics Library
#import statistics as stat
# Calculate the mode
#mode_value = stat.mode(data)

#print(f"The mode is: {mode_value}") #mode is 1 std from (above) the mean, majority of salaries can 