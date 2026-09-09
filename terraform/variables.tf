variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "frontend_port" {
  description = "External port for frontend"
  type        = number
}

variable "backend_port" {
  description = "External port for backend"
  type        = number
}