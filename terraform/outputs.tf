output "environment" {
  value = var.environment
}

output "frontend_url" {
  value = "http://localhost:${var.frontend_port}"
}

output "backend_url" {
  value = "http://localhost:${var.backend_port}"
}

output "backend_health_url" {
  value = "http://localhost:${var.backend_port}/health"
}