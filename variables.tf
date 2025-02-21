variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "rhel_ami" {
  description = "us-east-1"
  type        = string
  default     = "us-east-1" # Replace with a valid RHEL AMI ID
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

variable "key_pair" {
  description = "AWS key pair for the EC2 instance"
  type        = string
  default     = "Shinobi"
}

variable "db_password" {
  description = "Password for the PostgreSQL database"
  type        = string
  sensitive   = true
}


