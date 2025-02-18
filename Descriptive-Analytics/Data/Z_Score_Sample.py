import pandas as pd
import numpy as np
from scipy import stats

# # Example dataset
data = {'Age': [23, 25, 30, 21, 19, 29, 32, 34, 200, 22]}  # 200 is an outlier
df = pd.DataFrame(data)

# # Calculate Z-scores
df['Z_score'] = stats.zscore(df['Age'])

# # Set the threshold for outliers (typically Z > 3 or Z < -3)
threshold = 3

# # Detect outliers
outliers = df[np.abs(df['Z_score']) > threshold]

print("\nZ-scores and detected outliers:")
print(df)
print("\nDetected Outliers:")
print(outliers)