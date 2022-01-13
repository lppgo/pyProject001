#!/usr/bin/env python

""" """
""" --------------- json数据解析 ---------------
1：json.dumps(): 对数据进行编码
2：json.loads(): 对数据进行解码

"""
import json

data = {"no": 1, "url": "www.google.com", "name": "lucas"}

# Python 字典类型转换为 JSON 对象
json_str = json.dumps(data)
print("json_str : {}".format(json_str))

# 将 JSON 对象转换为 Python 字典
json_data = json.loads(json_str)
print("json_data : {}".format(json_data))

print(repr(data))
