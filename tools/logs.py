def requires_logs(question):
    return any(k in question.lower() for k in ["error", "fail", "exception"])

def request_logs():
    return "Please share relevant logs or error messages."
