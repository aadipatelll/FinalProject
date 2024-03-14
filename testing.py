import csv
import random

# Generate random data
data = [[random.choice([0, 1]) for _ in range(10)] for _ in range(10)]

# Write data to CSV file
with open('random_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)
