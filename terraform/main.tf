provider "aws" {
  region = "ap-northeast-1"
  access_key = "AKIA6GBMBHOYU2RWXCM3"
  secret_key = "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"
}


resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
  acl    = var.acl
  tags = var.tags
}
