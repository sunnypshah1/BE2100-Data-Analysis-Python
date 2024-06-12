import csv
from collections import defaultdict
import statistics
import math
from tabulate import tabulate

# Initialize a default dictionary to hold supplier data
supplier_data = defaultdict(list)

# Open the CSV file and read the data
with open('data2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        supplier, voltage = row[0], float(row[1])
        supplier_data[supplier].append(voltage)

# Prepare the data for the table
table_data = []
for supplier, voltages in supplier_data.items():
    count = len(voltages)
    reject_limit = 4
    rejects = sum(1 for v in voltages if v > reject_limit)
    ftq_sample = round((count - rejects) / count, 2)
    avg = round(statistics.mean(voltages), 2)
    stdev = round(statistics.stdev(voltages), 2)
    z_score = round((reject_limit - avg) / stdev, 2)
    estimated_population_ftq = round(ftq_sample * (1 + math.erf(z_score / math.sqrt(2))) / 2, 2)

    table_data.append([
        supplier,
        count,
        reject_limit,
        rejects,
        f'{ftq_sample * 100:.2f}%',
        avg,
        stdev,
        z_score,
        estimated_population_ftq
    ])

# Define the table headers
headers = [
    'Supplier',
    'Count',
    'Reject Limit',
    'Number of Rejects',
    'FTQ of Sample (percent)',
    'Sample Average',
    'Sample Standard Deviation',
    'Z Score',
    'Estimated Population FTQ'
]

# Print the table
print(tabulate(table_data, headers=headers, tablefmt='grid'))
