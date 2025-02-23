provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "popa_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "popa_subnet" {
  vpc_id            = aws_vpc.popa_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_eks_cluster" "popa_eks" {
  name     = "popa-eks-cluster"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = [aws_subnet.popa_subnet.id]
  }
}
