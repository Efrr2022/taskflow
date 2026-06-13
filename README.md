# TaskFlow API

A production-grade task management REST API built to demonstrate modern cloud-native application development using FastAPI, MySQL, Redis, Docker, and Kubernetes.

The project follows a hands-on DevOps learning journey, progressing from containerization fundamentals to Kubernetes orchestration and cloud deployment.

---

## Architecture

### Docker Architecture

```text
Internet
    │
    ▼
 Nginx Reverse Proxy
    │
    ▼
 FastAPI Application
    │
 ┌──┴──┐
 ▼     ▼
MySQL Redis
```

### Kubernetes Architecture

```text
┌──────────────────────────────────────────────┐
│              taskflow namespace              │
│                                              │
│ Internet                                     │
│    │                                         │
│    ▼                                         │
│ NodePort Service                             │
│    │                                         │
│    ▼                                         │
│ TaskFlow API Deployment (2 Replicas)         │
│    │                                         │
│ ┌──┴─────────────┐                           │
│ ▼                ▼                           │
│ MySQL            Redis                       │
│ StatefulSet      Deployment                  │
│ PVC: 1Gi         In-Memory Cache             │
│                                              │
│ CronJob → Automated MySQL Backups            │
└──────────────────────────────────────────────┘
```

---

# Technology Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| API              | FastAPI               |
| Database         | MySQL 8               |
| Cache            | Redis 7               |
| Reverse Proxy    | Nginx                 |
| Containerization | Docker                |
| Orchestration    | Kubernetes            |
| Runtime          | Distroless Containers |
| Platform         | Minikube              |
| Operating System | WSL Ubuntu            |

---

# Key Features

## Application Features

* RESTful task management API
* MySQL persistent storage
* Redis caching and statistics
* Health monitoring endpoints
* Production-ready configuration

## Docker Features

* Multi-stage builds
* Distroless runtime images
* Docker Compose orchestration
* Bind mounts for development
* Environment-based configuration
* Health checks and dependency management

## Kubernetes Features

* Deployments and ReplicaSets
* StatefulSets with Persistent Volumes
* Services and Service Discovery
* Startup, Readiness, and Liveness Probes
* Resource Requests and Limits
* ResourceQuota and LimitRange
* Rolling Updates and Rollbacks
* CronJobs for automated backups
* Node Affinity
* Taints and Tolerations
* Self-healing workloads

---

# Security Features

* Non-root containers
* Distroless runtime images
* Read-only filesystems
* Dropped Linux capabilities
* no-new-privileges security option
* Network isolation
* Environment-based secrets management
* Reduced attack surface

---

# Deployment

## Prerequisites

* Docker Desktop
* Minikube
* kubectl
* WSL Ubuntu
* Git

---

## Build Application Image

```bash
minikube docker-env | Invoke-Expression
docker build -t taskflow-api:latest .
```

---

## Deploy to Kubernetes

```bash
bash k8s/deploy.sh
```

---

## Access Application

```bash
minikube service taskflow-api-svc -n taskflow --url
```

---

# Useful Commands

## View Resources

```bash
kubectl get all -n taskflow
```

## Watch Pods

```bash
kubectl get pods -n taskflow -w
```

## View Logs

```bash
kubectl logs -l app=taskflow-api -n taskflow
```

## Check Resource Usage

```bash
kubectl top pods -n taskflow
```

## Deployment Status

```bash
kubectl rollout status deployment/taskflow-api -n taskflow
```

## Rollback Deployment

```bash
kubectl rollout undo deployment/taskflow-api -n taskflow
```

---

# Learning Journey

## Week 1 – Docker & Containerization ✅

* Multi-stage builds
* Docker networking
* Volumes and bind mounts
* Distroless containers
* Security hardening
* Docker Compose

## Week 2 – Kubernetes Fundamentals ✅

* Namespaces
* Deployments
* Services
* ReplicaSets
* StatefulSets
* Persistent Volumes
* Health Probes
* Resource Management
* CronJobs
* Scheduling
* Rolling Updates

## Upcoming Topics

### Week 3

* Jobs
* DaemonSets
* Advanced Scheduling

### Week 4

* Ingress
* TLS
* Network Policies

### Week 5

* StorageClasses
* Dynamic Provisioning

### Week 6

* RBAC
* Horizontal Pod Autoscaler
* Production Operations

### Week 7

* Helm Charts

### Week 8–9

* AWS ECS Fargate
* Amazon ECR
* GitHub Actions
* CI/CD Pipelines

---

# Learning Outcomes

This project demonstrates practical experience in:

* Containerization with Docker
* Production container security
* Kubernetes workload management
* Service discovery and networking
* Persistent storage management
* Health monitoring and self-healing
* Resource governance
* Automated backups
* Deployment automation
* Cloud-native application architecture

---

## Author

**Efrem Sultan**

GitHub: https://github.com/Efrr2022
