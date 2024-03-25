import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

################# 
# Load the data
df_train = pd.read_csv('train_features_marked.csv')  # replace 'your_data.csv' with your actual file path

# Separate features and target variable
X_train = df_train.drop('Label', axis=1)  # Assuming 'class' column contains the labels 'walking' or 'jumping'
y_train = df_train['Label']

df_test = pd.read_csv('test_features_marked.csv')

# Separate features and target variable
X_test = df_test.drop('Label', axis=1)  # Assuming 'class' column contains the labels 'walking' or 'jumping'
y_test = df_test['Label']


# Initialize the logistic regression model
model = LogisticRegression(solver='lbfgs', max_iter=100, C=1.0, class_weight='balanced', random_state=42)
# Train the model
model.fit(X_train, y_train)



# Predict the classes for the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Test set accuracy: {accuracy}")