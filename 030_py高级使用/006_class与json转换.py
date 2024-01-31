import json

""" 

python class json编码与解码

(1) dataclass
(2) 手动方式
"""


# (1)
# from dataclasses import dataclass


# @dataclass
# class Account:
#     ID: int
#     Name: str
#     Age: int
#     Weight: float


# (2)
class Account:
    #
    def __init__(self, ID, Name, Age, Weight):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.Weight = Weight

    # '__repr__' 是 Python 类中的一个特殊方法，用于返回一个对象的字符串表示形式。
    # 当我们在控制台中输入一个对象并按回车时，Python 解释器会自动调用对象的'__repr__'方法来获取其字符串的表示形式
    def __repr__(self):
        return f"Account(ID={self.ID}, Name={self.Name}, Age={self.Age}, Weight={self.Weight})"


# 创建一个 Account 实例
account_instance = Account(ID=1, Name="John", Age=25, Weight=68.5)

# 将 Account 实例编码为 JSON 字符串
json_string = json.dumps(account_instance.__dict__)

# 打印编码后的 JSON 字符串
print("Encoded JSON:")
print(json_string)

# 将 JSON 字符串解码为 Account 实例
decoded_account = json.loads(json_string, object_hook=lambda d: Account(**d))

# 打印解码后的 Account 实例
print("\nDecoded Account:")
print(decoded_account)
