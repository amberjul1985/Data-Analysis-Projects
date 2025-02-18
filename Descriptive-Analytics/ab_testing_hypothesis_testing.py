
# Import necessary libraries
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Generate synthetic dataset for A/B Testing
np.random.seed(42)
n_users = 10000  # Large dataset
groups = ['A', 'B']
conversions = [0, 1]

data = pd.DataFrame({
    'UserID': np.arange(1, n_users + 1),
    'Group': np.random.choice(groups, size=n_users, p=[0.5, 0.5]),
    'Conversion': np.random.choice(conversions, size=n_users, p=[0.8, 0.2]),
    'Time_On_Site': np.random.normal(loc=5, scale=2, size=n_users),
    'Pages_Visited': np.random.poisson(lam=3, size=n_users),
    'Purchase_Amount': np.random.normal(loc=50, scale=10, size=n_users)
})

# print(data.head)

# Independent T-Test
group_a = data[data['Group'] == 'A']['Purchase_Amount']
group_b = data[data['Group'] == 'B']['Purchase_Amount']
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f'T-Test Results: T-statistic: {t_stat}, P-value: {p_value}')

# F-Test (Levene's test for equal variances)
f_stat, f_p_value = stats.levene(group_a, group_b)
print(f'F-Test Results: F-statistic: {f_stat}, P-value: {f_p_value}')

# # # Chi-Squared Test
conversion_contingency = pd.crosstab(data['Group'], data['Conversion'])
chi2_stat, chi2_p_val, dof, expected = chi2_contingency(conversion_contingency)
print(f'Chi-Squared Test Results: Chi-squared stat: {chi2_stat}, P-value: {chi2_p_val}')

# # # Visualization - Boxplot for Purchase Amount
# sns.boxplot(data=[group_a, group_b], notch=True)
# plt.xticks([0, 1], ['Group A', 'Group B'])
# plt.title('Distribution of Purchase Amounts by Group')
# plt.show()

# # Visualization - Bar Chart for Conversion Rates
# conversion_rate_a = data[data['Group'] == 'A']['Conversion'].mean()
# conversion_rate_b = data[data['Group'] == 'B']['Conversion'].mean()
# plt.bar([0, 1], [conversion_rate_a, conversion_rate_b], tick_label=['Group A', 'Group B'])
# plt.title('Conversion Rates by Group')
# plt.ylabel('Conversion Rate')
# plt.show()

# # # Histogram for Time on Site
# plt.hist(data['Time_On_Site'], bins=20, color='skyblue')
# plt.title('Distribution of Time on Site')
# plt.xlabel('Time on Site (Minutes)')
# plt.ylabel('Frequency')
# plt.show()
