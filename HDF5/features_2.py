import h5py
import numpy as np 
import pandas as pd
from scipy.stats import skew, kurtosis 
from sklearn.preprocessing import MinMaxScaler, StandardScaler 

def extract_features(segment): 
    max_val = np.max(segment)
    min_val = np.min(segment)
    ptp_val = np.ptp(segment)  # peak-to-peak (range) 
    mean_val = np.mean(segment)
    median_val = np.median(segment)
    var_val = np.var(segment)
    skew_val = skew(segment)
    kurt_val = kurtosis(segment) 
    rms_val = np.sqrt(np.mean(np.square(segment))) #rms 
    zero_val = np.sum(np.diff(np.sign(segment)) != 0) / len(segment)  # zero crossing rate 

    return {
        'max': max_val,
        'min': min_val,
        'ptp': ptp_val,
        'mean': mean_val,
        'median': median_val, 
        'var': var_val, 
        'skew': skew_val,
        'kurt': kurt_val,
        'rms': rms_val,
        'zero': zero_val
    }

with h5py.File('dataset.h5', 'r') as hdf:
<<<<<<< HEAD
    train_set = hdf['dataset/Train/data'][:]
    test_set = hdf['dataset/Test/data'][:]

df_train = pd.DataFrame(train_set)
df_test = pd.DataFrame(test_set)
=======
    dataset = hdf['dataset']
    group_train = dataset['Train']
    group_test = dataset['Test']

    features_train = []
    features_test = []
>>>>>>> 453b2c807723d72b19b7aed01ac314271b773a20

    for dataset_name in group_train.keys():
        segment = group_train[dataset_name][:]
        features_train.append(extract_features(segment))

    for dataset_name in group_test.keys():
        segment = group_test[dataset_name][:]
        features_test.append(extract_features(segment))

    df_features_train = pd.DataFrame(features_train)
    df_features_test = pd.DataFrame(features_test)

    df_features_train.to_csv('train_features.csv', index=False)
    df_features_test.to_csv('test_features.csv', index=False)
