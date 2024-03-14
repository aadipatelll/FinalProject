import h5py
import numpy as np 
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
    with h5py.File(filename, "r") as f:
        for segment in f['segments']:
            features = extract_features(segment)
            print(features)

except Exception as e :
    print("Dang")

df_train = pd.DataFrame(train_set)
df_test = pd.DataFrame(test_set)

