import pandas as pd
import numpy as np
import h5py
from sklearn.model_selection import train_test_split

df = pd.read_csv('arjun_data.csv')
# Split the dataframe into segments of 250 rows
segments = [df.iloc[i:i + 250] for i in range(0, len(df), 250)]

print(segments)
