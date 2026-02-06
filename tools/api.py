def requires_api_info(question):
    return "api" in question.lower()

def request_api_details():
    return "Provide endpoint URL, method, auth type, and sample request."
