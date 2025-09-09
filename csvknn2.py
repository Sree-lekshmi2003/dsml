import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


data = pd.read_csv('csvfile2.csv') 


X = data[['sweetness', 'curnchiness']]  
y = data['foodtype']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


print("Enter the sample data:")
sweetness = float(input("Sweetness: "))
curnchiness = float(input("Curnchiness: "))

sample = pd.DataFrame([[sweetness, curnchiness]], columns=['sweetness', 'curnchiness'])

pred = knn.predict(sample)
print("Predicted food type:", pred[0])

