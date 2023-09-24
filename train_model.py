import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load a sample dataset (you should use your prepared dataset)
data = load_iris()
X, y = data.data, data.target

# Create and train a sample scikit-learn model (you should use your trained model)
model = RandomForestClassifier(n_estimators=1000)
model.fit(X, y)

# Save the model as a .pkl file
joblib.dump(model, 'your_model.pkl')

