# DEVOPS FA1 & FA2 — Infrastructure as Code, CI/CD, Kubernetes and Monitoring

## 1. Project Overview

This project demonstrates DevOps practices through two assignment phases.

**FA1 — Git-Based Infrastructure as Code and Multi-Environment Container Deployment**

FA1 uses Docker, Terraform and Git to create a frontend and backend application environment. The same Terraform configuration supports QA, UAT and PROD environments through environment-specific variable files.

**FA2 — CI/CD Pipeline, Automated Testing, Kubernetes Deployment and Monitoring**

FA2 extends the application with automated testing, GitHub Actions, Docker image builds, Kubernetes Deployments and Services, Prometheus metrics collection, and Grafana dashboards.

The project demonstrates how application development, containerization, deployment, version control and monitoring can be integrated into a DevOps workflow.

## 2. Objectives

The main objectives are:

- Maintain application source code and infrastructure configuration in Git.
- Provision multiple application environments using reusable Terraform configuration.
- Containerize the frontend and backend applications using Docker.
- Automate application testing and Docker image builds through GitHub Actions.
- Deploy the frontend and backend applications to Kubernetes.
- Demonstrate Kubernetes pod status, scaling and rollout operations.
- Collect application metrics using Prometheus.
- Visualize application and monitoring metrics using Grafana.
- Document the implementation, commands and verification procedures.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Git and GitHub | Source control and repository hosting |
| Terraform | Infrastructure as Code for FA1 |
| Docker | Application containerization and image building |
| Python | Backend application and automated tests |
| Flask | Backend REST-style HTTP endpoints |
| Nginx | Frontend web server |
| GitHub Actions | CI pipeline automation |
| Kubernetes | Application deployment, scaling and service discovery |
| Prometheus | Metrics collection and querying |
| Grafana | Metrics visualization and dashboards |
| YAML | CI/CD, Kubernetes and monitoring configuration |

## 4. Application Architecture

The project contains two main application components.

### 4.1 Frontend

The frontend uses Nginx to serve a web page. Its Docker image is built from the frontend Dockerfile.

- Container port: `80`
- Kubernetes Deployment: `frontend`
- Kubernetes Service: `frontend-service`
- Kubernetes Service type: NodePort
- Configured NodePort: `30080`

### 4.2 Backend

The backend uses Python and Flask to provide HTTP endpoints and application metrics.

- Container port: `5000`
- Kubernetes Deployment: `backend`
- Kubernetes Service: `backend-service`
- Kubernetes Service type: NodePort
- Configured NodePort: `30001`

The backend provides the following endpoints:

| Endpoint | Purpose |
|---|---|
| `/` | Returns application information, environment and status |
| `/health` | Returns the backend health status |
| `/metrics` | Exposes Prometheus metrics |

The `/metrics` endpoint provides request counters and request-duration measurements through the Prometheus Python client.

## 5. Project Structure

The main project structure is:

```text
DEVOPS FA/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── docker/
│   ├── frontend/
│   │   └── Dockerfile
│   └── backend/
│       ├── Dockerfile
│       └── app.py
│
├── tests/
│   └── test_app.py
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── environments/
│       ├── qa.tfvars
│       ├── uat.tfvars
│       └── prod.tfvars
│
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
│
├── monitoring/
│   ├── prometheus.yml
│   ├── prometheus-deployment.yaml
│   └── grafana-deployment.yaml
│
├── .gitignore
└── README.md
```

## 6. FA1 — Infrastructure as Code

### 6.1 Objective

FA1 provisions the frontend and backend Docker environment using Terraform. One Terraform codebase is reused for QA, UAT and PROD by supplying different variable files.

### 6.2 Terraform Configuration

The Terraform directory contains:

- `main.tf` — defines the Docker provider and infrastructure resources.
- `variables.tf` — declares configurable environment and port variables.
- `outputs.tf` — provides environment and application URL outputs.
- `environments/qa.tfvars` — QA-specific values.
- `environments/uat.tfvars` — UAT-specific values.
- `environments/prod.tfvars` — PROD-specific values.

### 6.3 Environment Configuration

| Environment | Frontend Port | Backend Port |
|---|---:|---:|
| QA | 8081 | 5001 |
| UAT | 8082 | 5002 |
| PROD | 8083 | 5003 |

### 6.4 Initialize and Validate Terraform

Run the following commands from the Terraform directory:

```bash
terraform init
terraform fmt
terraform validate
```

`terraform init` initializes the working directory and required provider plugins.

