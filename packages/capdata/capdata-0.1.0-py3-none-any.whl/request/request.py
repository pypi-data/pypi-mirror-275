import requests
import json

from request import PATH


# get 请求
def get(url, params, token):
    headers = {'Accept': 'application/json', 'content-type': 'application/json', 'x-access-token': token}
    response = requests.get(PATH + url, json=params, headers=headers).text
    res = json.loads(response)
    code = res["respCode"]
    if str(code) == 'SUCCEED':
        if 'data' in res:
            return res["data"]
        else:
            return None
    else:
        raise Exception(res["message"])


# post 请求
def post(url, params, token=""):
    headers = {'Accept': 'application/json', 'content-type': 'application/json'}
    if token.strip() != "":
        headers.setdefault('x-access-token', token)
    response = requests.post(PATH + url, json=params, headers=headers).text
    res = json.loads(response)
    code = res["respCode"]
    if str(code) == 'SUCCEED':
        if 'data' in res:
            return res["data"]
        else:
            return None
    else:
        raise Exception(res["message"])
