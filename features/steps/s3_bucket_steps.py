#import statements
import os
import boto3
import json
import time
from python_terraform import Terraform
from behave import given, when, then
from botocore.exceptions import ClientError
import subprocess


terraform = Terraform()

def get_s3_client():
    return boto3.client('s3', region_name='ap-northeast-1')


@given('I have deployed the S3 bucket module with default settings')
def step_impl(context):
    context.bucket_name = "jahnvis-bucket-name"
    context.SetTags = {"Environment": "dev", "Project": "my-project"}
    context.terraform_options = {
        'Bucket': context.bucket_name,
        'acl': 'private',
        'tags': {"Environment": "dev", "Project": "my-project"}
    }
    return_code, stdout, stderr = terraform.init()
    assert return_code == 0

@when('I apply the Terraform configuration')
def step_impl(context):
    # print("present working dir: ", os.getcwd())
    os.chdir('terraformFiles')

    # Change to the desired directory using a shell command
    # subprocess.call(f"cd terraformFiles", shell=True)


    return_code, stdout, stderr = terraform.apply(skip_plan=True, auto_approve=True)
    assert return_code == 0
    time.sleep(10)  # Wait for AWS to propagate changes

@then('the S3 bucket should be created')
def step_impl(context):
    s3_client = get_s3_client()
    print("Printing the boto3 instance for s3: ", s3_client)
    try:
        s3_client.head_bucket(Bucket =context.bucket_name)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            assert False, f"Bucket name does not exist: {e}"
        elif error_code == '403':
            assert False, f"Access to the bucket name is forbidden: {e}"
        else:
            assert False, f"Unexpected error: {e}"

@then('the bucket should have the ACL set to private')
def step_impl(context):
    s3_client = get_s3_client()
    acl = s3_client.get_bucket_acl(Bucket=context.bucket_name)
    s3_client.head_bucket(Bucket =context.bucket_name)
    assert any(grant['Permission'] == 'FULL_CONTROL' for grant in acl['Grants']), "Bucket ACL is not private"

@then('the bucket should have the correct tags')
def step_impl(context):
    s3_client = get_s3_client()
    tagging = s3_client.get_bucket_tagging(Bucket=context.bucket_name)
    tags = {tag['Key']: tag['Value'] for tag in tagging['TagSet']}
    expected_tags = {"Environment": "dev", "Project": "my-project"}
    assert tags == expected_tags, f"Bucket tags do not match: {tags} != {expected_tags}"
