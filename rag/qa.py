from tools.aws import requires_aws_context, aws_missing_info
from tools.logs import requires_logs, request_logs
from tools.api import requires_api_info, request_api_details

def precheck(question):
    if requires_aws_context(question):
        return aws_missing_info()
    if requires_logs(question):
        return request_logs()
    if requires_api_info(question):
        return request_api_details()
    return None

msg = precheck(question)
if msg:
    return msg
    
