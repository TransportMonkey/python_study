import re
from collections import Counter

# 过滤英文和数字
# str_ = 'saf546你rt好！436546北fgh5t京fj356'
# result = re.sub(r'[a-zA-Z0-9]','',str_)
# print(result) # 你好！北京

# # 编译正则表达式
# pattern = re.compile(r'\d+')
# str_ = 'adc3434dvv867'
# result = pattern.findall(str_)
# print(result) # ['3434', '867']

# 贪婪模式与非贪婪模式
# 贪婪模式
# html_str = "<div>Hello, <span>world</span>!</div>"
# pattern_greedy = r"<div>.*</div>"
# match_greedy = re.findall(pattern_greedy, html_str)
# print(match_greedy)
# # 非贪婪模式
# pattern_nongreedy = r"<div>(.*?)</div>"
# match_nongreedy = re.findall(pattern_nongreedy, html_str)
# print(match_nongreedy)

# # 用正则匹配日期格式
# date_format = r'\d{4}-\d{2}-\d{2}'
# text = "今天的日期是2018-03-20，明天是2018-03-21。"
# result = re.findall(date_format, text)
# print(result) # ['2018-03-20', '2018-03-21']


# 列表排序
# sort排序
# a = [4,34,6,56,65,642,67,88]
# a.sort() # 从小到大排序
# print(a) # [4, 6, 34, 56, 65, 67, 88, 642]
# a.sort(reverse=True) # 从大到小排序
# print(a) # [642, 88, 67, 65, 56, 34, 6, 4]

# sorted()
# b = [677,54,88,989,454,34,22,4]
# print(sorted(b)) # [4, 22, 34, 54, 88, 454, 677, 989]
# print(sorted(b,reverse=True)) # [989, 677, 454, 88, 54, 34, 22, 4]

# map方法的使用
# def test(num:int):
#     return num**2
# list_ = [1,26,3,4,45,36]
# result = map(test,list_)
# print(list(result)) # [1, 676, 9, 16, 2025, 1296]

# 用random取小数
# import random
# result = random.uniform(2,5)
# print(result) # 3.576450425807785

# 字符串去重
# a = 'addscxfdgbfbfsasdaaaa'
# new_str = ''.join(sorted(set(a))) # 去重并按从小到大排序
# print(new_str)

# 字符串编译方法
# str_ = '你好！做过'
# bytes_ = str_.encode('utf-8')
# print(type(bytes_)) # <class 'bytes'>
# # 反向操作
# res = bytes_.decode('utf-8')
# print(type(res))

# 字典按键大小排序
# a = {'dsd':323,'s':'ftg4','acf':'22'}
# print(sorted(a)) # ['acf', 'dsd', 's']

# 用Counter统计元素出现的次数
# list_ = ['1','2','3','4','5','6','1','2','3','4','5','6']
# result = Counter(list_)
# print(result) # Counter({'1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2})

# filter用法

# def test(num):
#     return num%2==0
# res = filter(test,[1,2,3,4,5,6])
# print(list(res)) # [2, 4, 6]

# a="张明 98分"
# res = re.sub(r'\d+','100',a)
# print(res)

# str_ = '就hash你就开2018-03-20始的反击得分'
# res = re.findall(r'\d{4}-\d{2}-\d{2}',str_)
# print(res)

# list_1 = ['a','b','c','d','e']
# list_2 = [1,2,3,4,5]
# print(list(zip(list_1,list_2)))