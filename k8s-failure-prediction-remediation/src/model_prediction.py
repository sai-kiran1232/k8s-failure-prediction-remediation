import pandas as pd
import joblib

# Load trained model
model = joblib.load("../models/k8s_failure_model.pkl")

# Example new data for prediction
new_data = pd.DataFrame({
    "cpu_usage": [85.5],
    "memory_usage": [92.3],
    "pod_restarts": [4],
    "network_latency": [75.1]
})

# Predict failure
prediction = model.predict(new_data)

# Output result
print(f"🛠️ Predicted Failure: {'Yes' if prediction[0] == 1 else 'No'}")
