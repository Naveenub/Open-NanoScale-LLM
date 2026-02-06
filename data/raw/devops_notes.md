# AWS EC2 and IAM Basics

An EC2 instance accesses AWS services using an IAM role.
If no role is attached, API calls to services like S3 will fail
with AccessDenied errors.

Common issues:
- Missing IAM role
- IAM policy does not allow required action
- Wrong AWS region
