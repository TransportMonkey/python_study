# import copy
# import re

# a = ['a','b','c']
# print(a) # ['a','b','c']
# b = copy.copy(a) # 浅拷贝
# a[0] = 4
# print(a) # [4,'b','c']
# print(b) # [a,'b','c']

# c= [[5,'r'],'d','345']
# print(c) # [[4,'r'],'d','345']
# d = copy.copy(c) # 浅拷贝
# c[0][0] = ['2','f5']
# print(c) # [[55,'r'],'d','345']
# print(d) # [[55,'r'],'d','345']

# f = ['a','b','c']
# print(f) # ['a','b','c']
# g = copy.deepcopy(f)
# f[0] = [1,2,3]
# print(f) # [[1,2,3],'b','c']
# print(g) # ['a','b','c']
# tmp_data = 1
# def test(num):
#     global tmp_data
#     if num > 99:
#         return tmp_data
#     num += 1
#     tmp_data += num
#     return  test(num)
# result = test(1)
# print(result)


# dict_1 = dict((['小林','sss'],['age1',24],['小明','sss'],['age1',22]))
# print(dict_1)

# a = [8,'5',3,4]
# # b = [1,2,3,4]
# # print(id(b[0]))
# # b[0] = 8
# # print(id(b[0]))
# b = copy.copy(a)
# a[1] = 'y'
# print(a) # [8,'y',3,4]
# print(b) # [8,'5',3,4]


# class Test:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(test, cls).__new__(cls)
#         return cls._instance
#     def __init__(self, value):
#         self.value = value
# test = Test(10)

# a = {'aa':12,'bdd':23}
# b = {'ddcv':238,'scf':32}
# new_dict = {**a,**b}
# print(new_dict)



# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# new_foo = sorted(foo,reverse=True,key=lambda x:(x>0,abs(x)))
# print(new_foo)

# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# new_foo = sorted(foo,key=lambda x:x["age"],reverse=True)
# print(new_foo)
# new_foo = sorted(foo,key=lambda x:x["name"])
# print(new_foo)

# 字典按键和值排序
# foo = {"name22":323,"ag2e":19},{"nam4ede":90787,"age":54},{"n3ame":2323,"age":17},{"nade3me":7656,"af3ge":23}
# new_dict = {**foo[0],**foo[1],**foo[2],**foo[3]}
# print(dict(sorted(new_dict.items(),key=lambda item:item[0])))
# print(dict(sorted(new_dict.items(),key=lambda item:item[1])))

# list_ = [('sw',46),('s4gw',65),('r475',76)]
# print(sorted(list_,key=lambda x:x[0]))
# print(sorted(list_,key=lambda x:x[1]))

# 列表嵌套列表，有相同的数字元素，添加参数(x[1],x[0])
# a = [['sds',54],['gf44',433],['gfg56',433],['tfgr',433],['f343',54]]
# print(sorted(a,key=lambda x:x[0]))
# print(sorted(a,key=lambda x:(x[1],x[0])))

# 按键对字典排序（zip方法）
# dict_ = {'sad2':32,'dfvv3':433,'2ed33':86}
# list_ = list(zip(dict_.keys(),dict_.values()))
# item_list = [i for i in list_]
# items_ = sorted(item_list,key=lambda x:x[0])
# # print(key_)
# new_dict = {d[0]:d[1] for d in items_}
# print(new_dict)

# 按键对字典排序（不用zip方法）
# b = {'name':'dsdd','dsw332':434,'dsc34':65,'323dd':4367}
# key_sort = sorted(b.items(), key=lambda x:x[0])
# new_dict = { d[0]:d[1] for d in key_sort}
# print(new_dict)

# list_ = [i for i in range(10)]
# print(list_)
# dict_ = {str(j):i for j,i in enumerate(range(10))}
# print(dict_)
# gen = (i for i in range(10))
# print(gen)

# str_="info:xiaoZhang 33 shandong"
# new_str = re.split(r'[:\s]+',str_)
# print(new_str)

# email_list = ['sd.comjsdnwk@163.com', '163jhdhc@.com', 'lzynsasbndb@163.com', '23213444@163.com']
# for email_ in email_list:
#     ret = re.match('[\w]{4,20}@163\.com$',email_)
#     if ret:
#         print(f'符合：{email_}')
#     else:
#         print(f'不符合:{email_}')

# str_1 = 'sda das '
# print(str_1.replace(' ',''))
# print(''.join(str_1.split(' ')))

# str_ = 'hello world!'
# print(str_.lower()) # 小写
# print(str_.upper()) # 大写

# str_ = 'asdasd4e23rf'
# # print(str_.count('a'))
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]

"""
-5 5 -4 4 
正数：0, 2, 4, 8, 8, 9
负数：-2, -4, -4, -5, -20
"""
# def test(num):
#     return num<0,abs(num)
    # if num < 0:
    #     return 1,abs(num)
    # else:
    #     return 0,abs(num)
# a = -5
# foo = [(True,5),(False,8),(Flase,0),(False,4),(False,9)...]
# new_foo = sorted(foo,key=test) # abs()取绝对值
# # print(new_foo) # [0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]
# # new_for = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# new_for = sorted(foo, key=lambda x:(x<0,abs(x)))
# print(new_foo)
# print(new_for)
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},
#        {"name":"zs","age":17},{"name":"ll","age":23}]

# print(sorted(foo,key=lambda x:(x['name'],x['age'])))
# list_ = [('sw',46),('sw',65),('r475',76)]
# print(sorted(list_,key=lambda x:(len(x[0]),x[1])))
# a = [['sds',54],['gf44',433],['gfg56',433],['tfgr',433],['f343',54]]
# print(sorted(a,key=lambda x:x[1]))

# zip()
# dict_ = {'sad2':32,'dfvv3':433,'2ed33':86}
# ret = list(zip(dict_.keys(),dict_.values()))
# sort_list = sorted(ret,key=lambda x:(len(x[0]),x[1]))
# print(sort_list)
# new_dict = {k:v for k,v in sort_list}
# # print(new_dict)
# str_1 = 'sda das '
# print(str_1.replace(' ',''))
# print(str_1.split(' '))
# print(','.join(str_1.split(' '))) # 'sda,das,'
# print(int("1.4")) # 1.4
# print(int(1.4)) # 1
dict_ = dict(names='小林',age=32)
print(dict_)