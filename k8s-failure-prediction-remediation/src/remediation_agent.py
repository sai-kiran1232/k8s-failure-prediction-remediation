import joblib
import numpy as np
from kubernetes import client, config

# Load Kubernetes Configuration
config.load_kube_config()
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

# Load ML Model
model = joblib.load("../models/k8s_failure_model.pkl")

# Simulated Kubernetes Metrics
def get_k8s_metrics():
    return {
        "cpu_usage": np.random.uniform(20, 90),
        "memory_usage": np.random.uniform(30, 95),
        "pod_restarts": np.random.randint(0, 5),
        "network_latency": np.random.uniform(10, 100),
    }

# Predict Issue
def predict_issue(metrics):
    data = np.array([[metrics["cpu_usage"], metrics["memory_usage"], metrics["pod_restarts"], metrics["network_latency"]]])
    return model.predict(data)[0]

# Remediation Actions
def scale_pods(deployment_name, namespace, replicas):
    scaling_body = {"spec": {"replicas": replicas}}
    apps_v1.patch_namespaced_deployment_scale(deployment_name, namespace, scaling_body)
    print(f"Scaled {deployment_name} to {replicas} replicas")

def restart_pods(namespace):
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        if pod.status.phase != "Running":
            v1.delete_namespaced_pod(pod.metadata.name, namespace)
            print(f"Restarted pod: {pod.metadata.name}")

# Monitoring Loop
while True:
    metrics = get_k8s_metrics()
    issue = predict_issue(metrics)

    if issue == 1:
        print("⚠️ Issue Detected! Running remediation...")
        restart_pods("default")
        scale_pods("my-app", "default", 5)
    else:
        print("✅ Cluster running smoothly.")
