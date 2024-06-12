import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Extract relevant columns for box plots
columns_to_plot = ['Voltage (V)', 'Circuit 1 (V)', 'Circuit 2 (V)', 'Circuit 3 (V)']

# Create box plots for each column, differentiated by supplier
df.boxplot(column=columns_to_plot, by='Supplier', vert=True, patch_artist=True, medianprops={'color':'black'})
plt.title('Box Plots for Voltage and Circuits by Supplier')
plt.ylabel('Voltage (V)')
plt.suptitle('')
plt.show()
