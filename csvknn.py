import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

# Load CSV data
data = pd.read_csv('csvfile1.CSV')  # Make sure this file exists in the same directory

# Features and label
X = data[['Height', 'Weight']]
y = data['T-shirt']

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=1)

# Create and fit KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)  # This must run before predict()

# Predict and evaluate
y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Predict for new sample
print("Enter the sample data:")
h = int(input("Height in cm: "))
w = int(input("Weight in kg: "))

sample = pd.DataFrame([[h, w]], columns=['Height', 'Weight'])

pred = knn.predict(sample)
pred_label = le.inverse_transform(pred)
print("Predicted T-shirt size:", pred_label[0])

