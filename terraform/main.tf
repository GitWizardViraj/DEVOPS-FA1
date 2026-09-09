terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

resource "docker_image" "frontend" {
  name = "devops-fa1-frontend:${var.environment}"

  build {
    context    = "../docker/frontend"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "frontend" {
  name  = "devops-fa1-frontend-${var.environment}"
  image = docker_image.frontend.image_id

  ports {
    internal = 80
    external = var.frontend_port
  }
}

resource "docker_image" "backend" {
  name = "devops-fa1-backend:${var.environment}"

  build {
    context    = "../docker/backend"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "backend" {
  name  = "devops-fa1-backend-${var.environment}"
  image = docker_image.backend.image_id

  env = [
    "ENVIRONMENT=${var.environment}"
  ]

  ports {
    internal = 5000
    external = var.backend_port
  }
}