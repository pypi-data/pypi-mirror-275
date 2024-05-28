import request.request as rq


# 获取token
def get_token(name, pwd):
    auth_json = {'account': name, 'pwd': pwd}
    return rq.post("/capdata/auth", auth_json)
