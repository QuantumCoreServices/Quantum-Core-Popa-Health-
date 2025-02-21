provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}


resource "aws_subnet" "public_2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"
}

resource "aws_db_subnet_group" "db_subnet_group" {
  name       = "patient-db-subnet-group"
  subnet_ids = [aws_subnet.public.id, aws_subnet.public_2.id] # Ideally, you should have subnets in at least two AZs.

  tags = {
    Name = "Patient DB Subnet Group"
  }
}

resource "aws_instance" "rhel_instance" {
  ami           = "ami-04017a1d5060f436f" # Added opening quote and corrected placement
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  key_name      = "Shinobi"

  tags = {
    Name = "PatientPortal-RHEL"
  }
}


resource "aws_db_instance" "patient_db" {
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  db_name           = "patientdb" # Use db_name instead of name
  username          = "postgresadmin"
  password          = "var.db_password"

  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.db_subnet_group.name
}

resource "aws_security_group" "db_sg" {
  name        = "db_security_group"
  description = "Allow access to RDS"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_s3_bucket" "patient_portal_bucket" {
  bucket = "patient-portal-data-bucket-unique"
  # acl argument removed; use aws_s3_bucket_acl instead
}

resource "aws_s3_bucket_versioning" "patient_portal_bucket_versioning" {
  bucket = aws_s3_bucket.patient_portal_bucket.id

  versioning_configuration {
    status = "Enabled"
  }

  depends_on = [aws_s3_bucket.patient_portal_bucket]

}

terraform {
  required_providers {
    time = {
      source  = "hashicorp/time"
      version = "~> 0.9"
    }
  }
}

resource "time_sleep" "wait_for_bucket" {
  depends_on      = [aws_s3_bucket.patient_portal_bucket]
  create_duration = "10s" # Adjust the duration as needed
}

resource "aws_lambda_function" "ml_service" {
  filename      = "ml_service.zip"
  function_name = "PatientPortalMLService"
  handler       = "ml_service.handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_exec_role.arn
  timeout       = 30
}

resource "aws_api_gateway_rest_api" "ml_api" {
  name = "PatientPortalMLAPI"
}

resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/aws/patientportal/app"
  retention_in_days = 30
}

resource "aws_iam_role" "lambda_exec_role" {
  name               = "lambda_exec_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Action": "sts:AssumeRole",
    "Principal": { "Service": "lambda.amazonaws.com" },
    "Effect": "Allow"
  }]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
