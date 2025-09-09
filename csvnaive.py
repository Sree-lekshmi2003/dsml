import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


data = pd.read_csv('csvfile1.CSV')  


X = data[['Height', 'Weight']]
y = data['T-shirt']




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


model = GaussianNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


print("Enter the sample data:")
h = int(input("Height in cm: "))
w = int(input("Weight in kg: "))
sample = pd.DataFrame([[h, w]], columns=['Height', 'Weight'])


pred = model.predict(sample)
pred_label = le.inverse_transform(pred)
print("Predicted T-shirt size:", pred_label[0])

