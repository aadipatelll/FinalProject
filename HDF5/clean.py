import pandas as pd

# 
def clean_df(df):
    for col in df.columns:
        try:
            df[col] = df[col].str.extract(r'([-]?\d+\.\d+)').astype(float) # Extract floating point numbers and discard all other data
        except AttributeError:  # If column is already proper numeric type, this error is raised, in which case it will just do nothing
            pass
    return df

# Load the data, clean it, then make new CSV files for the cleaned data
df_train = pd.read_csv('train_features.csv')
df_test = pd.read_csv('test_features.csv')


df_cleaned_test = clean_df(df_test.copy())
df_cleaned_train = clean_df(df_train.copy())

df_cleaned_train.to_csv('train_features_cleaned.csv', index=False)
df_cleaned_test.to_csv('test_features_cleaned.csv', index=False)

