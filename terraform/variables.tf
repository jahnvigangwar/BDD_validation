variable "bucket_name" {
  type = string
  default = "jahnvis-bucket-name"
}

variable "acl" {
  type = string
  default = "private"
}

variable "tags" {
  type = map(string)
  default = {"Environment": "dev", "Project": "my-project"}
}
