def requires_aws_context(question):
    keywords = ["ec2", "s3", "iam", "lambda", "vpc", "ecr"]
    return any(k in question.lower() for k in keywords)

def aws_missing_info():
    return "Please provide AWS region, account context, and service name."
