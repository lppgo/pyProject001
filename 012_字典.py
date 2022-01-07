#! /usr/bin/env python
# -*- coding:utf-8 -*-

# -----------------------------字典dict (kv)-----------------------
# 字典是无序的
map = {
    "apple": 1,
    "pear": 2,
    "orange": "3",
}

print(map["apple"])
# 新增一个元素
map["banana"] = 5
# 删除一个元素
del map["pear"]
print(map)

# 判断一个key是否在字典中
if "apple3" in map:
    print(map["apple"])
else:
    print("key apple is not in map! ")


# 遍历字典
knights = {'one': 'Go', 'two': "Python", 3: 'Java', 4: 'C'}

" 使用items()可以获取dict的k,v "
for k, v in knights.items():
    print(k, v)

" 普通遍历dict，只取key "
for v in knights:
    print(v)
