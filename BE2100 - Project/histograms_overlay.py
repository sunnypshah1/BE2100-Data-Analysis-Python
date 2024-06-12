import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Extract relevant columns
columns_of_interest = ['Voltage (V)', 'Circuit 1 (V)', 'Circuit 2 (V)', 'Circuit 3 (V)']

# Unique suppliers in the dataset
suppliers = df['Supplier'].unique()

# Plot histograms for each column, overlaying two suppliers
for column in columns_of_interest:
    plt.figure(figsize=(8, 6))
    
    for supplier in suppliers:
        supplier_data = df[df['Supplier'] == supplier][column]
        plt.hist(supplier_data, bins=20, alpha=0.5, label=supplier)

    plt.title(f'Histogram for {column} (Overlayed by Supplier)')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
