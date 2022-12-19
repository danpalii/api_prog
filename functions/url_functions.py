import requests



def put_request(url, value1, key_name, value2):
    requests.put(url, {"id": value1, key_name : value2})

def post_request(url, value1, key_name, value2):
    requests.post(url, {"id": value1, key_name : value2})

def get_request(url):
    responseVal = requests.get(url)
    response_var = responseVal.json()
    return response_var
