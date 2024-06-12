import pandas as pd
import statistics as stats

# Read the CSV file
df = pd.read_csv('data.csv')

# Select relevant columns
columns_of_interest = ['Voltage (V)', 'Circuit 1 (V)', 'Circuit 2 (V)', 'Circuit 3 (V)']

# Create an empty list to store DataFrames
dfs = []

# Iterate through each column
for column in columns_of_interest:
    # Iterate through each supplier
    for supplier in df['Supplier'].unique():
        # Filter data for the specific supplier and column
        subset = df[(df['Supplier'] == supplier)][column]
        
        # Calculate summary statistics and round values to 2 decimal places
        n = subset.count()
        mean = round(subset.mean(), 2)
        stdev = round(subset.std(), 2)
        variance = round(subset.var(), 2)
        minimum = round(subset.min(), 2)
        q1 = round(subset.quantile(0.25), 2)
        median = round(subset.median(), 2)
        q3 = round(subset.quantile(0.75), 2)
        maximum = round(subset.max(), 2)
        data_range = round(maximum - minimum, 2)
        iqr = round(q3 - q1, 2)
        
        # Calculate mode and n_mode only if there are modes
        mode = stats.multimode(subset)
        n_mode = len(mode)
        
        # Create a temporary DataFrame
        temp_df = pd.DataFrame({'Variable': [column],
                                'Supplier': [supplier],
                                'n': [n],
                                'mean': [mean],
                                'stdev': [stdev],
                                'variance': [variance],
                                'min': [minimum],
                                'q1': [q1],
                                'median': [median],
                                'q3': [q3],
                                'max': [maximum],
                                'range': [data_range],
                                'iqr': [iqr],
                                'mode': [mode if n_mode > 0 else None],
                                'n for mode': [n_mode]})
        
        # Append the temporary DataFrame to the list
        dfs.append(temp_df)

# Concatenate the list of DataFrames
pd.set_option('display.max_rows', None)
summary_df = pd.concat(dfs, ignore_index=True)

# Display the summary DataFrame
print(summary_df)
summary_df.to_csv('summary_stats.csv', index=False)
