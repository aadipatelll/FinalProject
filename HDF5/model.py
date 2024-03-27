import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the data
df_train = pd.read_csv('train_features_cleaned_marked.csv')
df_test = pd.read_csv('test_features_cleaned_marked.csv')


# Seperate the walk and jump labels from the data, for both train data and test data
X_train = df_train.drop('label', axis=1)
y_train = df_train['label']

X_test = df_test.drop('label', axis=1)
y_test = df_test['label']


# Initialize the logistic regression model
model = LogisticRegression(solver='lbfgs', max_iter=100, C=1.0, class_weight='balanced', random_state=42)
# Train the model
model.fit(X_train, y_train)


# Predict the labels for the test set
y_pred = model.predict(X_test)

# Put the predictions in a seperate CSV file to be analyzed later
test_features_predictions = X_test.copy()
test_features_predictions['label'] = y_pred
test_features_predictions.to_csv('test_features_predictions.csv', index=False)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Test set accuracy: {accuracy}")



