#Simple Regression

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('Descriptive-Analytics/advertising.csv')
X = data[['TV']]
y = data['Sales']

# Fit the model
model = LinearRegression()
model.fit(X, y)
# #---

print("Coeffecient", model.coef_[0])
print("Intercept", model.intercept_)

yPred=model.predict(X)
error= mean_squared_error(y, yPred)
print("Error", error)

#Visualizing the Simple Regression Results

# Scatter plot and regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales Revenue')
plt.title('Simple Linear Regression')
plt.show()

# Evaluating the model

r_squared = model.score(X, y)
print('R-squared:', r_squared)

X_with_const = sm.add_constant(X)
model_sm = sm.OLS(y, X_with_const).fit()
print(model_sm.summary())

# Assumptions Check

residuals = y - model.predict(X)
plt.hist(residuals, bins=20)
plt.title('Residuals Distribution')
plt.show()


# # Multiple Linear Regression

# from sklearn.datasets import fetch_california_housing
# import pandas as pd

# housing = fetch_california_housing()
# X = pd.DataFrame(housing.data, columns=housing.feature_names)
# y = housing.target

# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# # Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # # Fit the model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # # Check the coeefficients
# coeffs = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
# # print(coeffs)

# # # Evaluating MLR

# from sklearn.metrics import mean_squared_error, r2_score

# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print('Mean Squared Error:', mse)
# print('R-squared:', r2)

# #VIF

# from statsmodels.stats.outliers_influence import variance_inflation_factor

# vif_data = pd.DataFrame()
# vif_data['Feature'] = X.columns
# vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
# print(vif_data)

# df=pd.read_csv('Descriptive-Analytics\CAH.csv')

# corM=df.corr()
# print(corM)

# Handling Categorical Variables

# X = pd.get_dummies(X, drop_first=True)

# #Residual Analysis

# residuals = y_test - y_pred
# plt.scatter(y_pred, residuals)
# plt.xlabel('Predicted')
# plt.ylabel('Residuals')
# plt.title('Residuals vs. Predicted')
# plt.show()

#MSE , RMSE
# from sklearn.metrics import mean_squared_error

# # Calculate Mean Squared Error
# mse = mean_squared_error(y_test, y_pred)

# # Calculate Root Mean Squared Error
# rmse = mse ** 0.5

# print("Mean Squared Error (MSE):", mse)
# print("Root Mean Squared Error (RMSE):", rmse)

# #MAE
# from sklearn.metrics import mean_absolute_error

# # Calculate Mean Absolute Error
# mae = mean_absolute_error(y_test, y_pred)

# print("Mean Absolute Error (MAE):", mae)

# #AIC, BIC
# import statsmodels.api as sm

# # Add a constant to the model (for intercept)
# X_test_with_const = sm.add_constant(X_test)

# # Fit the model using statsmodels
# model_stats = sm.OLS(y_test, X_test_with_const).fit()

# # Calculate AIC and BIC
# aic = model_stats.aic
# bic = model_stats.bic

# print("Akaike Information Criterion (AIC):", aic)
# print("Bayesian Information Criterion (BIC):", bic)

# # Backward Elimination

import statsmodels.api as sm

# Backward Elimination Function
def backward_elimination(X, y, threshold_out=0.05):
    included = list(X.columns)
    while True:
        # Fit the model with all currently included features
        X_with_const = sm.add_constant(X[included])
        model = sm.OLS(y, X_with_const).fit()
        
        # Get p-values of included features
        pvalues = model.pvalues.iloc[1:]  # Exclude intercept p-value
        worst_pval = pvalues.max()  # Find the highest p-value
        
        if worst_pval > threshold_out:
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            print(f"Dropping {worst_feature} with p-value {worst_pval}")
        else:
            break

    return included

# Perform backward elimination
selected_features_backward = backward_elimination(X, y)
print("Selected features (Backward Elimination):", selected_features_backward)


# # Forward Selection

# import statsmodels.api as sm
# import pandas as pd

# # Forward Selection Function
# def forward_selection(X, y, threshold_in=0.05):
#     included = []
#     while True:
#         excluded = list(set(X.columns) - set(included))
#         new_pval = pd.Series(index=excluded, dtype=float)
        
#         # Calculate p-value for each excluded variable
#         for new_column in excluded:
#             model = sm.OLS(y, sm.add_constant(X[included + [new_column]])).fit()
#             new_pval[new_column] = model.pvalues[new_column]
        
#         best_pval = new_pval.min()
#         if best_pval < threshold_in:
#             best_feature = new_pval.idxmin()
#             included.append(best_feature)
#             print(f"Adding {best_feature} with p-value {best_pval}")
#         else:
#             break

#     return included

# # Perform forward selection
# selected_features = forward_selection(X, y)
# print("Selected features:", selected_features)


# #Stepwise Selection

