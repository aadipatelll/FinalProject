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

    df_train = pd.DataFrame(hdf['dataset/Train'][:])
    df_test = pd.DataFrame(hdf['dataset/Test'][:])

features_train = []
features_test = []

for start_row in range(0, df_train.shape[0], 250):
    segment = df_train.iloc[start_row:start_row+250]
    features_train.append(extract_features(segment))

for start_row in range(0, df_test.shape[0], 250):
    segment = df_test.iloc[start_row:start_row+250]
    features_test.append(extract_features(segment))

df_features_train = pd.DataFrame(features_train)
df_features_test = pd.DataFrame(features_test)

df_features_train.to_csv('train_features.csv', index=False)
df_features_test.to_csv('test_features.csv', index=False)


