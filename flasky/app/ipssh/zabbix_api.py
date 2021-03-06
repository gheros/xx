#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = 'edward'
import json
from urllib import request, parse

ZABBIX_URL = 'https://zabbix.lebosys.org'
ZABBIX_USERNAME = "edward"
ZABBIX_PASSWORD = "34@Shidai"

url = "{}/api_jsonrpc.php".format(ZABBIX_URL)
header = {"Content-Type": "application/json"}
# auth user and password
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": ZABBIX_USERNAME,
        "password": ZABBIX_PASSWORD
    },
    "id": 1,
}
# token='db9e52eb5a42576b50a045649c41375d'
# 由于API接收的是json字符串，故需要转化一下
value = json.dumps(data).encode('utf-8')

# 对请求进行包装
req = request.Request(url, headers=header, data=value)

# 验证并获取Auth ID
try:
    # 打开包装过的url
    result = request.urlopen(req)
except Exception as e:
    print("Auth Failed, Please Check Your Name And Password:", e)
else:
    response = result.read()
    # 上面获取的是bytes类型数据，故需要decode转化成字符串
    page = response.decode('utf-8')
    # 将此json字符串转化为python字典
    page = json.loads(page)
    result.close()
    print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))


# fe9f845b931f05d628e0148b1af7ed62