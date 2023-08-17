from .external import call_external_api

def check_response_greater_than_0_5():
    response = call_external_api()

    if "response_value" not in response:
        raise KeyError("Response 缺少 Key: response_value")
    elif response["response_value"] > 0.5:
        return True
    else:
        return False