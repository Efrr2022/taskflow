#!/bin/bash
# Deploy TaskFlow to Kubernetes
# Usage: bash k8s/deploy.sh

set -e

echo "Deploying TaskFlow to Kubernetes..."

echo "Creating namespace..."
kubectl apply -f k8s/namespace.yaml

echo "Applying config and secrets..."
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/limitrange.yaml
kubectl apply -f k8s/resourcequota.yaml

echo "Deploying data layer..."
kubectl apply -f k8s/mysql-statefulset.yaml
kubectl apply -f k8s/redis.yaml

echo "Waiting for MySQL to be ready..."
kubectl rollout status statefulset/mysql -n taskflow --timeout=120s

echo "Deploying API..."
kubectl apply -f k8s/api.yaml
kubectl rollout status deployment/taskflow-api -n taskflow --timeout=120s

echo "Deploying CronJob..."
kubectl apply -f k8s/cronjob.yaml

echo ""
echo "TaskFlow deployed successfully!"
kubectl get all -n taskflow