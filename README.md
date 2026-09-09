# DEVOPS FA1 — Git-Based Infrastructure as Code and Multi-Environment Container Deployment

## 1. Objective

The objective of this assignment is to implement a Docker-based application environment using Terraform and Git while supporting QA, UAT and PROD environments using a single Terraform codebase.

The application environment consists of:

- Container 1: Frontend/Web application
- Container 2: Backend/API application

Terraform is used to provision the Docker environment, while Git is used for version control.

The same Terraform configuration is reused for QA, UAT and PROD without creating separate copies of the infrastructure code.

---

## 2. Technologies Used

- Git
- Docker
- Terraform
- Nginx
- Python
- Flask

---

## 3. Project Structure

```text
DEVOPS FA/
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
├── docker/
│   ├── frontend/
│   │   └── Dockerfile
│   └── backend/
│       └── Dockerfile
│
├── .gitignore
└── README.md
4. Application Containers
4.1 Frontend Container

The frontend application uses Nginx.

The frontend Dockerfile builds an Nginx-based container that serves a simple web page.

The frontend container exposes port 80 internally.

4.2 Backend Container

The backend application uses Python Flask.

The backend provides:

Application endpoint
Health-check endpoint

The backend container exposes port 5000 internally.

5. Environment Configuration

The same Terraform code is used for all three environments.

Environment	Frontend Port	Backend Port
QA	8081	5001
UAT	8082	5002
PROD	8083	5003

Environment-specific values are stored in separate .tfvars files.

6. Terraform Files
main.tf

Contains the Docker provider and infrastructure resources for:

Frontend Docker image
Frontend Docker container
Backend Docker image
Backend Docker container
variables.tf

Defines variables used by the Terraform configuration:

Environment
Frontend port
Backend port
outputs.tf

Provides:

Environment name
Frontend URL
Backend URL
Backend health URL
7. Environment Files
QA

The QA environment uses:

environment = qa
frontend port = 8081
backend port = 5001

Deployment command:

terraform apply -var-file="environments/qa.tfvars"
UAT

The UAT environment uses:

environment = uat
frontend port = 8082
backend port = 5002

Deployment command:

terraform apply -var-file="environments/uat.tfvars"
PROD

The PROD environment uses:

environment = prod
frontend port = 8083
backend port = 5003

Deployment command:

terraform apply -var-file="environments/prod.tfvars"
8. Terraform Initialization

Terraform is initialized using:

terraform init

This downloads and initializes the required Docker provider.

9. Terraform Validation

The Terraform configuration can be checked using:

terraform validate

Terraform formatting can be performed using:

terraform fmt
10. Terraform Planning

Before applying infrastructure changes, Terraform can create an execution plan.

QA
terraform plan -var-file="environments/qa.tfvars"
UAT
terraform plan -var-file="environments/uat.tfvars"
PROD
terraform plan -var-file="environments/prod.tfvars"
11. Environment Deployment
QA Deployment
terraform apply -var-file="environments/qa.tfvars"

The QA frontend is available at:

http://localhost:8081

The QA backend is available at:

http://localhost:5001

The QA health endpoint is:

http://localhost:5001/health
UAT Deployment
terraform apply -var-file="environments/uat.tfvars"

The UAT frontend is available at:

http://localhost:8082

The UAT backend is available at:

http://localhost:5002

The UAT health endpoint is:

http://localhost:5002/health
PROD Deployment
terraform apply -var-file="environments/prod.tfvars"

The PROD frontend is available at:

http://localhost:8083

The PROD backend is available at:

http://localhost:5003

The PROD health endpoint is:

http://localhost:5003/health
12. Docker Verification

Running Docker containers can be checked using:

docker ps

Docker images can be checked using:

docker images

The running containers should include the frontend and backend containers for the selected environment.

For example, the PROD environment uses:

devops-fa1-frontend-prod
devops-fa1-backend-prod
13. Terraform Outputs

Terraform outputs can be displayed using:

terraform output

For PROD, the outputs include:

environment = "prod"
frontend_url = "http://localhost:8083"
backend_url = "http://localhost:5003"
backend_health_url = "http://localhost:5003/health"
14. Backend Health Check

The backend provides a health endpoint:

/health

For example, the PROD health endpoint is:

http://localhost:5003/health

A successful response confirms that the backend container is running and responding correctly.

15. Multi-Environment Implementation

The main requirement of the assignment is achieved by using a single Terraform codebase for all environments.

The Terraform configuration is defined only once:

terraform/
├── main.tf
├── variables.tf
└── outputs.tf

Different environment-specific values are supplied using:

terraform/environments/
├── qa.tfvars
├── uat.tfvars
└── prod.tfvars

Therefore, the same infrastructure code can be used as follows:

Same Terraform Code
        |
        +---- qa.tfvars ----> QA
        |
        +---- uat.tfvars ---> UAT
        |
        +---- prod.tfvars --> PROD

No separate Terraform infrastructure code is created for QA, UAT or PROD.

16. Git Version Control

Git is used to maintain the project and track changes.

Git repository initialization:

git init

Files can be checked using:

git status

Files can be staged using:

git add .

Changes can be committed using:

git commit -m "Commit message"

Commit history can be viewed using:

git log --oneline
17. .gitignore

Terraform-generated files such as state files and the .terraform directory are excluded from Git using .gitignore.

Examples include:

.terraform/
*.tfstate
*.tfstate.*
crash.log
crash.*.log

This prevents local Terraform state and generated files from being unnecessarily committed to the repository.

18. Verification Summary

The completed implementation demonstrates:

Git-based project management
Docker containerization
Frontend container deployment
Backend/API container deployment
Terraform infrastructure provisioning
Terraform validation and planning
QA environment deployment
UAT environment deployment
PROD environment deployment
Reusable Terraform configuration
Environment-specific .tfvars configuration
Docker container verification
Backend health checking
Terraform output verification
19. Conclusion

This assignment demonstrates Infrastructure as Code using Terraform with Docker and Git.

A frontend and backend application environment is provisioned using Terraform. The same Terraform infrastructure code supports QA, UAT and PROD through environment-specific .tfvars files.

This approach avoids duplicating infrastructure code and provides a reusable and maintainable multi-environment deployment structure.


Press:

```text
Ctrl + S
Step 2 — Check Git Difference

Go back to your CMD.

You should be at:

C:\Users\Viraj Deshmukh\Desktop\DEVOPS FA>

Run:

git diff -- README.md

You should now see the larger README changes.

Don't commit yet.

Step 3 — Important correction

Your previous README ended at:

└── README.md

without a newline. That's why Git showed:

\ No newline at end of file

The new README will end normally, so that's fine.

📸 Don't take a screenshot of the diff

The diff isn't important evidence for the assignment.

Instead, after saving the README, send me the output of:

git status