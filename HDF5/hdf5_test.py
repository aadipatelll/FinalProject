import pandas as pd
import numpy as np
import h5py
from sklearn.model_selection import train_test_split

def process_for_AI(df):
    # Split the dataframe into segments of 250 rows
    segments = [df.iloc[i:i + 250] for i in range(0, len(df), 250)]
    # Shuffle the segments
    np.random.shuffle(segments)
    return segments

# Read the CSV file and store them
# ds is just short form for dataset
ds_aadi = pd.read_csv('aadi_data.csv')
ds_trevor = pd.read_csv('trevor_data.csv')
ds_arjun = pd.read_csv('arjun_data.csv')

# Process each member's CSV file into segments
segments_aadi = process_for_AI(ds_aadi)
segments_trevor = process_for_AI(ds_trevor)
segments_arjun = process_for_AI(ds_arjun)

# Concatenate all the shuffled segments from all members into a single list
all_segments = segments_aadi + segments_trevor + segments_arjun

# Shuffle the segments again to ensure random distribution of all members' segments
np.random.shuffle(all_segments)

# Concatenate all segments into a single DataFrame for the train and test split
all_data_df = pd.concat(all_segments)

# Split the data into training and testing sets (90% train, 10% test)
train_set, test_set = train_test_split(all_data_df, test_size=0.1)

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

