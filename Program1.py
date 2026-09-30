from sklearn.linear_model import LinearRegression

# Data
X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[6]])

print("Predicted value:", prediction[0])