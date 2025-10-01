# Project Architecture

This document outlines the full architecture of the project, from **CI/CD with GitHub Actions** to **Kubernetes deployment with Ingress**.

---

## Architecture Diagram
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub        │    │   Docker         │    │   Kubernetes    │
│   Actions       │───▶│   Registry       │───▶│   Cluster       │
│   (CI/CD)       │    │   (Images)       │    │   (Deployment)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                                               │
         ▼                                               ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Ansible       │    │   Prometheus     │    │   Grafana       │
│   (Config Mgmt) │    │   (Metrics)      │    │   (Dashboard)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘


---

## Component Details

### 1. GitHub Actions (CI/CD)
- Automates build, test, and deployment.
- Triggered on `push` to the `main` branch.
- Integrates with Docker to build and push images.

### 2. Docker Registry
- Stores container images.
- GitHub Actions pushes updated images here.
- Kubernetes pulls images from the registry for deployment.

### 3. Kubernetes Cluster
- Manages deployment, scaling, and service discovery.
- Contains **Deployment**, **Service**, and **Ingress** resources.
- Ingress routes external traffic to services.

### 4. Ansible (Configuration Management)
- Optional but useful for managing cluster nodes or configuration updates.
- Can automate tasks like secret management or rolling updates.

### 5. Prometheus (Monitoring)
- Scrapes metrics from applications and Kubernetes cluster.
- Provides insights on performance and health.

### 6. Grafana (Dashboard)
- Connects to Prometheus to visualize metrics.
- Provides dashboards for monitoring application and cluster performance.

---

## Workflow

1. **Code Commit**: Developer pushes code to GitHub.
2. **CI/CD Triggered**: GitHub Actions builds and tests code.
3. **Docker Image**: GitHub Actions builds Docker image and pushes to registry.
4. **Kubernetes Deployment**: Cluster pulls the latest image and updates deployment.
5. **Ingress**: Routes traffic to application services.
6. **Monitoring**: Prometheus collects metrics; Grafana visualizes them.
7. **Configuration Management**: Ansible applies configuration changes as needed.

---

## Notes

- **Secrets Management**: Use GitHub Secrets and Kubernetes Secrets for credentials.
- **Ingress Controller**: Required to route traffic (NGINX or other).
- **Scaling**: Kubernetes Deployment supports replicas for high availability.
- **Observability**: Prometheus + Grafana setup allows monitoring of application and cluster health.
