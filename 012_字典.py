#! /usr/bin/env python
# -*- coding:utf-8 -*-

# -----------------------------字典dict (kv)-----------------------
""" 
List列表是有序的对象集合，
Dictionary字典(Map)是无序的对象集合
两者之间的区别在于: 
    字典当中的元素是通过键来存取的，而不是通过偏移存取

Dictionary字典是一种映射类型，字典用 {} 标识，它是一个无序的 键(key) : 值(value) 的集合

Key的类型必须是不可变类型(number,string,tuple),且不可重复
创建空字典使用{}
 """

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
