import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

data = pd.read_csv('csvfile2.csv')
print(data.head())

X = data[['sweetness', 'curnchiness']]
y = data['foodtype']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

print("Enter the sample data:")
sweetness = float(input("Sweetness: "))
curnchiness = float(input("Curnchiness: "))

sample = pd.DataFrame([[sweetness, curnchiness]], columns=['sweetness', 'curnchiness'])

pred = model.predict(sample)
print("Predicted food type:", pred[0])

