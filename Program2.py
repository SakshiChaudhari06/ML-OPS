from sklearn.tree import DecisionTreeClassifier

# Data
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5]])

print("Predicted class:", prediction[0])