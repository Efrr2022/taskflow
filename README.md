# TaskFlow API

A production-grade task management REST API built to demonstrate modern Docker containerization, security hardening, and multi-service orchestration using FastAPI, MySQL, Redis, Nginx, and Distroless containers.

---

# Architecture

```text
Internet → Nginx (Reverse Proxy) → FastAPI API → MySQL + Redis
```

| Service | Technology | Purpose |
|---|---|---|
| API | Python + FastAPI | REST API endpoints |
| Database | MySQL 8.0 | Persistent task storage |
| Cache | Redis 7 | Task counters & caching |
| Proxy | Nginx | Reverse proxy & TLS termination |

---

# Features

- Multi-stage Docker builds
- Distroless production runtime
- Redis caching integration
- MySQL persistent storage
- Nginx reverse proxy
- Docker Compose orchestration
- Health checks with dependency chaining
- Security-hardened containers
- Development & production override configurations
- Bind mounts for hot reload development

---

# What This Project Demonstrates

## Docker & Containerization
- Multi-stage builds
- Distroless images
- Docker networking
- Volumes & bind mounts
- Health checks
- Compose overrides
- Environment variable management

## Security Hardening
- Non-root container user
- Read-only filesystem
- Dropped Linux capabilities
- `no-new-privileges`
- Reduced CVE surface
- Distroless runtime image

## Infrastructure Concepts
- Reverse proxy architecture
- Service isolation
- Network segmentation
- Dependency orchestration
- Production vs development environments

---

# Security Highlights

- Distroless runtime image
- Zero critical vulnerabilities in base image
- Containers run as non-root user
- Read-only container filesystem
- All Linux capabilities dropped except `NET_BIND_SERVICE`
- Secrets managed via `.env`
- Internal database network isolation
- Docker Scout vulnerability scanning

---

# Image Optimization

| Stage | Before | After |
|---|---|---|
| Image Size | ~270MB | ~85MB |
| Vulnerabilities | Multiple Critical/High | Reduced attack surface |
| Runtime | Full Linux | Distroless |

---

# Project Structure

```text
taskflow/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│   └── ...
│
├── nginx/
│   └── nginx.conf
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose.override.yml
├── docker-compose.prod.yml
├── .env.example
└── README.md
```

---

# Quick Start

## Prerequisites

- Docker Desktop
- Git

---

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/taskflow.git
cd taskflow
```

---

## Configure Environment Variables

```bash
cp .env.example .env
```

Update the `.env` file with your values.

---

## Run Development Environment

```bash
docker compose up --build
```

API available at:

```text
http://localhost/docs
```

---

# Production Deployment

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/users` | Register user |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |
| GET | `/stats` | Redis-backed statistics |

---

# Docker Compose Architecture

## Base Compose
`docker-compose.yml`

Contains:
- Core services
- Networks
- Security settings
- Health checks
- Volumes

---

## Development Override
`docker-compose.override.yml`

Contains:
- Bind mounts
- Hot reload
- Debug logging
- Local port exposure

---

## Production Override
`docker-compose.prod.yml`

Contains:
- Production scaling
- Resource limits
- Optimized runtime settings

---

# Container Security Configuration

## Security Features Used

```yaml
cap_drop:
  - ALL

cap_add:
  - NET_BIND_SERVICE

security_opt:
  - no-new-privileges:true

read_only: true
```

---

# Health Checks

All services implement container health checks:

- API endpoint validation
- MySQL readiness checks
- Redis ping checks
- Dependency startup ordering

---

# Docker Scout Scanning

Example vulnerability scanning:

```bash
docker scout quickview taskflow-api
docker scout cves taskflow-api
```

---

# Development Workflow

## Rebuild Containers

```bash
docker compose build --no-cache
```

---

## Restart Services

```bash
docker compose up -d
```

---

## View Logs

```bash
docker logs taskflow-api
```

---

## Enter Debug Container

```bash
docker exec -it taskflow-debug sh
```

---

# Networking

## Internal Networks

| Network | Purpose |
|---|---|
| frontend | Public-facing services |
| backend | Internal services only |

The database is isolated from public access.

---

# Technologies Used

- Python 3.11
- FastAPI
- SQLAlchemy
- MySQL 8
- Redis 7
- Nginx
- Docker
- Docker Compose
- Distroless Images

---

# Learning Roadmap

This repository evolves week-by-week while learning cloud-native infrastructure.

## Week 1
- Docker fundamentals
- Multi-stage builds
- Volumes
- Networking
- Distroless images
- Security hardening

## Week 2
- Kubernetes Pods
- Deployments
- Services

## Week 3
- StatefulSets
- Jobs & CronJobs
- Resource limits

## Week 4
- Ingress
- TLS
- Network Policies

## Week 5
- Persistent Volumes
- StorageClasses

## Week 6
- RBAC
- Horizontal Pod Autoscaler
- Rolling deployments

## Week 7
- Helm charts

## Week 8-9
- AWS ECS Fargate
- CI/CD pipelines
- GitHub Actions

---

# Future Improvements

- JWT Authentication
- Role-based access control
- HTTPS with Let's Encrypt
- Prometheus monitoring
- Grafana dashboards
- Kubernetes deployment manifests
- Helm packaging
- GitHub Actions CI/CD

---

# Author

Built as a hands-on cloud-native infrastructure and container security learning project.

---

