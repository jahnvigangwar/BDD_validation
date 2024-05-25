provider "aws" {
    region = "ap-northeast-1"  
}

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
  acl    = var.acl
  tags = var.tags
}
