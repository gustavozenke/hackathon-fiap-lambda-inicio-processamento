terraform {
  backend "s3" {
    bucket = "hackathon-fiap-terraform-tfstate"
    key    = "lambda-inicio-processamento.tfstate"
    region = "us-east-1"
  }
}