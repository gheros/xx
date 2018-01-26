#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import re
#
# ZABBIX_URL = 'https://zabbix.lebosys.org'
# ZABBIX_USERNAME = "edward"
# ZABBIX_PASSWORD = "34@Shidai"
url = 'https://zabbix.lebosys.org/api_jsonrpc.php'
username = 'edward'
password = '34@Shidai'


# 登陆
def requestJson(url, values):
    data = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data, {'Content-Type': 'application/json-rpc'})
    response = urllib.request.urlopen(req, data)
    a = response.read().decode(encoding='utf-8')
    output = json.loads(a)
    #    print output
    try:
        message = output['result']
    except:
        message = output['error']['data']
        print(message)
        quit()

    return output['result']


##登陆的API
def authenticate(url, username, password):
    values = {'jsonrpc': '2.0',
              'method': 'user.login',
              'params': {
                  'user': username,
                  'password': password
              },
              'id': '0'
              }
    idvalue = requestJson(url, values)
    return idvalue


# auth的值
auth = authenticate(url, username, password)
print(auth)
#version
def version(auth):
    values = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": auth,
    "id": 1
}
    output = requestJson(url, values)
    return output
print(version(auth))



##查询组ID {'groupid': '8', 'name': 'Switch'}
def groups(auth):
    values = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": ["groupid", "name"],
        },
        'auth': auth,
        'id': '1'
    }
    output = requestJson(url, values)
    return output


b = groups(auth)
print(b)

##查询主机  {'hostid': '10108',
def hosts(auth):
    values = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["groupid", "name"],
            "groupids": "8",
        },
        'auth': auth,
        'id': '1'
    }
    output = requestJson(url, values)
    return output


host = hosts(auth)
host1 = []
host2 = []
for i in range(len(host)):
    host1.append(host[i]['name'])
    host2.append(host[i]['hostid'])

host3 = dict(zip(host1, host2))
print(host3)
print(host)


##查询主机项目 {'key_': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'itemid': '26399'}
def item(auth):
    values = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": ["itemids", "key_"],
            "hostids": "10108",
        },
        'auth': auth,
        'id': '1'
    }
    output = requestJson(url, values)
    return output


print(item(auth))

##查询项目的历史值  'lastvalue': '-14760.0000'
def his(auth, itemids):
    values = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "history": 0,
            "itemids": itemids,
            "sortfield": "itemid",
            "sortorder": "DESC",
            "limit": 1
        },
        'auth': auth,
        'id': '1'
    }
    output = requestJson(url, values)
    return output


# print(his(auth,26399))

##查询触发项目值和监控项目  {'description': 'xxxxxxxxxxxxxxx', 'hostname': 'xxxxxxxxxxxxxxx', 'items': [{'itemid': '26399'}], 'triggerid': '17030'}
def trigger(auth, hostid):
    values = {
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "output": [
                "description",
            ],
            "filter": {
                "hostid": hostid,
            },
            "selectItems": "",
            "sortfield": "hostname",
            "sortorder": "DESC"
        },
        'auth': auth,
        'id': '1'
    }
    output = requestJson(url, values)
    return output

    ###简单使用案例，可查考，根据触发器查找历史。
    t1 = trigger(auth, host3[msg['Content']])
    t2 = []
    t3 = []
    for i in range(len(t1)):
        t5 = t1[i]['items'][0]  ##   'items': [{'itemid': '26399'}]
        t6 = his(auth, t5['itemid'])  ##   his(auth,26399)
        t2.append(t1[i]['description'])  ##监控项目描述
        t3.append(round(float(t6[0]['lastvalue'])) / 1000)  ##项目ID 的值
    t4 = dict(zip(t2, t3))
    t8 = []
    for k in t4:
        t7 = k + ":" + "{}".format(t4[k]) + "db"
        t8.append(t7)
    t9 = "\n".join(t8)