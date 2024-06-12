import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Extract relevant columns
columns_of_interest = ['Voltage (V)', 'Circuit 1 (V)', 'Circuit 2 (V)', 'Circuit 3 (V)']

# Plot histograms for each column
for column in columns_of_interest:
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='blue', edgecolor='black')
    plt.title(f'Histogram for {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
