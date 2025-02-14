# Flask App Monitoring with Prometheus and Grafana in Kubernetes

This repository contains Kubernetes manifests for deploying a Flask application and monitoring it using Prometheus and Grafana. The setup also includes an Ingress for external access and Horizontal Pod Autoscaler (HPA) for auto-scaling based on CPU utilization.

## Prerequisites
- A Kubernetes cluster
- kubectl configured to interact with the cluster
- Helm installed (for Prometheus and Grafana setup, if required)
- Ingress controller installed (e.g., NGINX Ingress Controller)

## Deployment Overview
### Components
- **Flask Application**: A simple Python Flask app that exposes metrics.
- **Prometheus**: Used for scraping metrics from the Flask app.
- **Grafana**: For visualizing metrics from Prometheus.
- **Ingress**: Manages external access to services.
- **HPA (Horizontal Pod Autoscaler)**: Auto-scales the Flask app based on CPU utilization.

## Deployment Instructions

### 1. Deploy the Flask Application
Apply the following Kubernetes manifests:
```sh
kubectl apply -f deploy.yaml
```

### 2. Deploy Prometheus
```sh
kubectl apply -f configmap.yaml
kubectl apply -f prometheus.yml
```

### 3. Deploy Grafana
```sh
kubectl apply -f grafana.yaml
```

### 4. Install Nginx Ingress controller and deploy ingress yaml

```sh
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```
or using Helm

```sh
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install my-ingress-nginx ingress-nginx/ingress-nginx --version 4.12.0
```
Deploy the ingress yaml

```sh
kubectl apply -f ingress.yaml
```
Ensure DNS is correctly set up for accessing the services via Ingress.

### 5. Installing Metrics server

```sh
kubectl apply -f https://raw.githubusercontent.com/ACloudGuru-Resources/content-cka-resources/master/metrics-server-components.yaml
```

### 6. Enable Auto-Scaling
```sh
kubectl apply -f hpa.yaml
```

## Accessing the Services
- **Flask App**: `http://python.arunm.online`
- **Prometheus**: `http://prometheus.arunm.online`
- **Grafana**: `http://grafana.arunm.online`

## Configuring Prometheus to Scrape Flask Metrics
The `prometheus.yml` configures Prometheus to scrape metrics from the Flask app:
```yaml
scrape_configs:
  - job_name: 'python-app'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['pythonsvc.default.svc.cluster.local:5000']
```

## Visualizing Metrics in Grafana
1. Log in to Grafana.
2. Add Prometheus as a data source.
3. Import a dashboard or create a new one using PromQL queries.

## Monitoring Auto-Scaling
To check the status of the HPA:
```sh
kubectl get hpa
```
To simulate a load for testing scaling:

login to the python pod and run dd command

```sh
dd if=/dev/zero of=/dev/null &
```

## Conclusion
This setup ensures that the Flask app is monitored using Prometheus and Grafana while being scalable with Kubernetes' Horizontal Pod Autoscaler.

