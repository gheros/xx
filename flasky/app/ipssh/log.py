#从dnspod批量插入IP

import urllib
import json
import re
import time
def _request_():
    url ="https://dnsapi.cn/Info.Version -d 'login_token=9a2e50dabb92eda52d8d5828bfa2c1a3&format=json'"
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print(data)
    print("接口调用完成")
    return data
_request_()