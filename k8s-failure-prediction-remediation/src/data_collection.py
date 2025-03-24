import pandas as pd
import numpy as np

# Set random seed for consistency
np.random.seed(42)

# Generate synthetic Kubernetes metrics
num_samples = 1000
data = {
    "cpu_usage": np.random.uniform(20, 95, num_samples),  # Simulated CPU usage %
    "memory_usage": np.random.uniform(30, 98, num_samples),  # Simulated Memory usage %
    "pod_restarts": np.random.randint(0, 5, num_samples),  # Random pod restarts
    "network_latency": np.random.uniform(10, 120, num_samples),  # Simulated network latency (ms)
    "failure_label": np.random.choice([0, 1], size=num_samples, p=[0.8, 0.2])  # 80% Normal, 20% Failure
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("../data/k8s_metrics.csv", index=False)
print("✅ Sample dataset saved: data/k8s_metrics.csv")