# import statsmodels.api as sm
# import pandas as pd

# # Stepwise Selection Function

# def stepwise_selection(X, y, threshold_in=0.05, threshold_out=0.05):
#     included = []
#     while True:
#         # Forward step
#         excluded = list(set(X.columns) - set(included))
#         new_pval = pd.Series(index=excluded, dtype=float)
        
#         # Calculate p-value for each excluded variable
#         for new_column in excluded:
#             model = sm.OLS(y, sm.add_constant(X[included + [new_column]])).fit()
#             new_pval[new_column] = model.pvalues[new_column]
        
#         best_pval = new_pval.min()
#         if best_pval < threshold_in:
#             best_feature = new_pval.idxmin()
#             included.append(best_feature)
#             print(f"Adding {best_feature} with p-value {best_pval}")

#         # Backward step
#         model = sm.OLS(y, sm.add_constant(X[included])).fit()
#         pvalues = model.pvalues.iloc[1:]  # Exclude intercept p-value
#         worst_pval = pvalues.max()
        
#         if worst_pval > threshold_out:
#             worst_feature = pvalues.idxmax()
#             included.remove(worst_feature)
#             print(f"Dropping {worst_feature} with p-value {worst_pval}")

#         # Stop when no more variables can be added or removed
#         if best_pval >= threshold_in and worst_pval <= threshold_out:
#             break

#     return included

# # Perform stepwise selection
# selected_features_stepwise = stepwise_selection(X, y)
# print("Selected features (Stepwise Selection):", selected_features_stepwise)

# #Lasso
# from sklearn.linear_model import LassoCV

# # Fit Lasso model with cross-validation
# lasso = LassoCV(cv=5)
# lasso.fit(X_train, y_train)

# # Identify selected features
# selected_features = X.columns[lasso.coef_ != 0]
# print("Selected features:", selected_features)

# # PCA

# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA

# # Standardize data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Apply PCA
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X_scaled)

# print("Explained variance ratio:", pca.explained_variance_ratio_)

# #Interpreting PCA Results

# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler

# # Standardize the data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Apply PCA
# pca = PCA()
# pca.fit(X_scaled)

# # Plot the explained variance ratio
# plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, marker='o')
# plt.title('Scree Plot')
# plt.xlabel('Principal Component')
# plt.ylabel('Explained Variance Ratio')
# plt.show()

# # Cumulative explained variance
# cumulative_variance = pca.explained_variance_ratio_.cumsum()
# plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
# plt.title('Cumulative Explained Variance')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.show()

# #When to Use PCA
# # Choosing the number of components based on explained variance threshold (e.g., 95%)
# pca = PCA(n_components=0.95)
# X_reduced = pca.fit_transform(X_scaled)

# print(f"Number of components selected to explain 95% variance: {pca.n_components_}")
# print("Reduced data shape:", X_reduced.shape)

# #Combinig PCA with Regression

# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# # Split the reduced dataset into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.2, random_state=0)

# # Fit a regression model on the PCA-reduced data
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predict and evaluate
# y_pred = model.predict(X_test)
# from sklearn.metrics import mean_squared_error, r2_score
# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R-squared:", r2_score(y_test, y_pred))

# #Case Study on PCA and Regression

# import pandas as pd
# from sklearn.decomposition import PCA
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

# # Load the wine quality dataset
# wine_data = pd.read_csv('winequality-red.csv', delimiter=';')
# X_wine = wine_data.drop(columns='quality')
# y_wine = wine_data['quality']

# # Standardize the data and apply PCA
# X_scaled = StandardScaler().fit_transform(X_wine)
# pca = PCA(n_components=0.95)
# X_reduced = pca.fit_transform(X_scaled)

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X_reduced, y_wine, test_size=0.2, random_state=0)

# # Train and evaluate the regression model
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# print("Wine Quality Prediction - MSE:", mean_squared_error(y_test, y_pred))
# print("Wine Quality Prediction - R-squared:", r2_score(y_test, y_pred))

# #Model Evaluation Comparison
# # Full model without PCA
# X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_wine, y_wine, test_size=0.2, random_state=0)
# model_full = LinearRegression()
# model_full.fit(X_train_full, y_train_full)
# y_pred_full = model_full.predict(X_test_full)

# # PCA-reduced model
# model_pca = LinearRegression()
# model_pca.fit(X_train, y_train)  # Using PCA-transformed data from Slide 57
# y_pred_pca = model_pca.predict(X_test)

# # Compare MSE and R-squared for both models
# print("Full Model - MSE:", mean_squared_error(y_test_full, y_pred_full))
# print("Full Model - R-squared:", r2_score(y_test_full, y_pred_full))
# print("PCA Model - MSE:", mean_squared_error(y_test, y_pred))
# print("PCA Model - R-squared:", r2_score(y_test, y_pred))