`terraform fmt` formats the Terraform configuration.

`terraform validate` checks the configuration for errors.

### 6.5 Plan and Deploy Environments

QA:

```bash
terraform plan -var-file="environments/qa.tfvars"
terraform apply -var-file="environments/qa.tfvars"
```

UAT:

```bash
terraform plan -var-file="environments/uat.tfvars"
terraform apply -var-file="environments/uat.tfvars"
```

PROD:

```bash
terraform plan -var-file="environments/prod.tfvars"
terraform apply -var-file="environments/prod.tfvars"
```

Review the execution plan before applying infrastructure changes.

### 6.6 Verify FA1 Deployment

Check the Docker containers and images:

```bash
docker ps
docker images
```

Display Terraform outputs:

```bash
terraform output
```

Application URLs for each environment are:

**QA**

- Frontend: `http://localhost:8081`
- Backend: `http://localhost:5001`
- Health endpoint: `http://localhost:5001/health`

**UAT**

- Frontend: `http://localhost:8082`
- Backend: `http://localhost:5002`
- Health endpoint: `http://localhost:5002/health`

**PROD**

- Frontend: `http://localhost:8083`
- Backend: `http://localhost:5003`
- Health endpoint: `http://localhost:5003/health`

Use the environment URLs corresponding to the configuration that is actually running.

## 7. FA2 — Continuous Integration Pipeline

### 7.1 Objective

FA2 introduces an automated CI workflow using GitHub Actions. The workflow runs when code is pushed to the `main` branch, when a pull request targets `main`, or when manually triggered.

Workflow file:

```text
.github/workflows/ci-cd.yml
```

### 7.2 Pipeline Stages

The workflow performs these steps:

1. **Checkout repository:** downloads the repository source code onto the GitHub Actions runner.
2. **Set up Python:** configures Python 3.11.
3. **Install dependencies:** installs Flask and `prometheus-client`.
4. **Run unit tests:** executes the automated backend tests.
5. **Build backend image:** builds the backend Docker image.
6. **Build frontend image:** builds the frontend Docker image.
7. **Verify images:** lists the generated Docker images.

### 7.3 Triggering the Pipeline

Commit and push a change to the main branch:

```bash
git add .
git commit -m "describe the change"
git push origin main
```

Open the repository's **Actions** tab on GitHub to inspect the workflow run.

A green check mark indicates that all workflow steps completed successfully. A red cross indicates that at least one step failed.

### 7.4 Docker Image Tags

The CI workflow builds the following image tags:

```text
devops-fa1-backend:<commit-sha>
devops-fa1-backend:latest
devops-fa1-frontend:<commit-sha>
devops-fa1-frontend:latest
```

The commit-specific tag identifies the source revision used to build the image.

**Pipeline scope:** The current workflow builds images on the GitHub Actions runner. It does not publish images to a remote registry or automatically deploy them to Kubernetes.

## 8. Automated Testing

### 8.1 Test File

Automated backend tests are maintained in:

```text
tests/test_app.py
```

The tests use Python's built-in `unittest` framework and Flask's test client.

### 8.2 Tests Implemented

**Home endpoint test**

- Sends a GET request to `/`.
- Checks that the HTTP status code is `200`.
- Verifies the expected application name and running status.

**Health endpoint test**

- Sends a GET request to `/health`.
- Checks that the HTTP status code is `200`.
- Verifies that the returned status is `healthy`.

### 8.3 Run Tests Locally

Install the dependencies:

```bash
python -m pip install flask prometheus-client
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

Both tests should pass before the code is pushed.

### 8.4 Failure Handling

The unit-test command returns a non-zero exit code when a test fails. Because the GitHub Actions workflow executes the test step before the Docker build steps, a failed test stops the normal pipeline execution.

The expected pipeline sequence is:

```text
Git Push
   |
   v
Checkout Repository
   |
   v
Install Dependencies
   |
   v
Run Unit Tests
   |
   +---- Failure ----> Pipeline Fails
   |
   v
Build Backend Image
   |
   v
Build Frontend Image
   |
   v
