variable "function_name" {
  type        = string
  default     = "hackathon-inicio-processamento"
}

variable "function_role" {
  type        = string
  default     = "arn:aws:iam::369780787289:role/LabRole"
}

variable "handler" {
  type        = string
  default     = "application.router.lambda_handler.lambda_handler"
}

variable "runtime" {
  type        = string
  default     = "python3.9"
}

variable "timeout" {
  type        = number
  default     = 60
}

variable "queue_url" {
  type        = string
  default     = "https://sqs.us-east-1.amazonaws.com/369780787289/sqs-processamento"
}