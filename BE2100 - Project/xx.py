import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
data = """
Supplier,Voltage (V),Circuit 1 (V),Circuit 2 (V),Circuit 3 (V)
Supplier 1,3.59,1.03,6.78,8.01
Supplier 1,3.41,0.96,2.09,3.27
Supplier 1,4.96,1.00,6.93,5.76
Supplier 1,3.44,1.01,6.91,6.50
Supplier 1,2.50,1.01,3.22,6.66
Supplier 1,3.49,1.01,6.81,6.79
Supplier 1,3.02,1.00,3.02,6.07
Supplier 1,3.71,0.99,6.94,5.09
Supplier 1,3.29,1.02,7.21,7.80
Supplier 1,4.01,0.99,6.13,5.33
Supplier 1,4.11,1.01,6.69,6.51
Supplier 1,2.47,1.02,3.51,7.53
Supplier 1,4.91,0.97,5.67,3.82
Supplier 1,3.01,1.02,3.48,7.44
Supplier 1,3.06,1.05,6.77,9.55
Supplier 1,4.33,0.99,6.20,4.97
Supplier 1,3.66,1.01,7.57,6.95
Supplier 1,4.10,0.99,6.41,5.05
Supplier 1,4.05,1.00,6.34,5.68
Supplier 1,1.74,1.03,3.74,8.22
Supplier 1,3.59,1.01,7.33,7.04
Supplier 1,3.09,0.99,2.85,5.56
Supplier 1,4.09,1.01,6.69,7.03
Supplier 1,2.72,0.98,2.61,4.84
Supplier 1,4.90,0.97,5.90,3.50
Supplier 2,2.21,1.01,3.35,7.04
Supplier 2,4.22,0.97,5.28,4.01
Supplier 2,3.21,1.01,6.02,7.07
Supplier 2,4.18,0.97,2.16,3.49
Supplier 2,3.00,1.01,3.23,6.70
Supplier 2,3.20,1.01,5.58,6.89
Supplier 2,3.13,1.01,5.94,6.58
Supplier 2,2.57,1.00,2.95,5.84
Supplier 2,3.65,0.99,5.52,5.48
Supplier 2,3.56,1.01,7.04,6.59
Supplier 2,3.67,0.98,2.44,4.32
Supplier 2,2.15,1.01,3.24,6.73
Supplier 2,1.94,1.00,2.90,5.69
Supplier 2,3.11,1.00,4.37,6.10
Supplier 2,3.11,0.99,2.85,5.56
Supplier 2,3.70,0.95,1.79,2.37
Supplier 2,1.99,1.03,3.76,8.27
Supplier 2,3.48,0.97,2.25,3.75
Supplier 2,2.82,1.04,7.78,9.16
Supplier 2,2.81,1.01,3.23,6.70
Supplier 2,2.54,1.00,3.04,6.12
Supplier 2,2.16,0.91,0.84,5.69
Supplier 2,2.91,1.00,3.04,6.11
Supplier 2,2.81,1.00,3.11,6.34
Supplier 2,3.43,0.97,2.19,3.58
"""

df = pd.read_csv(pd.compat.StringIO(data))

# Simple Linear Regression (using Voltage and Circuit 1)
X_simple = df[['Voltage']]
y_simple = df['Circuit1']

X_simple_train, X_simple_test, y_simple_train, y_simple_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)

# Create a linear regression model
simple_model = LinearRegression()

# Train the model
simple_model.fit(X_simple_train, y_simple_train)

# Make predictions
y_simple_pred = simple_model.predict(X_simple_test)

# Evaluate the model
mse_simple = mean_squared_error(y_simple_test, y_simple_pred)
r2_simple = r2_score(y_simple_test, y_simple_pred)

# Print results
print("Simple Linear Regression:")
print(f'Mean Squared Error: {mse_simple}')
print(f'R-squared: {r2_simple}')

# Plot the regression line
plt.scatter(X_simple_test, y_simple_test, color='black')
plt.plot(X_simple_test, y_simple_pred, color='blue', linewidth=3)
plt.xlabel('Voltage')
plt.ylabel('Circuit 1')
plt.title('Simple Linear Regression')
plt.show()

# Multiple Linear Regression (using Voltage, Circuit 2, and Circuit 3)
X_multiple = df[['Voltage', 'Circuit2', 'Circuit3']]
y_multiple = df['Circuit1']

X_multiple_train, X_multiple_test, y_multiple_train, y_multiple_test = train_test_split(X_multiple, y_multiple, test_size=0.2, random_state=42)

# Create a linear regression model
multiple_model = LinearRegression()

# Train the model
multiple_model.fit(X_multiple_train, y_multiple_train)

# Make predictions
y_multiple_pred = multiple_model.predict(X_multiple_test)

# Evaluate the model
mse_multiple = mean_squared_error(y_multiple_test, y_multiple_pred)
r2_multiple = r2_score(y_multiple_test, y_multiple_pred)

# Print results
print("\nMultiple Linear Regression:")
print(f'Mean Squared Error: {mse_multiple}')
print(f'R-squared: {r2_multiple}')
