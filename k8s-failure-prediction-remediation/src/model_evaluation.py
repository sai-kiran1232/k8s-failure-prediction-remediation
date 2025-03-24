import pandas as pd
import joblib
from sklearn.metrics import classification_report

# Load dataset and model
df = pd.read_csv("../data/k8s_metrics.csv")
model = joblib.load("../models/k8s_failure_model.pkl")

# Define Features and Labels
X = df.drop(columns=["failure_label"])
y = df["failure_label"]

# Make Predictions
y_pred = model.predict(X)

# Print Classification Report
print(classification_report(y, y_pred))