Pipeline Success
```

## 9. Docker Containerization

### 9.1 Backend Docker Image

The backend Dockerfile is located at:

```text
docker/backend/Dockerfile
```

It uses Python 3.11 Alpine, installs Flask and `prometheus-client`, copies `app.py`, and starts the Flask application on port `5000`.

Build the backend image locally:

```bash
docker build -t devops-fa1-backend:metrics-v1 ./docker/backend
```

### 9.2 Frontend Docker Image

The frontend Dockerfile is located at:

```text
docker/frontend/Dockerfile
```

It creates an Nginx-based image that serves the frontend web page.

Build the frontend image:

```bash
docker build -t devops-fa1-frontend:latest ./docker/frontend
```

### 9.3 Verify Images and Containers

```bash
docker images
docker ps
```

The CI workflow builds both images automatically on the GitHub runner. Local builds are useful for testing and Kubernetes deployment in Docker Desktop.

## 10. Kubernetes Deployment

### 10.1 Objective

Kubernetes manages the frontend and backend containers. Deployments maintain the desired number of application pods, while Services provide stable access to the pods.

The Kubernetes manifests are stored in:

```text
k8s/
```

### 10.2 Deployment Manifests

| File | Purpose |
|---|---|
| `backend-deployment.yaml` | Defines the backend Deployment and container |
| `backend-service.yaml` | Exposes the backend through a NodePort Service |
| `frontend-deployment.yaml` | Defines the frontend Deployment and container |
| `frontend-service.yaml` | Exposes the frontend through a NodePort Service |

The backend Deployment uses the `devops-fa1-backend` image. The frontend Deployment uses the `devops-fa1-frontend` image.

### 10.3 Apply Kubernetes Resources

Run these commands from the project root:

```bash
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

Check Deployments:

```bash
kubectl get deployments
```

Check pods:

```bash
kubectl get pods
```

Check Services:

```bash
kubectl get services
```

### 10.4 Scaling the Backend

The backend can be scaled by changing the desired replica count:

```bash
kubectl scale deployment backend --replicas=2
```

Verify the result:

```bash
kubectl get pods -l app=backend
kubectl get deployment backend
```

Scaling demonstrates how Kubernetes maintains multiple backend pod replicas.

### 10.5 Rollout Verification

Check the backend rollout:

```bash
kubectl rollout status deployment/backend
```

Check the frontend rollout:

```bash
kubectl rollout status deployment/frontend
```

A successful rollout confirms that Kubernetes has completed the Deployment update.

### 10.6 Updating the Backend Image

For the local Docker Desktop environment, a newly built backend image can be deployed using a unique tag:

```bash
docker build -t devops-fa1-backend:metrics-v1 ./docker/backend
kubectl set image deployment/backend backend=devops-fa1-backend:metrics-v1
kubectl rollout status deployment/backend
```

Using a unique image tag helps avoid ambiguity when updating locally available images.

## 11. Prometheus Monitoring

### 11.1 Objective

Prometheus collects time-series metrics from the backend and its own monitoring service. These metrics can be queried and visualized in Grafana.

The Prometheus configuration file is:

```text
monitoring/prometheus.yml
```

### 11.2 Configuration

The current configuration defines two scrape jobs:

- `prometheus` — collects Prometheus's own metrics.
- `backend` — scrapes the Flask backend's `/metrics` endpoint through `backend-service:5000`.

The scrape interval is configured as 15 seconds.

### 11.3 Prometheus Kubernetes Resources

The file:

```text
monitoring/prometheus-deployment.yaml
```

defines the Prometheus Deployment and Service.

The configuration is supplied through the `prometheus-config` ConfigMap.

If the ConfigMap needs to be created or updated from the project root:

```bash
kubectl create configmap prometheus-config --from-file=prometheus.yml=monitoring/prometheus.yml --dry-run=client -o yaml | kubectl apply -f -
```

Apply the Prometheus resources:

```bash
kubectl apply -f monitoring/prometheus-deployment.yaml
```

Restart Prometheus if a configuration reload is required:

```bash
kubectl rollout restart deployment/prometheus
kubectl rollout status deployment/prometheus
```

### 11.4 Verify Prometheus

Check the Prometheus pod:

```bash
kubectl get pods
```

Forward the Prometheus Service port:

```bash
kubectl port-forward service/prometheus-service 9090:9090
```

Keep the terminal running and open:

- Prometheus interface: `http://localhost:9090`
- Targets: `http://localhost:9090/targets`
- Query interface: `http://localhost:9090/graph`

The backend target should show `UP`.

### 11.5 Application Metrics

The Flask backend exposes metrics using the Prometheus Python client.

**Request counter**

```promql
sum(backend_http_requests_total)
```

This query counts the recorded HTTP requests across backend request labels.

**Request duration rate**

```promql
rate(backend_http_request_duration_seconds_sum[5m])
```

This query shows the rate at which accumulated request-processing time increases over five minutes. It is not the average duration per request.

**Average request duration**

