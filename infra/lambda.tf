data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../${path.module}/src"
  output_path = "../${path.module}/lambda.zip"
}

resource "aws_lambda_function" "this" {
  filename      = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256

  function_name = var.function_name
  role          = var.function_role
  handler       = var.handler
  runtime       = var.runtime
  timeout       = var.timeout

  environment {
    variables = {
      QUEUE_PROCESSAMENTO_URL = var.queue_url
      env = "prod"
    }
  }

  layers = [aws_lambda_layer_version.lambda_layer.arn]
}