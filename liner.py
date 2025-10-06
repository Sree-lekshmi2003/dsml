import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
diabetes = datasets.load_diabetes()
print("Feature names in diabetes dataset:")
print(diabetes.feature_names)
X, y = datasets.load_diabetes(return_X_y=True)
X_bmi = X[:, np.newaxis, 2]
print("\nShape of BMI feature matrix:", X_bmi.shape)
X_train = X_bmi[:-20]
X_test = X_bmi[-20:]
y_train = y[:-20]
y_test = y[-20:]
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
bmi_input = float(input("\nEnter a BMI value (standardized): "))
user_input = np.array([[bmi_input]])
user_prediction = model.predict(user_input)
print(f"Predicted disease progression for BMI {bmi_input}: {user_prediction[0]:.2f}")
print("\nModel Coefficients:")
print(f"Coefficient (slope): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