```promql
rate(backend_http_request_duration_seconds_sum[5m])
/
rate(backend_http_request_duration_seconds_count[5m])
```

This query calculates average request duration in seconds when requests have occurred during the selected interval.

## 12. Grafana Dashboard

### 12.1 Objective

Grafana visualizes metrics collected by Prometheus through a monitoring dashboard.

The Grafana Kubernetes resources are defined in:

```text
monitoring/grafana-deployment.yaml
```

### 12.2 Access Grafana

Forward the Grafana Service port:

```bash
kubectl port-forward service/grafana-service 3000:3000
```

Keep the terminal running and open:

```text
http://localhost:3000
```

Sign in with the credentials configured for your local Grafana deployment. Change demonstration credentials before using the setup outside a local lab.

### 12.3 Configure the Prometheus Data Source

Configure a Prometheus data source in Grafana.

For the Kubernetes deployment, the Prometheus Service URL is:

```text
http://prometheus-service:9090
```

Use **Save & test** to verify the connection.

### 12.4 Dashboard Panels

The project dashboard is named:

**FA2 DevOps Monitoring Dashboard**

The four panels are:

1. **Prometheus Target Availability** — shows the availability of Prometheus scrape targets using the `up` metric.
2. **Total Prometheus HTTP Requests** — displays HTTP request activity for the Prometheus server.
3. **Total Backend Requests** — displays the backend request counter.
4. **Backend Request Duration Rate** — visualizes the rate of accumulated backend request-processing time.

The dashboard combines monitoring-service metrics with application-specific metrics.

## 13. Git Version Control

Git maintains the source code, Dockerfiles, Terraform configuration, Kubernetes manifests, monitoring configuration and documentation.

Check the current working tree:

```bash
git status
```

Review recent commits:

```bash
git log --oneline -10
```

Stage changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "describe the change"
```

Push commits to GitHub:

```bash
git push origin main
```

The GitHub Actions workflow runs automatically when a commit is pushed to `main`.

## 14. .gitignore

The `.gitignore` file excludes generated files and local artifacts that should not normally be tracked.

Examples include:

```text
.terraform/
*.tfstate
*.tfstate.*
crash.log
crash.*.log
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
```

Terraform state files and generated Python files are excluded to keep the repository clean.

## 15. End-to-End Verification Checklist

Before the demonstration, verify each component.

### Git and CI/CD

- [ ] Source code and configuration are committed to Git.
- [ ] Latest changes are pushed to GitHub.
- [ ] GitHub Actions completes successfully.
- [ ] Unit tests pass.
- [ ] Both Docker images build successfully.

### Docker

- [ ] Backend image builds successfully.
- [ ] Frontend image builds successfully.
- [ ] Docker images can be inspected using `docker images`.

### Kubernetes

- [ ] Frontend Deployment is available.
- [ ] Backend Deployment is available.
- [ ] Frontend and backend pods are running.
- [ ] Services are configured correctly.
- [ ] Backend scaling can be demonstrated.
- [ ] Deployment rollout status can be checked.

### Prometheus and Grafana

- [ ] Prometheus pod is running.
- [ ] Backend scrape target is `UP`.
- [ ] Backend metrics can be queried.
- [ ] Grafana connects to Prometheus.
- [ ] Dashboard panels display metrics.
- [ ] Application request and duration metrics are visible.

### Documentation

- [ ] README reflects the actual configuration.
- [ ] Commands correspond to the project files.
- [ ] Final changes are committed and pushed.

## 16. Limitations and Implementation Scope

The current GitHub Actions workflow checks out the repository, installs Python dependencies, runs unit tests, and builds the frontend and backend Docker images.

The workflow does not currently publish images to an external container registry or automatically deploy the application to Kubernetes. Kubernetes deployment is performed using the configured local cluster and `kubectl` commands.

The Prometheus configuration scrapes Prometheus itself and the Flask backend. Although Kubernetes CPU and memory usage can be inspected using `kubectl top`, those values are not automatically exported to Grafana by the current Prometheus configuration.

These distinctions describe the actual implementation and identify possible future enhancements.

## 17. Conclusion

FA1 demonstrates Infrastructure as Code by reusing Terraform configuration to provision Docker-based QA, UAT and PROD environments.

FA2 extends the project with GitHub Actions, automated unit tests, Docker image builds, Kubernetes Deployments and Services, application metrics, Prometheus and Grafana.

Together, the two assignments demonstrate version control, infrastructure automation, application testing, containerization, orchestration and monitoring in a practical DevOps workflow.