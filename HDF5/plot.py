import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV File
df = pd.read_csv('arjun_data.csv')

# Plotting the Data
plt.figure(figsize=(10, 6))
plt.plot(df['Time (s)'], df['Linear Acceleration z (m/s^2)'], label='Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Linear Acceleration z (m/s²)')
plt.title('Acceleration Data Over Time')
plt.legend()
plt.grid(True)
plt.show()
