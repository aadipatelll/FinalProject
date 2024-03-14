import pandas as pd
import numpy as np
import h5py
from sklearn.model_selection import train_test_split

def process_for_AI(df):
    # Split the dataframe into segments of 250 rows
    segments = [df.iloc[i:i + 250] for i in range(0, len(df), 250)]
    # Shuffle the segments
    np.random.shuffle(segments)
    # Concatenate the segments back into a single dataframe
    return pd.concat(segments, ignore_index=True)

# Read the CSV file and store them
# ds is just short form for dataset
ds_aadi = pd.read_csv('./aadi_data.csv')
ds_trevor = pd.read_csv('./trevor_data.csv')
ds_arjun = pd.read_csv('./arjun_data.csv')

# Read each CSV file into a dataframe, segment and shuffle
ds_1 = process_for_AI(ds_aadi)
ds_2 = process_for_AI(ds_trevor)
ds_3 = process_for_AI(ds_arjun)

# Combine all the shuffled segments from all members
combined_ds = pd.concat([ds_1, ds_2, ds_3], ignore_index=True)

# Split the combined data into training and testing sets (90% train, 10% test)
train_set, test_set = train_test_split(combined_ds, test_size=0.1)

with h5py.File('dataset.h5', 'w') as hdf:
    # Create dataset group at the root level
    group_dataset = hdf.create_group('dataset')

    # Create subgroups for training and testing sets in dataset group
    group_train = group_dataset.create_group('Train')
    group_test = group_dataset.create_group('Test')
    
    # Create and store data for the training and testing sets inside their respective groups
    group_train.create_dataset('data', data=train_set.to_numpy())
    group_test.create_dataset('data', data=test_set.to_numpy())
    
    # Create groups for each member at the root level
    group_aadi = hdf.create_group('aadi_data')
    group_trevor = hdf.create_group('trevor_data')
    group_arjun = hdf.create_group('arjun_data')
    
    # Create and store data for each member's data sets inside their respective groups
    group_aadi.create_dataset('data', data=ds_aadi.to_numpy())
    group_trevor.create_dataset('data', data=ds_trevor.to_numpy())
    group_arjun.create_dataset('data', data=ds_arjun.to_numpy())

