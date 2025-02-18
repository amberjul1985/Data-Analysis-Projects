import pandas as pd #installing pandas to work with data
df = pd.read_csv('Descriptive-Analytics\Student_Grades.csv') #creating a dataframe using student grade data from CSV file
print(df.head()) #produce first 5 rows of table (including all columns)
print(df.describe())

dfdr = (df.dropna())
print(dfdr.describe())

dfme = df.fillna(df.mean(numeric_only=True))
print(dfme.describe())

dfmd = df.fillna(df.median(numeric_only=True))
print(dfmd.describe())

dffi = df.ffill()
print(dffi.describe())

dfba = df.bfill()
print(dfba.describe())