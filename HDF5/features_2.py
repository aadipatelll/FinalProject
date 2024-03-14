import h5py
import numpy as np 
import pandas as pd
from scipy.stats import skew, kurtosis 
from sklearn.preprocessing import MinMaxScaler, StandardScaler 


filename = "dataset.h5"


def extract_features(segment): 
    features = [] 
    features.append(np.max(segment)) 
    features.append(np.min(segment)) 
    features.append(np.ptp(segment))  # peak-to-peak (range) 
    features.append(np.mean(segment)) 
    features.append(np.median(segment)) 
    features.append(np.var(segment)) 
    features.append(skew(segment)) 
    features.append(kurtosis(segment)) 
    features.append(np.sqrt(np.mean(np.square(segment)))) #rms 
    features.append(np.sum(np.diff(np.sign(segment)) != 0) / len(segment))  # zero crossing rate 

    return features 

try:
    with h5py.File('dataset.h5', 'r') as hdf:
        # Read datasets
        train_set = hdf['dataset/Train'][:]
        test_set = hdf['dataset/Test'][:]

    # Convert the numpy arrays to DataFrames
    df_train = pd.DataFrame(train_set)
    df_test = pd.DataFrame(test_set)

    # Placeholder for features extracted from segments
    features_train = []
    features_test = []

    # Process segments for train_set
    for start_row in range(0, df_train.shape[0], 250):
        segment = df_train.iloc[start_row:start_row+250]
        features_train.append(extract_features(segment))

    # Process segments for test_set 
    for start_row in range(0, df_test.shape[0], 250):
        segment = df_test.iloc[start_row:start_row+250]
        features_test.append(extract_features(segment))

    # Convert the lists of features into DataFrame
    df_features_train = pd.DataFrame(features_train)
    df_features_test = pd.DataFrame(features_test)

    # Example: Save the features to CSV files
    df_features_train.to_csv('train_features.csv', index=False)
    df_features_test.to_csv('test_features.csv', index=False)

except Exception as e :
    print("Dang")

