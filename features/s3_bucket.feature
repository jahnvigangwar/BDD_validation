Feature: S3 Bucket Creation
  As a DevOps engineer
  I want to ensure that the S3 bucket module creates a bucket with the correct configurations

  Scenario: Create an S3 bucket with default settings
    Given I have deployed the S3 bucket module with default settings
    When I apply the Terraform configuration
    Then the S3 bucket should be created
    And the bucket should have the ACL set to private
    And the bucket should have the correct tags
