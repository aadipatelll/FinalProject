import pandas as pd
import matplotlib.pyplot as plt

# Assuming the CSV file is named "data.csv" and is located in the same directory as this script.
# The first column is named "Time" and the second column is named "Acceleration".

# Step 1: Read the CSV File
# Replace 'data.csv' with the path to your CSV file
df = pd.read_csv('arjun_data.csv')

# Step 2: Data Preprocessing (if necessary)
# This step assumes the time data is in seconds and acceleration data is properly formatted.
# Convert the Time column to datetime if it's not already in that format
# This step might be unnecessary depending on your specific time format.
# df['Time'] = pd.to_datetime(df['Time'], unit='s')

# Step 3: Plotting the Data
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Acceleration'], label='Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Acceleration Data Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Note: Uncomment the function calls for execution outside of the PCI environment.
